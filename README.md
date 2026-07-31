# Huldah

Huldah is the **human-systems analysis** half of what used to be the `cairn`
package. Where [Deborah](https://github.com/gellsmore-svg/Deborah) defines and
validates the process *language*, Huldah interprets evidence about how a system
is actually used.

*Huldah was a prophetess who interpreted and authenticated a text.*

```bash
pip install huldah
```

## What it does

- **Human factors** — offline analysis of a process document for plausible
  cognitive, psychological, social, organisational, behavioural-economic and
  incentive load. Qualitative risk estimates and conversation starters; no LLM
  required, with optional LLM interpretation on top.
- **UI evidence** — turn a UI simulation report into human-load evidence, layout
  overlays, and Cairn annotation blocks you can paste back into the process.
- **Functional layout load** — how much interface overhead sits between a person
  and the business work.
- **Live observation** — watch a running stack and turn traces into reviewable
  observations (bridges Galeed trace events).
- **Interface recommendations** — traceable current→future state suggestions.
- **Agent harness** — plan deterministic CLI steps for an interactive agent to
  run, plus the open questions it should ask. It plans; it does not execute.

## Quickstart

```bash
# offline human-factors analysis of a process document
huldah-human-factors my-process.cairn.md
huldah-human-factors my-process.cairn.md -f json

# UI evidence -> human load, overlays, annotations
huldah-ui-evidence ui-sim-report.json --format markdown
huldah-ui-annotations ui-sim-report.json -o ui-annotations.cairn.md

# traceable interface recommendations and a combined report
huldah-recommend-interface-changes ui-evidence.json --future-svg-output future.svg
huldah-generate-report --input my-process.cairn.md \
  --interface-evidence ui-evidence.json --format html --output report.html

# plan an agent harness run (emits commands + open questions, runs nothing)
huldah-agent-harness-plan --process my-process.cairn.md \
  --ui-evidence ui-evidence.json --repo . --check-files

# optional LLM interpretation through any command provider, or queued via Hoglah
huldah-human-factors my-process.cairn.md --llm-command "my-llm-wrapper --model local"
huldah-human-factors my-process.cairn.md --hoglah-model gemma3:1b
```

Or programmatically:

```python
from huldah import analyze_human_factors, format_human_factors_report

report = analyze_human_factors(open("my-process.cairn.md").read())
print(format_human_factors_report(report))
```

## Relationship to Deborah

Huldah depends on Deborah and reads the same documents. **The document format
keeps the Cairn name** — `.cairn.md` files and ```` ```cairn ```` fences are
unchanged; only the Python packages were renamed. See
[MIGRATING.md](https://github.com/gellsmore-svg/Deborah/blob/main/MIGRATING.md)
if you are coming from `cairn`.

The docx/pdf exporters live in Deborah's render layer, so `huldah[export]`
defers to `deborah[export]` rather than duplicating the dependency.

## Manifest

Huldah advertises its own Keturah manifest — `analyze_human_factors`,
`analyze_ui_simulation_report`, `analyze_functional_layout`,
`recommend_interface_changes`, `build_analysis_report`,
`build_agent_harness_plan` — so an MCP consumer only sees tools this package can
actually execute.

## Licence

Apache-2.0.
