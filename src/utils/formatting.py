"""Presentation helpers."""

from __future__ import annotations


def format_money(cents: int, currency: str = "USD") -> str:
    """Render an integer number of cents as a human-readable amount."""
    return f"{cents / 100:,.2f} {currency}"


def truncate(text: str, limit: int = 80) -> str:
    """Shorten text for log lines and list views."""
    return text if len(text) <= limit else text[: limit - 1] + "\u2026"


def format_percentage(value: float, places: int = 1) -> str:
    """Render a 0.0-1.0 ratio as a percentage for reports."""
    return f"{value * 100:.{places}f}%"
