# Video Intelligence

CCTV feeds with Cosmos-powered alerts for real-time business intelligence

Video Intelligence is a Cosmos-powered CCTV app for real-time business intelligence and automatic alerts. A dashboard brings events and business metrics together; each event links to the source footage for review on desktop or mobile.

[Website](https://atelierneyra.com/video) · [Open demo](https://preview.atelierneyra.com/apps/video/control-room/#view=location&period=year) · [Product tour](docs/product-tour.md) · [Documentation](https://docs.atelierneyra.com/video/overview/)

[![Video Intelligence retail dashboard beside mobile source-video and visitor review](https://atelierneyra.com/assets/product-motion-v5/video-bfd81a0d96af.jpg)](https://preview.atelierneyra.com/apps/video/control-room/#view=location&period=year)

RetailAction footage by Standard Cognition. [Source licence and attribution](docs/images/NOTICE).

The starter opens the retained 45-recording retail sample, with its actual processing results, tracks and source licences.

## From a business metric to the camera

1. **Open Home → Annual.** See the retained location dashboard and its historical period.
2. **Open a tracker.** Follow a summary into its detailed history or individual occurrences.
3. **Choose View footage.** Play the relevant recording and inspect its camera-local visitor chapters, frames and evidence.
4. **Inspect the follow-up.** Queue watch, Empty shelf watch and Shop summary define recurring agent work over admitted events; activation uses your inputs, budget and delivery setup.

## Product areas

| Area | What it does |
| --- | --- |
| Dashboard | Connect business summaries to the detailed tracker behind each number. |
| Nine retail trackers | Follow visitors, product interactions, pickups, returns, baskets, queues, shelves, sales and conversion. |
| Video review | Inspect the recording interval and source evidence behind an event. |
| Cosmos processing | Ingest and index recordings, retrieve useful intervals and inspect selected clips. |
| Evidence admission | Validate source identity, clocks, profiles and labels before computing maintained metrics. |
| Agents and alerts | Define queue/shelf watches and a periodic shop summary from committed observations. |

The demo uses the retained 45-recording trial, with model answers, publisher references and generated history labelled separately. The alert jobs are inactive definitions; connect and test your own cameras, processing and delivery to continue the live workflow.

[Product tour](docs/product-tour.md) follows the dashboard experience and maps its modules. [Implementation and trial evidence](docs/implementation.md) retains the processing results, tracker layers and exact acceptance boundaries.

## Run the interface

Use Python 3.12 and FFmpeg, including `ffmpeg` and `ffprobe` on your PATH.

```sh
git clone https://github.com/latintzar/camera-video-search.git
cd camera-video-search
make install
make dev
```

Open **http://127.0.0.1:18530/control-room/#view=location&period=year**. Read the private `~/.local/state/camera-video-search/owner-code.txt` file and enter its one-use code. The starter downloads a checksummed 119 MB sample, creates your own workspace and runs the original Python backend. The same code and sample power the hosted preview. Home opens the retained historical period; open a tracker, then choose **View footage** for its source. The Rocoto mark returns to Home. [Sample contents and licences](docs/processed-sample.md).


[Product tour](docs/product-tour.md) · [Getting started](docs/get-started.md) · [Workflows](docs/workflows.md) · [Architecture](docs/video-architecture.md) · [Setup](docs/video-setup.md) · [Design decisions](docs/video-design.md) · [Function reference](docs/video-reference.md)

## Implementation and licence

[Implementation and retained evidence](docs/implementation.md) · [Trial status](docs/video-status.md) · [Agent setup skill](.agents/skills/video-operations-setup/SKILL.md)

Original code and authored fixtures use [MIT](LICENSE). Libraries, fonts, models and marks retain their [own terms](THIRD_PARTY.md). The sample’s Standard.AI and CC BY-SA 4.0 terms and attribution travel with its files; see [sample licences](docs/processed-sample.md#source-licences).

[made by atelier neyra](https://atelierneyra.com)
