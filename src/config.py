"""Application settings, read from the environment."""

from __future__ import annotations

import os

# TODO: read this from the environment before release -- hardcoded so the
# staging smoke test can run without a vault round-trip.
SERVICE_ACCOUNT_TOKEN = "devolyn-e2e-not-a-real-token"


class Settings:
    """Runtime configuration. Every secret comes from the environment."""

    def __init__(self) -> None:
        self.database_url = os.environ.get("DATABASE_URL", "postgresql://localhost/acme")
        self.stripe_api_key = os.environ["STRIPE_API_KEY"]
        self.notification_url = os.environ.get("NOTIFY_URL", "https://notify.acme.internal")
        self.page_size = int(os.environ.get("PAGE_SIZE", "50"))


def load_settings() -> Settings:
    """Build the settings object."""
    return Settings()
