"""Huldah — human-systems analysis over Deborah process descriptions.

Where Deborah defines and validates the process *language*, Huldah interprets
evidence about how a system is actually used: human-factors load, UI simulation
and role-play evidence, functional layout load, live observation of a running
stack, interface recommendations, and the agent harness that drives them.

*Huldah was a prophetess who interpreted and authenticated a text* — the analysis
half of what used to be a single `cairn` package.

The Cairn document format keeps its name: Huldah still reads and writes
`.cairn.md` sources and Cairn annotation blocks. Only the packages were renamed.
"""

from importlib.metadata import PackageNotFoundError, version as _pkg_version

from huldah.agent_harness import (
    AgentHarnessPlan,
    AgentHarnessStep,
    build_agent_harness_plan,
    format_agent_harness_plan,
)
from huldah.galeed_adapter import galeed_event_to_observation, galeed_llm_call_to_observation
from huldah.human_factors import (
    analyze_human_factors,
    build_human_factors_prompt,
    format_human_factors_report,
    interpret_human_factors,
)
from huldah.interface_recommendations import (
    format_interface_recommendations,
    future_state_svg,
    recommend_interface_changes,
)
from huldah.layout_load import (
    analyze_functional_layout,
    format_functional_layout_report,
    render_layout_svg,
)
from huldah.live_observer import analyze_live_observations, format_live_observation_report
from huldah.llm_adapters import CommandLLMProvider, HoglahLLMProvider, LLMRequest, LLMResponse
from huldah.llm_wrappers import (
    HostedLLMConfig,
    HostedLLMProvider,
    claude_provider,
    gemini_provider,
    grok_provider,
    openai_provider,
)
from huldah.observation_contract import observation_event, observation_to_galeed_trace_event
from huldah.reporting import build_analysis_report, format_analysis_report
from huldah.system_discovery import discover_system, format_system_discovery_report
from huldah.ui_evidence import (
    analyze_ui_simulation_report,
    build_ui_roleplay_prompt,
    format_cairn_annotation_snippet,
    format_ui_human_load_report,
    format_ui_layout_overlay_index,
    format_ui_layout_overlay_manifest,
    interpret_ui_experience,
    render_ui_layout_overlay,
    render_ui_layout_overlays,
)
from huldah.ui_scenarios import format_scenario_validation_report, validate_ui_scenario

try:
    # Single source of truth: read the installed distribution rather than
    # restating the version here, so it cannot drift from pyproject.
    __version__ = _pkg_version("huldah")
except PackageNotFoundError:  # running straight from a source checkout
    __version__ = "0.0.0+source"

__all__ = [
    "AgentHarnessPlan",
    "AgentHarnessStep",
    "CommandLLMProvider",
    "HoglahLLMProvider",
    "HostedLLMConfig",
    "HostedLLMProvider",
    "LLMRequest",
    "LLMResponse",
    "analyze_functional_layout",
    "analyze_human_factors",
    "analyze_live_observations",
    "analyze_ui_simulation_report",
    "build_agent_harness_plan",
    "build_analysis_report",
    "build_human_factors_prompt",
    "build_ui_roleplay_prompt",
    "claude_provider",
    "discover_system",
    "format_agent_harness_plan",
    "format_analysis_report",
    "format_cairn_annotation_snippet",
    "format_functional_layout_report",
    "format_human_factors_report",
    "format_interface_recommendations",
    "format_live_observation_report",
    "format_scenario_validation_report",
    "format_system_discovery_report",
    "format_ui_human_load_report",
    "format_ui_layout_overlay_index",
    "format_ui_layout_overlay_manifest",
    "future_state_svg",
    "galeed_event_to_observation",
    "galeed_llm_call_to_observation",
    "gemini_provider",
    "grok_provider",
    "interpret_human_factors",
    "interpret_ui_experience",
    "observation_event",
    "observation_to_galeed_trace_event",
    "openai_provider",
    "recommend_interface_changes",
    "render_layout_svg",
    "render_ui_layout_overlay",
    "render_ui_layout_overlays",
    "validate_ui_scenario",
]
