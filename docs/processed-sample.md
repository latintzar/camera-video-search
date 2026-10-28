# Processed retail sample

The starter and hosted preview run the same original application and retained retail workspace. The sample is a versioned GitHub release; [its descriptor](../examples/processed-retail.json) pins the archive and every-file manifest by SHA256.

| Material | Contents |
| --- | --- |
| Recordings | 45 source recordings, posters, crops and camera-local person tracks |
| Latest completed model trial | Four RetailAction views, six windows; completed 9 October 2026 at 16:56 UTC |
| Archived model answers | Nine recordings, including five earlier trials |
| Latest trial admission | 17 raw observations, all retained in quarantine; zero reviewed observations |
| Publisher annotations | 68 dataset-reference events, separate from model answers |
| Business history | The original generated history, marked `data_basis: generated_history` |
| Interface | Home, nine trackers and their histories, products, camera playback, visitor chapters and source evidence |

The sample preserves native revision `21e1a5a8a6936631bd7a`. Its retained bundle was rebuilt on 24 October 2026; that is its packaging date. `processing-receipt.json` records the actual completed run, window timings and raw-answer hashes. The admission audit stays in `bundle/revisions/21e1a5a8a6936631bd7a/qa/model-output-audit.json`.

Choose **Annual** on Home to inspect the historical data. The weekly and monthly controls use the current calendar, as they do in the original application. The preview's shared data stays at the retained snapshot; recipient installations can continue with their own sources and provider configuration.

## Start and inspect

Run `make install`, then `make dev`. The first start downloads approximately 119 MB into `~/.cache/camera-video-search/processed-retail-2026-10-09`. Every file is verified before import. The original backend reads private SQLite stores and serves the actual media with HTTP byte ranges.

Use the private code in `~/.local/state/camera-video-search/owner-code.txt`. Open Home, choose a tracker, then use **View footage**. In the player settings, **Cosmos 8B** selects archived admitted model observations; **Dataset annotations · evaluation reference** selects the publisher's reference labels. Quarantined raw answers remain inspectable in the admission audit.

The importer creates a fresh company identity and access registry. It retains the recording-local logical principal needed by existing visit identifiers, with a newly issued local owner code. The portable package contains five data stores and the source-scoped camera bundle. Source credentials, provider accounts, conversations and billing records stay with their owning services.

`tools/dev.py` clears ambient provider configuration, disables the background tracker runner and custom execution, and fences provider networking. Reading this sample uses the CPU backend and retained outputs. Configuring fresh model calls follows [Setup](video-setup.md).

For a machine with the verified sample already available:

```sh
.venv/bin/python tools/dev.py --sample-dir /absolute/path/to/processed-retail-sample \
  --state "$HOME/.local/state/camera-video-search" --port 18530
```

The synthetic shop in `examples/` remains a small protocol test fixture. The retained processed sample is the starter's default.

## Host a preview

The same backend can mount below an existing site's URL path:

```sh
.venv/bin/python tools/dev.py --state "$HOME/.local/state/video-public" \
  --public-preview --prefix /apps/video \
  --public-origin https://preview.example.com --port 18530
```

Reverse-proxy that path to the loopback listener, preserving the original Host header. The entry is `/apps/video/control-room/#clip=retailaction-000027-rank0`. Historical Home opens at `/apps/video/control-room/#view=location&period=year`.

Public visitors use a newly issued native observer session over the retained sample. A server wrapper admits reads and enforces the read-only contract before the native handlers. Source URLs and cookie paths are mounted on the server; camera byte ranges and event streams retain their native transport. The session cookie is HttpOnly, SameSite Strict and Secure at the configured HTTPS origin. Changes run in the recipient's own workspace.

## Source licences

RetailAction was published by **Standard Cognition (Standard AI)** under the [Standard.AI Dataset License](https://huggingface.co/datasets/standard-cognition/RetailAction/blob/main/LICENSE). Its licence allows redistribution with attribution, the licence and the required NOTICE, and includes separate commercial terms. The package contains that complete licence and NOTICE, and each recording displays its source credit. Source anonymisation and camera-local identity scope are preserved.

The Intel recordings were curated by **Parker Lischwe** and published in [Intel's Video Summarization For Retail dataset](https://huggingface.co/datasets/Intel/Video_Summarization_For_Retail) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Original clips and the derived posters, crops, tracked overlays and annotations retain that attribution and licence. The package includes the source card and full licence text.

Original adapters and generated business-history records use this project's MIT licence. Dataset material retains the terms above. Model weights have the separate terms listed in [Third-party notices](../THIRD_PARTY.md).

[made by atelier neyra](https://atelierneyra.com)
