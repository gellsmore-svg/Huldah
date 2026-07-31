# Changelog

## [0.1.0] - 2026-07-31
Initial release — extracted from `cairn-lang` v0.8.2 as the human-systems
analysis half of the Cairn split (see `Noa/docs/cairn-split-and-rename.md`).

- Modules: `human_factors`, `ui_evidence`, `ui_scenarios`, `layout_load`,
  `interface_recommendations`, `live_observer`, `system_discovery`, `reporting`,
  `agent_harness`, `observation_contract`, `galeed_adapter`, `llm_wrappers`,
  `llm_adapters`, and their 14 console scripts (`cairn-*` → `huldah-*`).
- Own Keturah manifest advertising the six analysis capabilities, split out of
  the fused `cairn` manifest so each package advertises only what it can execute.
- Depends on `deborah>=0.9` for the language; `huldah[export]` defers to
  `deborah[export]` for docx/pdf.
- Behaviour is unchanged from v0.8.2: all 77 analysis tests moved across and pass.
  Hoglah task ids move namespace (`cairn.human_factors.interpret` →
  `huldah.human_factors.interpret`).
