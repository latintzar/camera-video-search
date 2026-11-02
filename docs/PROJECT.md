# Video Intelligence

Video Intelligence is a Cosmos-powered CCTV app for real-time business intelligence and automatic alerts. A dashboard brings events and business metrics together; each event links to the source footage for review on desktop or mobile.

[Product tour](product-tour.md) follows the location dashboard into trackers, footage and source-linked evidence. The source retains ingestion, indexing, Cosmos adapters and the shared agent harness.

A recording contains hours of activity. A useful answer needs to point back to the exact clip and frame, and a business metric needs a consistent rule for which observations count.

| Feature | What it does |
| --- | --- |
| Source recordings | Browse and play the retained camera recordings at the moment behind an observation. |
| Cosmos processing | The source includes ingestion, indexing and model adapters for processing footage. |
| Evidence review | Review observations, references and admission before using them in a tracker. |
| Retail trackers | Nine deterministic trackers compute results from admitted observations. |
| Agent integration | The original harness connects scoped tools, workspace records and retail interfaces. |

## Workflow

Camera recording → Cosmos processing → Source-linked observations → Evidence review → Deterministic trackers

## Design decisions

- A model observation keeps its source identity and frame location.
- Evidence admission and deterministic tracker calculations are separate from model generation.

## Status and next steps

The native preview opens the latest completed retained retail trial, with 45 recordings and the original processing results. The source includes the processing path; fresh model runs require an appropriate configured runtime and provider. Connect an owned camera dataset, commission processing and evaluate the observations against the business question.

Source: [docs/processed-sample.md](../docs/processed-sample.md), [docs/video-architecture.md](../docs/video-architecture.md), [docs/video-design.md](../docs/video-design.md), [docs/video-setup.md](../docs/video-setup.md).
