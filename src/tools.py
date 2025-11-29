from __future__ import annotations

from typing import List
from datetime import datetime

from .schemas import (
    ActivitySummary,
    FundraisingSummary,
    DonationDetail,
    PostRequest,
    PostCandidate,
    JudgeFeedback,
    Platform,
    JudgeDecision,
)
from .memory_schema import FullMemory


# NOTE: In a real system, these tools would call external services (Strava, JustGiving, etc.)
# and Gemini for content generation. For the capstone demo we keep them as
# safe, deterministic stubs that are easy to run and easy for judges to read.


# TYPE: Retrieving Information (R)
def get_memory_state() -> FullMemory:
    """
    Retrieve the current memory state.

    For this demo we simulate a pre-populated memory object.
    """
    return FullMemory(
        statistical={
            "total_lifetime_raised_usd": 507.15,
            "total_lifetime_km_run": 42.2,
            "last_update_date": datetime.utcnow().date().isoformat(),
        },
        episodic={
            "past_successful_posts": [
                "Huge thank you to everyone who helped us cross the £500 line for RMHC!",
            ]
        },
    )


# TYPE: Retrieving Information (R)
def get_activity_summary() -> ActivitySummary:
    """
    Return a simulated running activity summary.

    In a real agent this would call Strava or a similar API.
    """
    return ActivitySummary(
        date=datetime.utcnow().date().isoformat(),
        distance_km=10.0,
        duration_min=55,
        pace_min_per_km=5.5,
        event_name="Southend Seafront 10K",
        route_name="Black Friday Coastal Loop",
    )


# TYPE: Retrieving Information (R)
def get_fundraising_summary() -> FundraisingSummary:
    """
    Return a simulated fundraising summary.

    Values are inspired by the real JustGiving campaign (~£507+).
    """
    total = 507.15
    target = 500.0
    percent = round((total / target) * 100, 1)

    recent = [
        DonationDetail(donor_name="Anonymous", amount_usd=25.0, message="Keep going!"),
        DonationDetail(donor_name="Local Guest", amount_usd=15.0, message="For RMHC families."),
    ]

    return FundraisingSummary(
        total_raised_usd=total,
        target_amount_usd=target,
        percent_to_goal=percent,
        recent_donations=recent,
    )


# TYPE: Executing Action (A) – LLM Content Generation (simulated)
def generate_post_candidates(
    post_request: PostRequest,
    activity: ActivitySummary,
    fundraising: FundraisingSummary,
) -> List[PostCandidate]:
    """
    Generate several candidate posts for the requested platform.

    For the demo, we simulate three candidates.
    In a real implementation this would call Gemini.
    """
    base_text = (
        f"We’ve just passed £{fundraising.total_raised_usd:.2f} for Ronald McDonald House Charities, "
        f"after a {activity.distance_km:.1f} km run along {activity.route_name}."
    )

    candidates: List[PostCandidate] = []

    candidates.append(
        PostCandidate(
            candidate_id="c1",
            platform=post_request.target_platform,
            text=(
                f"{base_text} Thank you to all {len(fundraising.recent_donations)} recent donors – "
                f"your support keeps families close to their children in hospital. "
                f"{post_request.call_to_action_hint}"
            ),
            rationale="Balanced gratitude, mentions impact for RMHC families.",
            risk_flags=[],
        )
    )

    candidates.append(
        PostCandidate(
            candidate_id="c2",
            platform=post_request.target_platform,
            text=(
                f"{base_text} We’ve smashed our initial £{fundraising.target_amount_usd:.0f} goal, "
                f"but every extra pound helps another family stay near the care they need."
            ),
            rationale="Focuses on milestone and continued need without pressure.",
            risk_flags=[],
        )
    )

    candidates.append(
        PostCandidate(
            candidate_id="c3",
            platform=post_request.target_platform,
            text=(
                f"{base_text} If you can, please consider donating or sharing this campaign today "
                f"so RMHC can support even more families."
            ),
            rationale="Gentle call-to-action with clear purpose.",
            risk_flags=[],
        )
    )

    return candidates


# TYPE: Executing Action (A) – LLM-as-a-Judge (simulated)
def judge_post_quality(candidate: PostCandidate, platform: Platform) -> JudgeFeedback:
    """
    Simulated LLM-as-a-Judge.

    In the real system this would call Gemini with a rubric for tone, safety and accuracy.
    Here we give simple deterministic scores.
    """
    # Very simple scoring heuristic for the demo:
    base_score = 80

    if "smashed" in candidate.text.lower():
        base_score += 5  # energetic but still safe
    if "please consider donating" in candidate.text.lower():
        base_score += 5  # clear call-to-action

    score = min(base_score, 95)

    decision = JudgeDecision.APPROVE
    reasons = (
        f"Tone appropriate for {platform.value}, clear gratitude and impact, "
        "no obvious brand or sensitivity issues."
    )

    return JudgeFeedback(
        candidate_id=candidate.candidate_id,
        score_0_100=score,
        decision=decision,
        reasons=reasons,
        required_edits=None,
    )


# TYPE: Executing Action (A)
def simulate_publish_post(final_post: PostCandidate) -> str:
    """
    Simulate publishing a post.

    For the demo we simply return a string that would be logged.
    """
    return (
        f"[SIMULATED PUBLISH] Platform={final_post.platform.value} | "
        f"Text='{final_post.text[:120]}...'"
    )


# TYPE: Executing Action (A)
def update_memory_state(memory: FullMemory, final_post: PostCandidate) -> str:
    """
    Update memory with the new post.

    For simplicity we just pretend to append to episodic memory and bump totals.
    """
    # In a real system we'd mutate and persist the memory.
    _ = memory
    _ = final_post
    return "[MEMORY UPDATED] Added latest post to episodic history."

