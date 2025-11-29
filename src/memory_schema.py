from typing import List
from pydantic import BaseModel


class StatisticalMemory(BaseModel):
    """
    Long-term numerical stats about the fundraising campaign.

    This helps the agent:
    - Avoid repeating the same milestone posts.
    - Always know the lifetime totals.
    """
    total_lifetime_raised_usd: float = 0.0
    total_lifetime_km_run: float = 0.0
    last_update_date: str = "N/A"


class EpisodicMemory(BaseModel):
    """
    Episodic memory of previous successful posts.

    The agent can use this to:
    - Imitate past tone that worked well.
    - Avoid sending near-duplicate messages.
    """
    past_successful_posts: List[str] = []


class FullMemory(BaseModel):
    """
    Container for all memory types used by the agent.
    """
    statistical: StatisticalMemory = StatisticalMemory()
    episodic: EpisodicMemory = EpisodicMemory()
