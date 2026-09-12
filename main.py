"""Command-line entry point for the AI Instagram team."""

from __future__ import annotations

import json
import sys

from agents.orchestrator.orchestrator import Orchestrator


def main() -> None:
    request = " ".join(sys.argv[1:]).strip()
    if not request:
        print('Usage: python main.py "Create a Reel about VPR for beginners"')
        raise SystemExit(1)

    plan = Orchestrator().create_plan(request)
    print(json.dumps(plan, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
