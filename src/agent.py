from __future__ import annotations

from datetime import datetime
from typing import List, Optional, Dict, Any
from uuid import uuid4

from .schemas import (
    Platform,
    Tone,
    PostRequest,
    PostCandidate,
    JudgeFeedback,
    TrajectoryStep,
    TrajectoryLog,
    JudgeDecision,
)
from .tools import (
    get_memory_state,
    get_activity_summary,
    get_fundraising_summary,
    generate_post_candidates,
    judge_post_quality,
    simulate_publish_post,
    update_memory_state,
)

SYSTEM_INSTRUCTION = """
[... keep exactly as in previous message, or paste that long system text here ...]
"""
# To save space here, reuse the SYSTEM_INSTRUCTION you already pasted earlier.
# (If you don't have it, tell me and I'll resend a compact version.)


class RMHCRunRaiserAgent:
    # ... keep the full class implementation from my previous message ...
    # (No changes needed except the JudgeDecision import already handled)
    # Paste the whole class exactly as given before.
    ...
