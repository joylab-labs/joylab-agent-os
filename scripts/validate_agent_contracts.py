#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def validate(schema_path, files):
    schema = load(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    failed = False
    for filename in files:
        data = load(filename)
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
        if errors:
            failed = True
            print(f"BLOCKED {filename}")
            for error in errors:
                where = ".".join(str(p) for p in error.absolute_path) or "<root>"
                print(f"  - {where}: {error.message}")
        else:
            print(f"PASS {filename}")
    return 1 if failed else 0

def main():
    p = argparse.ArgumentParser()
    kind = p.add_mutually_exclusive_group()
    kind.add_argument("--failure", action="store_true")
    kind.add_argument("--evidence", action="store_true")
    p.add_argument("files", nargs="+")
    args = p.parse_args()
    if args.failure:
        schema_name = "failure_packet.schema.json"
    elif args.evidence:
        schema_name = "evidence_contract.schema.json"
    else:
        schema_name = "agent_contract.schema.json"
    raise SystemExit(validate(ROOT / "schemas" / schema_name, args.files))

if __name__ == "__main__":
    main()
