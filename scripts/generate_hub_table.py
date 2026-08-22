#!/usr/bin/env python3
"""Generate the CloudBank campus hub table from 2i2c's cluster configuration.

CloudBank's hubs are hosted by 2i2c, whose public infrastructure repo is the
source of truth for which campuses have a hub and what its domain is. This
script reads that config and writes a Markdown fragment that
getting-started/hub-url.md includes.

The script never fails the docs build. It depends on a path inside a third
party repo that carries no compatibility promise, so any fetch, parse, or
schema error leaves the previous table in place (or writes a fallback that
points readers at 2i2c) and exits 0.

Run it before building:

    python scripts/generate_hub_table.py
"""

import datetime
import pathlib
import re
import sys
import urllib.request

import yaml

SOURCE = (
    "https://raw.githubusercontent.com/2i2c-org/infrastructure/main"
    "/config/clusters/cloudbank/cluster.yaml"
)
SOURCE_HUMAN = "https://infrastructure.2i2c.org/reference/hubs/"

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO_ROOT / "getting-started" / "_hub-table.md"

# Hubs in the cloudbank cluster that are not campus course hubs.
NOT_A_CAMPUS = {"staging", "authoring", "demo", "gpu-demo"}

# Names that suggest a hub is infrastructure rather than a campus. Anything
# matching this but absent from NOT_A_CAMPUS is reported, so a new demo or
# staging hub upstream surfaces instead of quietly appearing as an institution.
SUSPICIOUS = re.compile(
    r"demo|test|staging|\bdev\b|sandbox|template|authoring|example", re.I
)

FALLBACK = f"""For the current list of campus hubs, see
[2i2c's hub reference]({SOURCE_HUMAN}) and look for hubs in the `cloudbank` cluster.
"""


def warn(message):
    print(f"generate_hub_table: {message}", file=sys.stderr)


def fetch_config():
    with urllib.request.urlopen(SOURCE, timeout=30) as response:
        return yaml.safe_load(response.read())


def build_table(config):
    """Return the Markdown table, or raise if the upstream shape changed."""
    hubs = config["hubs"]

    rows = []
    skipped = []
    for hub in hubs:
        name = hub["name"]
        if name in NOT_A_CAMPUS:
            skipped.append(name)
            continue
        label = hub.get("display_name") or name
        if SUSPICIOUS.search(f"{name} {label}"):
            warn(f"listing {name!r} ({label}) as a campus; add it to "
                 f"NOT_A_CAMPUS if that is wrong")
        rows.append((label, hub["domain"]))

    if not rows:
        raise ValueError("no campus hubs found in upstream config")

    rows.sort(key=lambda row: row[0].lower())

    if skipped:
        warn(f"skipped {len(skipped)} non-campus hubs: {', '.join(sorted(skipped))}")
    warn(f"found {len(rows)} campus hubs")

    today = datetime.date.today().isoformat()
    lines = ["| Institution | Hub |", "|---|---|"]
    lines += [f"| {label} | [{domain}](https://{domain}) |" for label, domain in rows]
    lines += [
        "",
        f"Retrieved from [2i2c's CloudBank cluster configuration]({SOURCE}) on {today}.",
        "",
    ]
    return "\n".join(lines)


def main():
    try:
        table = build_table(fetch_config())
    except Exception as error:
        warn(f"could not generate the hub table: {error}")
        if OUT.exists():
            warn(f"keeping the existing {OUT.relative_to(REPO_ROOT)}")
        else:
            OUT.parent.mkdir(parents=True, exist_ok=True)
            OUT.write_text(FALLBACK)
            warn(f"wrote a fallback {OUT.relative_to(REPO_ROOT)}")
        return 0

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(table)
    warn(f"wrote {OUT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
