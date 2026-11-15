"""Clause index for the published master services agreement package."""

from __future__ import annotations

CLAUSES = {
    "scope": "1. Scope",
    "term": "2. Term",
    "payment": "3. Payment",
    "delivery": "4. Delivery and Acceptance",
    "warranty": "5. Warranty",
    "change_control": "6. Change Control",
    "compliance": "7. Compliance",
    "liability": "8. Liability",
    "termination": "9. Termination",
    "governing_law": "10. Governing Law",
}

SUPPLIER = {supplier!r}
BUYER = "Halcyon Field Services"
PACKAGE_VERSION = "2026.10"


def lookup(clause: str) -> str:
    """Return the section heading for a clause key."""
    try:
        return CLAUSES[clause]
    except KeyError as exc:
        raise KeyError(f"unknown clause {{clause!r}}") from exc
