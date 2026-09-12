"""A small, deterministic foundation for the future Orchestrator."""

from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class TaskPlan:
    status: str
    agent: str
    request: str
    goal: str
    suggested_roles: list[str]
    next_step: str


class Orchestrator:
    """Converts a free-text request into a stable task contract.

    Intent recognition and external calls will be added only after this
    contract is agreed and covered by tests.
    """

    def create_plan(self, request: str) -> dict[str, object]:
        normalized_request = request.strip()
        if not normalized_request:
            raise ValueError("A request cannot be empty.")

        roles = ["research", "strategy", "content", "quality"]
        lower_request = normalized_request.lower()
        if any(word in lower_request for word in ("reel", "рилс", "video", "видео")):
            roles.append("video")
        if any(word in lower_request for word in ("table", "таблица", "excel", "контент-план")):
            roles.append("excel")
        if any(word in lower_request for word in ("visual", "визуал", "design", "дизайн")):
            roles.append("visual")

        plan = TaskPlan(
            status="draft",
            agent="orchestrator",
            request=normalized_request,
            goal="Prepare an approved Instagram content task",
            suggested_roles=roles,
            next_step="Confirm the brief, then send it to the first selected role.",
        )
        return asdict(plan)
