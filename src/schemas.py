from __future__ import annotations

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class Platform(str, Enum):
    LINKEDIN = "linkedin"
    STRAVA = "strava"
    INTERNAL = "internal"


class Tone(str, Enum):
    PROFESSIONAL = "professional"
    MOTIVATIONAL = "motivational"
    CASUAL = "casual"


class JudgeDecision(str, Enum):
    APPROVE = "APPROVE"
    REVISE = "REVISE"
    REJECT = "REJECT"


class ActivitySummary(BaseModel):
    """Summary of one run or training session."""
    date: str
    distance_km: float
    duration_min: int
    pace_min_per_km: float
    event_name: str
    route_name: str


class DonationDetail(BaseModel):
    """One donation entry."""
    donor_name: str
    amount_usd: float
    message: Optional[str] = None


class FundraisingSummary(BaseModel):
    """Aggregated summary of fundraising progress."""
    total_raised_usd: float
    target_amount_usd: float
    percent_to_goal: float
    recent_donations: List[DonationDetail]


class PostRequest(BaseModel):
    """High-level user intention for the agent."""
    target_platform: Platform
    tone: Tone
    objective: str
    audience: str
    call_to_action_hint: str


class PostCandidate(BaseModel):
    """One candidate social post for a platform."""
    candidate_id: str
    platform: Platform
    text: str
    rationale: str
    risk_flags: List[str]


class JudgeFeedback(BaseModel):
    """Result from the LLM-as-a-Judge quality gate."""
    candidate_id: str
    score_0_100: int
    decision: JudgeDecision
    reasons: str
    required_edits: Optional[str] = None


class TrajectoryStep(BaseModel):
    """One step in the 7-step trajectory, for observability."""
    step_number: int
    step_name: str
    timestamp: str
    description: str
    tools_used: List[str]
    notes: Optional[Dict[str, Any]] = None


class TrajectoryLog(BaseModel):
    """Full execution trace for a single agent run."""
    session_id: str
    steps: List[TrajectoryStep]
    final_decision_summary: str
