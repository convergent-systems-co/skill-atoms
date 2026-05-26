#!/usr/bin/env python3
"""Validate every skill atom against schemas/atom-v1.json.

Per-file checks:
  skills/skill/<id>.json  → atom-v1.json
                            id field must match "skill/<filename-stem>"
                            type field must be "skill"

Exit 0 on full pass; exit 1 on any failure.
"""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("error: jsonschema not installed. Run: pip install jsonschema", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "schemas" / "atom-v1.json"
SKILLS_DIR = REPO / "skills" / "skill"


def load_validator() -> jsonschema.Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    return jsonschema.Draft202012Validator(schema)


def validate_atoms(validator) -> int:
    errors = 0
    paths = sorted(p for p in SKILLS_DIR.glob("*.json") if p.name != ".gitkeep")
    for path in paths:
        rel = path.relative_to(REPO)
        local_errors = _validate_one(path, rel, validator)
        if local_errors == 0:
            print(f"✓ {rel}")
        errors += local_errors
    return errors


def _validate_one(path: Path, rel: Path, validator) -> int:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"✗ {rel}: invalid JSON ({e})")
        return 1

    schema_errors = list(validator.iter_errors(data))
    if schema_errors:
        print(f"✗ {rel}")
        for err in schema_errors:
            loc = "/".join(str(x) for x in err.absolute_path) or "<root>"
            print(f"    schema: {err.message} at {loc}")
        return len(schema_errors)

    # id must be "skill/<filename-stem>"
    expected_id = f"skill/{path.stem}"
    if data.get("id") != expected_id:
        print(f"✗ {rel}")
        print(f"    id={data.get('id')!r} does not match expected {expected_id!r}")
        return 1

    # type must match parent dir name
    parent = path.parent.name
    if data.get("type") != parent:
        print(f"✗ {rel}")
        print(f"    type={data.get('type')!r} does not match parent dir {parent!r}")
        return 1

    return 0


def main() -> int:
    if not SCHEMA_PATH.exists():
        print(f"missing schema: {SCHEMA_PATH}", file=sys.stderr)
        return 1

    if not SKILLS_DIR.exists():
        print(f"missing skills directory: {SKILLS_DIR}", file=sys.stderr)
        return 1

    validator = load_validator()
    total = validate_atoms(validator)

    if total:
        print(f"\n{total} error(s)")
        return 1
    print(f"\nall valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
