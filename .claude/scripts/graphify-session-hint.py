"""Add one Graphify hint at session start when a usable existing graph is present."""
import json
from pathlib import Path
import shutil
import sys

def main():
    try:
        event = json.load(sys.stdin)
        cwd = Path(event.get("cwd") or ".")
        if not (cwd / "graphify-out/graph.json").is_file() or not shutil.which("graphify"):
            return
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "Existing Graphify graph: use scoped query/path/explain for architectural relationships; rg for direct text lookup, and source inspection for edits. Follow the shared global rules."
        }}))
    except (ValueError, TypeError, AttributeError, OSError):
        return

if __name__ == "__main__":
    main()
