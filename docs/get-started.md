# Getting started

## First result

```sh
make install
make dev
```

The server binds to `127.0.0.1:18530`. Use the one-use code saved in `~/.local/state/video-operations/owner-code.txt`.

The included twelve-second video depicts a synthetic shop and one labelled visitor. Three supplied annotations describe touching, picking up and returning an example item. The existing source/clock/identity admission code saves those records, and the original processors publish nine tracker outputs. The example's one visitor and three interactions are fixture values.

From Home, open a tracker to inspect its history. Choose **View footage** to open the native player, select the visitor and seek through its chapters. The player identifies its model layer as **Authored annotations**.

The starter uses the original SQLite reader and local workspace stores. It clears ambient provider configuration and blocks outside networking. A different private state path is available:

```sh
.venv/bin/python tools/dev.py --state "$HOME/.local/state/video-example" --port 18530
```

## State and restart

The state directory contains access hashes, workspace membership, source/profile/observation records, tracker outputs and the source-scoped media bundle. A product marker protects unrelated directories. Repeating the seed retains the recording identity and observation keys; each run issues a new private access code.

Stop with Ctrl+C and run the same command to reopen the saved workspace. The original business processors compute from saved observations. Their output and the underlying recording survive a process restart.

## Optional source work

`tools/render-fixture.py` regenerates the included owned media with Pillow and FFmpeg. Its recipe and hashes live in `examples/`. The provider paths are documented separately in [Setup](video-setup.md). For an offline source check, run `make test`.

[made by atelier neyra](https://atelierneyra.com)
