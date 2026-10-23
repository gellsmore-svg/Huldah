# Huldah

**Huldah reads a process, or evidence of how people actually use a system,
and points out where the human burden is.** It flags where people must switch
context, carry uncertainty, rubber-stamp an AI suggestion or work against
their incentives. For each finding it gives a mitigation and the questions to
ask the people who do the work.

It is the analysis half of the former `cairn` package;
[Deborah](https://github.com/gellsmore-svg/Deborah) is the language half.
Huldah reads the same `.cairn.md` process documents. *(Huldah was a
prophetess who interpreted and authenticated a text, 2 Kings 22.)*

## Is it for you?

**Good fit:** you are designing or reviewing a business process, AI-assisted
workflow or UI, and want a structured first pass on human load before you
talk to users. The pass runs offline in seconds, with no model needed.

**Not a fit:** you want a finding you can treat as validated. The offline
analysis matches cues in the text and estimates risk. It starts the
conversation with real users; it does not replace it.

## Try it

```bash
pip install huldah
huldah-human-factors my-process.cairn.md         # add -f json for machine output
```

Run against Deborah's
[accounts-payable example](https://github.com/gellsmore-svg/Deborah/blob/main/examples/accounts-payable-exception.cairn.md),
each step gets findings like these:

```
## 3. Review the AI-generated exception summary and source evidence.
- trust_automation: automation bias - Matched cues in step 3: ai summary, ai recommendation, ...
  Mitigation: expose evidence, uncertainty, and disagreement separately from the AI suggestion.
- cognitive_load: uncertainty load - Matched cues in step 3: missing evidence, ...
  Mitigation: show what is known, unknown, and disputed before asking for judgement.
**Risk:** significant (probability: high; impact: medium; confidence: medium)
Rationale: Estimated from offline human-factor cues; confirm with domain users before treating as authoritative.
```

To add an LLM's interpretation on top, use `--llm-command "my-llm-wrapper"`
(any command) or `--hoglah-model gemma3:1b` (queued via
[Hoglah](https://github.com/gellsmore-svg/hoglah)).

From Python:

```python
from huldah import analyze_human_factors, format_human_factors_report

print(format_human_factors_report(analyze_human_factors(open("my-process.cairn.md").read())))
```

## What else it analyses

| Question | Command | Input |
|---|---|---|
| Where is the human load in this process? | `huldah-human-factors` | a `.cairn.md` process |
| How much interface overhead sits between a person and the work? | `huldah-layout-load` | UI geometry JSON |
| What does using the real UI feel like? | `huldah-ui-sim` (Playwright) → `huldah-ui-evidence` → `huldah-ui-annotations`; or all at once with `huldah-ui-pipeline` | a UI simulation scenario |
| How might a user experience it? | `huldah-ui-roleplay` (LLM role-play) | a `huldah-ui-sim` report |
| What should change in the interface? | `huldah-recommend-interface-changes` | UI evidence |
| What is happening in a running system? | `huldah-system-discover` → `huldah-live-observe`, or `huldah-galeed-observe` | a live stack, or Galeed exports |
| What should an agent run to gather the evidence? | `huldah-agent-harness-plan` (plans only, runs nothing) | process + UI evidence |
| One report of all of it | `huldah-generate-report --format html` | any of the above |

UI evidence and observations come back as Cairn annotation blocks you can
paste into the process document, so findings stay attached to the steps they
concern. `huldah-ui-sim` needs Node.js with Playwright installed.

## How to read the results

- **Findings are cue-based estimates.** Each one names the cues it matched,
  so you can see why it fired and dismiss it if the cue is misleading.
- **Risk ratings carry a confidence.** Treat them as a priority order for
  user conversations, not as measurements.
- The method behind each category is in
  [HUMAN-FACTORS-METHODOLOGY.md](docs/HUMAN-FACTORS-METHODOLOGY.md); see also
  [FUNCTIONAL-LAYOUT-LOAD.md](docs/FUNCTIONAL-LAYOUT-LOAD.md),
  [UI-SIMULATION.md](docs/UI-SIMULATION.md) and
  [HCI-TOUCHPOINTS.md](docs/HCI-TOUCHPOINTS.md).

## With Deborah and the family

- Huldah depends on Deborah and reads the same documents. **The format keeps
  the Cairn name**: `.cairn.md` files and ```cairn fences are unchanged. Coming
  from `cairn`? See
  [MIGRATING.md](https://github.com/gellsmore-svg/Deborah/blob/main/MIGRATING.md).
- docx and pdf export use Deborah's render layer: `pip install 'huldah[export]'`.
- Huldah publishes a [Keturah](https://github.com/gellsmore-svg/keturah)
  manifest of the six analyses it can execute, so MCP clients see only
  callable tools.

[CHANGELOG](CHANGELOG.md) · Apache 2.0, see [LICENSE](LICENSE).
