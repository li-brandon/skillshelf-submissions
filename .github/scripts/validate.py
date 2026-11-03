#!/usr/bin/env python3
"""Validate SkillShelf submission files.

Checks every submissions/*.md (except _TEMPLATE.md) for:
  - YAML front matter with non-empty required fields
  - a valid YYYY-MM-DD lastTested date
  - a non-empty "## Skill text" section
"""

import datetime
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
SUBMISSIONS_DIR = REPO_ROOT / "submissions"
TEMPLATE_NAME = "_TEMPLATE.md"

REQUIRED_FIELDS = [
    "name",
    "slug",
    "description",
    "connectors",
    "license",
    "source",
    "author",
    "lastTested",
]

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)(.*)\Z", re.DOTALL)
SKILL_TEXT_RE = re.compile(r"^##\s+Skill text\s*$", re.MULTILINE | re.IGNORECASE)
NEXT_H2_RE = re.compile(r"^##\s+", re.MULTILINE)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def is_empty(value):
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, dict)):
        return len(value) == 0
    return False


def check_last_tested(value):
    # PyYAML parses unquoted YYYY-MM-DD as a date; quoted values stay strings.
    if isinstance(value, datetime.datetime):
        return "lastTested must be a date (YYYY-MM-DD), not a timestamp"
    if isinstance(value, datetime.date):
        return None
    text = str(value).strip()
    if not DATE_RE.match(text):
        return f"lastTested must be in YYYY-MM-DD format (got {text!r})"
    try:
        datetime.date.fromisoformat(text)
    except ValueError:
        return f"lastTested is not a valid calendar date (got {text!r})"
    return None


def check_connectors(value):
    if not isinstance(value, list):
        return "connectors must be a YAML list"
    if any(is_empty(item) for item in value):
        return "connectors must not contain empty entries"
    return None


def extract_skill_text(body):
    match = SKILL_TEXT_RE.search(body)
    if not match:
        return None
    rest = body[match.end():]
    next_heading = NEXT_H2_RE.search(rest)
    if next_heading:
        rest = rest[: next_heading.start()]
    return rest.strip()


def validate_file(path):
    errors = []
    text = path.read_text(encoding="utf-8")

    match = FRONT_MATTER_RE.match(text)
    if not match:
        return ["missing YAML front matter (file must start with '---' and close with '---')"]

    raw_front_matter, body = match.groups()
    try:
        data = yaml.safe_load(raw_front_matter)
    except yaml.YAMLError as exc:
        return [f"invalid YAML front matter: {exc}"]
    except ValueError as exc:
        # PyYAML raises ValueError for date-shaped values that are not real
        # dates, e.g. an unquoted lastTested: 2026-02-30.
        return [f"invalid value in front matter (check lastTested is a real date): {exc}"]

    if not isinstance(data, dict):
        return ["front matter must be a YAML mapping of fields"]

    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"missing required field '{field}'")
        elif is_empty(data[field]):
            errors.append(f"field '{field}' must not be empty")

    if "slug" in data and not is_empty(data["slug"]) and str(data["slug"]) != path.stem:
        errors.append(f"slug '{data['slug']}' must match the file name '{path.stem}'")

    if "connectors" in data and not is_empty(data["connectors"]):
        error = check_connectors(data["connectors"])
        if error:
            errors.append(error)

    if "lastTested" in data and not is_empty(data["lastTested"]):
        error = check_last_tested(data["lastTested"])
        if error:
            errors.append(error)

    skill_text = extract_skill_text(body)
    if skill_text is None:
        errors.append("missing '## Skill text' section")
    elif not skill_text:
        errors.append("'## Skill text' section must not be empty")

    return errors


def main():
    if not SUBMISSIONS_DIR.is_dir():
        print(f"error: {SUBMISSIONS_DIR} does not exist")
        return 1

    files = sorted(p for p in SUBMISSIONS_DIR.glob("*.md") if p.name != TEMPLATE_NAME)
    if not files:
        print("No submissions to validate.")
        return 0

    failed = 0
    for path in files:
        rel = path.relative_to(REPO_ROOT)
        errors = validate_file(path)
        if errors:
            failed += 1
            print(f"FAIL {rel}")
            for error in errors:
                print(f"  - {error}")
                # GitHub Actions annotation so errors show inline on the PR.
                print(f"::error file={rel}::{error}")
        else:
            print(f"ok   {rel}")

    print()
    print(f"{len(files) - failed}/{len(files)} submission(s) passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
