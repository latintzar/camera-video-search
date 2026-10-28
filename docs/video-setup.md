# Setup

## CPU first result

`make install` installs the pinned CPU development environment. `make dev` creates a recipient-owned sample workspace and runs the original interface over its saved records. The included video and poster are already rendered. FFmpeg and ffprobe support optional source preparation and fixture regeneration.

## Recipient credentials

```sh
.venv/bin/python tools/configure.py init --features openai
.venv/bin/python tools/configure.py doctor --features openai
```

The helper uses hidden input and writes `~/.config/video-operations/runtime.env` with mode 0600 in an owner-only directory. It prints configuration names and paths. State, recordings, keys and provider configuration belong outside the checkout.

| Feature | Configuration | Runtime boundary |
| --- | --- | --- |
| OpenAI agents | `ROCOTO_OPENAI_API_KEY`, `ROCOTO_PUBLIC_ORIGIN`, `ROCOTO_OPERATOR_ID`, explicit spending mode | Managed Agents API, hosted execution, reachable scoped MCP callback, funded allowance |
| Modal GPU | `VIDEO_OPERATIONS_MODAL_WORKSPACE`, `ROCOTO_RETAIL_MODAL_PYTHON`, `ROCOTO_RETAIL_MODAL_CONFIG_PATH`, `ROCOTO_OPERATOR_ID` | Recipient workspace/account, model terms, owner-attested cap/credit record and one-use compute admission |
| Persistent index | `ROCOTO_RETAIL_QDRANT_URL` | Own loopback Qdrant service and verified generation |
| Maintained reader | `RUNTIME_DATABASE_URL`, `ROCOTO_RETAIL_REALTIME_READS` | Original migrations/SDK, exact runtime role and tenant/principal RLS |
| Maps/weather | Retail location-context switch and recipient Mapbox/Google credentials | Explicit provider commissioning and ledger |
| Intake/custom execution | Source-media/storage/executor service configuration and readiness receipts | Separate owned brokers/workers and bounded sandbox |

The retained Modal pilot compares its operator identity with an owner email returned by that Modal workspace. Configure your own billing identity; its historical workspace default has been removed. An empty workspace is rejected before compute admission. Existing cap, credit, ownership and reservation checks remain active.

## Connected workspace

Follow [OpenAI setup](OPENAI-SETUP.md) for actual permissions, public MCP origin, allowance and provider spending mode. Its environment names and managed namespace remain compatible with the original framework.

```sh
.venv/bin/python tools/serve.py --state "$HOME/.local/state/video-connected"   --env-file "$HOME/.config/video-operations/runtime.env"
```

The command saves a private one-use owner code in that state directory, selects recipient configuration and starts the original connected host. Its optional workers and providers still require their own setup. The local fixture server remains the verified provider-free starting point.

## Index and model requirements

The pinned Qdrant Compose file selects a separate project, volume and loopback port for this release. It is an optional service recipe, independently of GPU commissioning. The release has offline transport/generation tests; a fresh Docker/Qdrant/GPU service acceptance is separate.

Cosmos Embed uses the pinned `nvidia/Cosmos-Embed1-224p` revision in `modal_embed.py`, eight sampled frames per short window and a 256-dimensional space. The source prepares short windows before admission. Detailed inspection uses the separate Cosmos configuration in `cosmos_inspect.py`. Download weights through your own provider/model access and accept their actual model terms. The optional GPU install owns Cosmos packages and checkpoints.

## Database and storage

Workspace SQLite/file schemas are created by their owning modules. The optional PostgreSQL reader retains its original migration closure under `backend/migrations`; it is separate from this SQLite first result. Apply only the selected maintained runtime's documented migrations and role grants to a fresh owned database. Source media, Qdrant generations, model caches and custom-executor artifacts have separate private storage roots and source identities.

[made by atelier neyra](https://atelierneyra.com)
