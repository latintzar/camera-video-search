"""The CLI process owns worker shutdown before caller-owned state can be removed."""
from pathlib import Path
import json
import os
import signal
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = Path(__file__).resolve().parents[2]


@unittest.skipUnless(os.name == "posix", "The source runtime uses POSIX process groups.")
class DevLifecycleTest(unittest.TestCase):
    def test_cli_waits_for_its_worker_shutdown(self):
        with tempfile.TemporaryDirectory(prefix="video-worker-lifecycle-") as temporary:
            root = Path(temporary)
            tools = root / "tools"
            tools.mkdir()
            (root / "harness").mkdir()
            # Run the exact shipped entry point; substitute its expensive media/server imports.
            (tools / "dev.py").write_bytes((ROOT / "tools/dev.py").read_bytes())
            (tools / "processed_sample.py").write_text("""
from pathlib import Path
def verify_sample(path): return Path(path)
def download_sample(): raise AssertionError("A local sample was supplied.")
def install_sample(state, sample):
    state = Path(state); state.mkdir()
    return {"state": str(state), "owner_code_file": "fixture", "basis": "fixture", "provider_calls": 0}
""")
            (root / "harness/server.py").write_text("def create_app(state): return state\n")
            (tools / "uvicorn.py").write_text("""
import json, os, signal, time
def run(state, **kwargs):
    def stop(signum, frame):
        time.sleep(.15)
        (state / "shutdown.json").write_text(json.dumps({"pid": os.getpid()}))
        raise SystemExit(0)
    signal.signal(signal.SIGTERM, stop)
    (state / "ready.json").write_text(json.dumps({"pid": os.getpid()}))
    while True: time.sleep(.01)
""")
            state = root / "state"
            command = [sys.executable, str(tools / "dev.py"), "--state", str(state), "--sample-dir", str(root), "--port", "18531"]
            process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, start_new_session=True)
            try:
                for _ in range(250):
                    if (state / "ready.json").exists(): break
                    if process.poll() is not None:
                        self.fail("CLI exited before readiness: " + process.stderr.read().decode())
                    time.sleep(.02)
                else:
                    self.fail("Worker did not become ready.")
                worker = json.loads((state / "ready.json").read_text())["pid"]
                self.assertEqual(worker, process.pid, "The CLI must retain ownership of the long-lived worker.")
                process.terminate()
                self.assertEqual(process.wait(timeout=5), 0)
                self.assertEqual(json.loads((state / "shutdown.json").read_text())["pid"], worker)
            finally:
                try: os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError: pass
                if process.poll() is None: process.wait(timeout=5)
                if process.stderr: process.stderr.close()


if __name__ == "__main__": unittest.main()
