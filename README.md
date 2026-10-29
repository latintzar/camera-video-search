# Video Search

Video Search is a tool for searching and reviewing camera footage.

[Website](https://atelierneyra.com/video) · [Open app](https://preview.atelierneyra.com/?project=video) · [Documentation](https://docs.atelierneyra.com/video/overview/)

Its retail workspace connects source recordings, model observations and nine deterministic trackers.

Originally **Rocoto Video**, built on the Vitrina Harness. This source beta includes the original retail interface, ingestion and indexing code, Cosmos adapters, source-scoped playback, observation admission, nine deterministic trackers and the shared agent workspace.

![Video Search reviewing a RetailAction camera recording](docs/assets/readme-hero.png)

RetailAction footage by Standard Cognition. [Source licence and attribution](docs/images/NOTICE).

The starter opens the retained 45-recording retail sample, with its actual processing results, tracks and source licences.

## Run the interface

Use Python 3.12 and FFmpeg, including `ffmpeg` and `ffprobe` on your PATH.

```sh
git clone https://github.com/latintzar/camera-video-search.git
cd camera-video-search
make install
make dev
```

Open **http://127.0.0.1:18530/control-room/#clip=retailaction-000027-rank0**. Read the private `~/.local/state/camera-video-search/owner-code.txt` file and enter its one-use code. The starter downloads a checksummed 119 MB sample, creates your own workspace and runs the original Python backend. The same code and sample power the hosted preview. The first view opens a recording from the latest completed trial. The Rocoto mark opens Home; choose **Annual** to see the retained historical period. [Sample contents and licences](docs/processed-sample.md).


[Getting started](docs/get-started.md) · [Workflows](docs/workflows.md) · [Architecture](docs/video-architecture.md) · [Setup](docs/video-setup.md) · [Design decisions](docs/video-design.md) · [Function reference](docs/video-reference.md)

## Included work

| Layer | Implementation | Evidence |
| --- | --- | --- |
| Interface | Home, tracker canvases, camera player, visitor chapters, onboarding and workspace | Original UI over the retained processed sample |
| Sources | Resumable upload, link/folder/SFTP intake, immutable versions, preparation and worker readiness | Offline protocol tests; connected services have separate commissioning |
| Semantic index | Cosmos Embed on H100, exported CPU text tower, persistent Qdrant generations | Original executed trials and retained code; current release checks use local fixtures/fake transports |
| Detailed inspection | Selected-clip Cosmos inspection, caching, evidence derivation and bounded compute | Original paid trials; fresh provider acceptance remains separate |
| Observations and trackers | Clock/identity admission, provenance, baskets, nine core processors, typed tile/canvas output | Retained model answers, publisher references, generated history and source tests |
| Shared workspace | Accounts, conversations, agents, recipes, tools, permissions and spending | Included Vitrina Harness implementation; managed execution uses a recipient OpenAI project |

The sample preserves nine recordings with archived model answers, including four views from the latest completed trial. That trial produced 17 quarantined observations. Publisher annotations and generated business history retain their own provenance. [Sample guide](docs/processed-sample.md) · [Status and historical trials](docs/video-status.md).

## Original launch artwork

![Original launch illustration](docs/images/original-illustration.webp)

Fictional, AI-generated launch scenes. [Artwork provenance](provenance/marketing-assets.json).

## Continue the work

```sh
make test
python tools/source-map.py
```

Each guide links the actual implementation and records its boundary. The [agent setup skill](.agents/skills/video-operations-setup/SKILL.md) follows the same path. Keep recipient credentials and state outside source through [the configuration helper](docs/video-setup.md).

Original code and authored fixtures use [MIT](LICENSE). Vendored libraries, fonts, model weights and marks retain their [own terms](THIRD_PARTY.md). The downloadable retail sample carries the Standard.AI Dataset License and CC BY-SA 4.0 separately; its full terms and attribution travel with the files.

[made by atelier neyra](https://atelierneyra.com)
