from agents.orchestrator.orchestrator import Orchestrator


def test_reel_request_includes_video_role() -> None:
    plan = Orchestrator().create_plan("Сделай Reel про ВПР для начинающих")

    assert plan["status"] == "draft"
    assert plan["agent"] == "orchestrator"
    assert "video" in plan["suggested_roles"]
