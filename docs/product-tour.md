# Product tour

Video Intelligence is a Cosmos-powered CCTV app for real-time business intelligence and automatic alerts. A dashboard brings events and business metrics together; each event links to the source footage for review on desktop or mobile.

Security cameras capture the business all day. You need relevant events, timely alerts and useful metrics linked to the footage that explains them.

## A retail metric leads back to the camera

1. **Open the dashboard.** Open Home and select Annual for the retained historical period. Visitors, product handling, baskets, queues, shelves, sales and conversion have their own tracker tiles.
2. **Inspect a tracker.** Open its detailed canvas to follow the history or occurrence behind the summary. The tile and full canvas use the same output revision.
3. **Review the source footage.** Choose View footage and seek the relevant recording. Camera-local visitor chapters, source frames and observation intervals keep the event attached to the video that explains it.
4. **Check the evidence layer.** Inspect archived Cosmos observations separately from Dataset annotations · evaluation reference. The latest model trial’s raw candidates remain in its admission audit.
5. **Define the operational follow-up.** Queue watch, Empty shelf watch and Shop summary are retained agent definitions. A configured installation can apply them to admitted observations and its own participant, input and spending permissions.

The hosted read-only dashboard and the local starter use the same retained 45-recording sample. Fresh CCTV acquisition, Cosmos processing and delivered alerts use owned infrastructure and their own acceptance checks. The alert definitions are inactive drafts in the sample.

## Product areas

| Area | What you do | Result |
| --- | --- | --- |
| Home | See the location’s business metrics and their historical period. | A useful summary opens the detailed tracker behind it. |
| Nine retail trackers | Inspect Visitors, Product interactions, Picked up, Put back, Basket, Queue time, Empty shelves, Sales and Conversion. | Each maintained processor declares its source requirements and calculation. |
| Camera and visitor review | Play a source recording and inspect an event or tracked visit. | Observations retain their recording interval and camera-local identity. |
| Cosmos processing | Prepare recordings, index bounded windows and inspect selected clips. | A model output retains source, model and processing provenance. |
| Evidence admission | Check source clocks, profiles, tracker labels and provenance. | Only admitted records enter the maintained business calculations. |
| Agents and alerts | Configure a queue watch, shelf watch or periodic shop summary. | A configured runtime can report or notify from the admitted event stream. |

## Design decisions

- **A metric needs a source.** A tracker links to evidence rather than leaving a business number detached from the footage.
- **Generation and counting have different jobs.** Cosmos proposes observations. Admission checks them, and deterministic processors calculate the maintained tracker outputs.
- **Search narrows expensive inspection.** H100 Cosmos Embed indexing, a CPU text tower and filtered Qdrant retrieval locate intervals before detailed model inspection.
- **Business meaning remains explicit.** Basket-derived sales are estimates; committed till rows have a transaction basis. Recording-local person labels keep their camera scope.

## Reached stage

The preview runs the retained retail application and footage. Model candidates stay in their recorded admission state; publisher-reference events and generated business history keep their own labels. Fresh cameras, processing, POS inputs and delivered alerts need your own configuration and acceptance tests. [Implementation and trial evidence](implementation.md) preserves the executed runs, exact counts and source licences.

## Modules

| Source | Responsibility |
| --- | --- |
| [Intake and worker](../harness/verticals/retail/source_intake.py) | Retain immutable source versions; the separate worker prepares and publishes verified index generations. |
| [Cosmos retrieval](../harness/verticals/retail/cosmos_retrieval.py) | Keep bounded windows, the pinned embedding space and generation identity. |
| [Persistent vector index](../harness/verticals/retail/qdrant_retrieval.py) | Retrieve within tenant, source and model filters. |
| [Detailed inspection](../harness/verticals/retail/cosmos_inspect.py) | Inspect selected clips with bounded funded model work and cached evidence. |
| [Observation admission](../harness/verticals/retail/stream_ingestion.py) | Validate observation profile, clock, interval and tracker labels. |
| [Core trackers](../harness/verticals/retail/core_trackers/retail.json) | Declare the nine trackers and the inputs each needs. |
| [Dashboard and player](../harness/verticals/retail/web/control-room/) | Present tiles, histories, source playback and visitor chapters. |
| [Ready agents](../harness/verticals/retail/ready_agents.json) | Define queue, shelf and shop-summary jobs for an admitted runtime. |

## Setup and implementation

[Getting started](get-started.md) · [Sample and licences](processed-sample.md) · [Setup](video-setup.md) · [Architecture](video-architecture.md) · [Design decisions](video-design.md) · [Workflows](workflows.md) · [Function reference](video-reference.md) · [Trial status](video-status.md) · [Agent skill](../.agents/skills/video-operations-setup/SKILL.md) · [Implementation and retained evidence](implementation.md)

[made by atelier neyra](https://atelierneyra.com)
