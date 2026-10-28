# Workflows

## Recording to a searchable interval

The intake creates an immutable source version. The worker prepares bounded windows, obtains embeddings and verifies a new index generation before publishing Ready. A stopped or interrupted publication keeps the previous visible generation.

Sources: [intake](../harness/verticals/retail/source_intake.py), [worker](../harness/verticals/retail/source_worker.py), [embedding](../harness/verticals/retail/source_embedding.py), [Qdrant](../harness/verticals/retail/qdrant_retrieval.py), [visibility](../harness/verticals/retail/source_visibility.py).

## Search and inspection

The CPU text tower embeds a query in the pinned Cosmos space. Retrieval narrows by tenant, model and current source/clip scope. Selected-clip inspection uses a separate model and funded admission, with cached results and source/derivative hashes.

Sources: [retrieval](../harness/verticals/retail/cosmos_retrieval.py), [inspection](../harness/verticals/retail/cosmos_inspect.py), [query budget](../harness/verticals/retail/query_budget.py), [evidence](../harness/verticals/retail/evidence_presentation.py).

## Observation to a tracker

An observation supplies its saved profile revision, source interval, tracker label and provenance. Admission validates that contract before projection. Deterministic processors then publish one revision containing the compact tile and its detailed canvas.

The included fixture runs this same path with explicitly supplied annotations. It produces one visitor, three interactions, one pickup and one return. Queue, shelf and till-dependent measures name their missing inputs in the interface.

Sources: [admission](../harness/verticals/retail/stream_ingestion.py), [records](../harness/verticals/retail/retail_records.py), [tracker recipe](../harness/verticals/retail/core_trackers/retail.json), [runner](../harness/verticals/retail/tracker_runner.py), [publication](../harness/verticals/retail/import_control_room_bundle.py).

## Tracker to source evidence

Open a native tracker canvas, select an occurrence or visitor, then seek its recording. Playback retains the exact source interval and camera-local path. The source-scoped bundle and the maintained reader have separate, explicit read authorities.

Sources: [native player](../harness/verticals/retail/web/control-room/app.js), [Home](../harness/verticals/retail/web/control-room/location-view.js), [media authority](../harness/verticals/retail/playback_media.py).

## Recurring agents

Queue watch, Empty shelf watch and Shop summary are saved inactive drafts. Activation requires current input coverage, participant reach, budget and provider readiness. Live phone delivery additionally requires the commissioned live-observation lane.

Sources: [ready agents](../harness/verticals/retail/ready_agents.json), [retail host](../harness/verticals/retail/retail_host.py), [background jobs](../harness/mechanics/background_agents.py), [signal chain](../harness/mechanics/signal_chain.py).

[made by atelier neyra](https://atelierneyra.com)
