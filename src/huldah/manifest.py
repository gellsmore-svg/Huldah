"""Huldah's Keturah manifest — its LLM-consumable analysis interfaces.

Split out of the single `cairn` manifest: Deborah advertises the language
(validate/render/parse + the plan schema), Huldah advertises the analysis
tools. Each package now advertises only what it can actually execute.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from importlib.metadata import PackageNotFoundError, version as _pkg_version
from typing import Any

try:
    from keturah import Manifest, capability, manifest
except ImportError:

    @dataclass
    class _Capability:
        name: str
        description: str
        input_schema: dict[str, Any] | None = None
        output_schema: dict[str, Any] | None = None
        tags: list[str] = field(default_factory=list)
        kind: str = "tool"

    @dataclass
    class Manifest:
        product: str
        version: str
        description: str
        capabilities: list[_Capability]

        def to_mcp(self) -> dict[str, Any]:
            tools = []
            for item in self.capabilities:
                if item.kind == "resource":
                    continue
                tools.append(
                    {
                        "name": item.name,
                        "description": item.description,
                        "inputSchema": item.input_schema or {"type": "object"},
                    }
                )
            return {"tools": tools}

    def capability(
        name: str,
        description: str,
        *,
        input_schema: dict[str, Any] | None = None,
        output_schema: dict[str, Any] | None = None,
        tags: list[str] | None = None,
        kind: str = "tool",
    ) -> _Capability:
        return _Capability(
            name=name,
            description=description,
            input_schema=input_schema,
            output_schema=output_schema,
            tags=tags or [],
            kind=kind,
        )

    def manifest(product: str, *, version: str, description: str, capabilities: list[_Capability]) -> Manifest:
        return Manifest(product=product, version=version, description=description, capabilities=capabilities)


def _version() -> str:
    for distribution in ("huldah",):
        try:
            return _pkg_version(distribution)
        except PackageNotFoundError:
            continue
    return "0.0.0+source"


def build_manifest() -> Manifest:
    return manifest(
        "huldah",
        version=_version(),
        description="Human-systems analysis over Deborah process descriptions: human factors, UI evidence, layout load, and interface recommendations.",
        capabilities=[
            capability(
                "analyze_human_factors",
                "Offline analysis of a Cairn document for plausible cognitive, psychological, social, "
                "organisational, behavioural-economic, and incentive factors. Returns qualitative risk "
                "estimates and conversation starters; does not require an LLM service.",
                input_schema={
                    "type": "object",
                    "properties": {"input_cairn": {"description": "Cairn markdown text or PLAN object"}},
                    "required": ["input_cairn"],
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "steps": {"type": "array"},
                        "warnings": {"type": "array", "items": {"type": "string"}},
                    },
                },
                tags=["human-factors", "analysis", "offline"],
            ),
            capability(
                "analyze_ui_simulation_report",
                "Summarise a cairn-ui-sim JSON report as deterministic human-load evidence, including "
                "HCI phases, human systems, qualitative risk, suggested Cairn blocks, and measured "
                "functional layout load snapshots when present.",
                input_schema={
                    "type": "object",
                    "properties": {"report": {"type": "object", "description": "cairn-ui-sim JSON report"}},
                    "required": ["report"],
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "scenario": {"type": "string"},
                        "metrics": {"type": "object"},
                        "findings": {"type": "array"},
                        "suggested_blocks": {"type": "object"},
                    },
                },
                tags=["ui", "human-load", "hci", "analysis", "offline"],
            ),
            capability(
                "analyze_functional_layout",
                "Analyse UI layout geometry for cognitive and motor traversal load using element "
                "rectangles, relationships, and task sequence. Supports label distance, "
                "evidence-to-action distance, scan path, pointer travel, findings, and mitigations.",
                input_schema={
                    "type": "object",
                    "properties": {
                        "layout": {
                            "type": "object",
                            "description": "Layout JSON with viewport, elements, relations, and sequence",
                        }
                    },
                    "required": ["layout"],
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "metrics": {"type": "object"},
                        "findings": {"type": "array"},
                        "suggested_blocks": {"type": "object"},
                    },
                },
                tags=["ui", "layout", "human-load", "analysis", "offline"],
            ),
            capability(
                "recommend_interface_changes",
                "Generate deterministic interface change recommendations from UI evidence. Every "
                "recommendation includes OKF traceability, rationale, priority, effort, current "
                "state, and proposed future state.",
                input_schema={
                    "type": "object",
                    "properties": {"evidence": {"type": "object", "description": "UI simulation report or layout JSON"}},
                    "required": ["evidence"],
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "recommendations": {"type": "array"},
                        "references": {"type": "array"},
                    },
                },
                tags=["ui", "recommendations", "okf", "traceability"],
            ),
            capability(
                "build_analysis_report",
                "Assemble a structured Cairn analysis report from process text and/or UI evidence, "
                "including human factors, augmentation findings, traceable interface recommendations, "
                "and references. Can be exported as Markdown, HTML, JSON, or PDF through the CLI.",
                input_schema={
                    "type": "object",
                    "properties": {
                        "input_cairn": {"type": "string"},
                        "interface_evidence": {"type": "object"},
                    },
                },
                output_schema={"type": "object", "properties": {"title": {"type": "string"}}},
                tags=["report", "ui", "human-factors", "okf"],
            ),
            capability(
                "build_agent_harness_plan",
                "Plan deterministic Cairn CLI/API steps for an interactive agent harness based on "
                "available process, UI evidence, and layout artifacts. Returns commands to run and "
                "open questions for missing evidence; it does not execute the commands.",
                input_schema={
                    "type": "object",
                    "properties": {
                        "process_path": {"type": "string"},
                        "ui_evidence_path": {"type": "string"},
                        "layout_path": {"type": "string"},
                        "repository_path": {"type": "string"},
                        "screenshot_paths": {"type": "array", "items": {"type": "string"}},
                        "output_dir": {"type": "string"},
                        "check_paths": {"type": "boolean"},
                    },
                },
                output_schema={
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "inputs": {"type": "object"},
                        "missing_inputs": {"type": "array"},
                        "steps": {"type": "array"},
                        "open_questions": {"type": "array"},
                    },
                },
                tags=["agent", "orchestration", "harness", "offline"],
            ),
        ],
    )
