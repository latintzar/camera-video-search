# Getting started

## First result

Use Python 3.12. Install FFmpeg and its `ffprobe` tool before running the CPU media checks. On Ubuntu:

```sh
sudo apt-get update
sudo apt-get install --no-install-recommends -y ffmpeg
```

```sh
make install
make dev
```

The server binds to `127.0.0.1:18530`. Open `http://127.0.0.1:18530/control-room/#clip=retailaction-000027-rank0`. Use the one-use code saved in `~/.local/state/camera-video-search/owner-code.txt`.

The first start downloads the checksummed retained retail sample: 45 recordings, original person tracks, archived model answers, dataset references and the saved business history. The backend imports that sample into your own private stores. [Sample contents and licences](processed-sample.md).

On Home, choose **Annual** to see the saved historical period. Open a tracker to inspect its history, then choose **View footage**. The native player provides camera selection, visitor chapters, playback speed, camera-view paths and distinct **Cosmos 8B** and **Dataset annotations · evaluation reference** layers.

The starter uses the original SQLite reader and local workspace stores. It clears ambient provider configuration and blocks outside networking. A different private state path is available:

```sh
.venv/bin/python tools/dev.py --state "$HOME/.local/state/video-example" --port 18530
```

## State and restart

The state directory contains access hashes, workspace membership, source/profile/observation records, tracker outputs and the source-scoped media bundle. A product marker protects unrelated directories. Repeating the start retains the imported recording identities and saved records; each run issues a new private access code.

Stop with Ctrl+C and run the same command to reopen the saved workspace. The original backend reads the saved observations. Their output and the underlying recordings survive a process restart. The starter keeps background processing off so the retained sample stays reproducible.

## Optional source work

`tools/render-fixture.py` regenerates the separate small protocol-test recording with Pillow and FFmpeg. Its recipe and hashes live in `examples/`. The provider paths are documented separately in [Setup](video-setup.md). For an offline source check, run `make test`.

[made by atelier neyra](https://atelierneyra.com)
