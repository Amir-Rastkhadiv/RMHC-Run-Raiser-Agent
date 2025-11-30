from __future__ import annotations

from datetime import datetime, timezone
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
You are the RMHC Run-Raiser Agent.

Mission:
- Help a fundraiser for Ronald McDonald House Charities communicate milestones
  safely and effectively on LinkedIn, Strava-style feeds, and internal channels.
- Always protect the RMHC brand (empathy, accuracy, sensitivity).

You follow a mandatory 7-STEP TRAJECTORY:
1) Retrieve memory
2) Retrieve latest activity + fundraising data
3) Plan communication strategy (persona, tone, objective)
4) Generate post candidates
5) Quality Gate (LLM-as-a-Judge)
6) Execute action (simulate publish)
7) Update memory + log the trajectory
"""


class RMHCRunRaiserAgent:
    """Level 2 orchestrator with tools, memory, and observability."""

    def __init__(self) -> None:
        self.system_instruction = SYSTEM_INSTRUCTION

    def _now_iso(self) -> str:
        """Return current UTC time as ISO string (timezone-aware)."""
        return datetime.now(timezone.utc).isoformat()

    def _add_step(
        self,
        steps: List[TrajectoryStep],
        step_number: int,
        step_name: str,
        description: str,
        tools_used: Optional[List[str]] = None,
        notes: Optional[Dict[str, Any]] = None,
    ) -> None:
        step = TrajectoryStep(
            step_number=step_number,
            step_name=step_name,
            timestamp=self._now_iso(),
            description=description,
            tools_used=tools_used or [],
            notes=notes or {},
        )
        steps.append(step)

    def run(self, post_request: PostRequest) -> Dict[str, Any]:
        """Run full 7-step trajectory for one PostRequest."""
        steps: List[TrajectoryStep] = []
        session_id = str(uuid4())

        # Step 1: memory
        memory = get_memory_state()
        self._add_step(
            steps, 1, "Retrieve Memory",
            "Loaded statistical and episodic memory.",
            tools_used=["get_memory_state"],
        )

        # Step 2: data
        activity = get_activity_summary()
        fundraising = get_fundraising_summary()
        self._add_step(
            steps, 2, "Retrieve Data",
            "Fetched latest activity and fundraising stats.",
            tools_used=["get_activity_summary", "get_fundraising_summary"],
            notes={
                "distance_km": activity.distance_km,
                "total_raised_usd": fundraising.total_raised_usd,
                "percent_to_goal": fundraising.percent_to_goal,
            },
        )

        # Step 3: plan
        self._add_step(
            steps, 3, "Plan Communication Strategy",
            "Using PostRequest to select persona and objective.",
            notes={
                "target_platform": post_request.target_platform.value,
                "tone": post_request.tone.value,
                "objective": post_request.objective,
                "audience": post_request.audience,
            },
        )

        # Step 4: generate candidates
        candidates = generate_post_candidates(post_request, activity, fundraising)
        self._add_step(
            steps, 4, "Generate Candidates",
            f"Generated {len(candidates)} post candidates (simulated Gemini).",
            tools_used=["generate_post_candidates"],
            notes={"candidate_ids": [c.candidate_id for c in candidates]},
        )

        # Step 5: judge
        best_candidate = None
        best_feedback = None
        best_score = -1
        for c in candidates:
            fb = judge_post_quality(c, post_request.target_platform)
            if fb.score_0_100 > best_score:
                best_score = fb.score_0_100
                best_candidate = c
                best_feedback = fb

        self._add_step(
            steps, 5, "Quality Gate (Judge)",
            "Evaluated candidates and selected the top-scoring safe option.",
            tools_used=["judge_post_quality"],
            notes={
                "selected_candidate_id": best_candidate.candidate_id,
                "score_0_100": best_feedback.score_0_100,
                "decision": best_feedback.decision,
            },
        )

        # Step 6: simulate publish
        publish_result = simulate_publish_post(best_candidate)
        self._add_step(
            steps, 6, "Simulate Publish",
            "Simulated publishing the approved post.",
            tools_used=["simulate_publish_post"],
            notes={"publish_result": publish_result},
        )

        # Step 7: update memory + finalise
        update_memory_state(memory, best_candidate)
        final_summary = (
            f"Published a {post_request.target_platform.value} post with objective "
            f"'{post_request.objective}'. Judge score: {best_feedback.score_0_100}."
        )
        self._add_step(
            steps, 7, "Update Memory & Finalise",
            "Updated memory (simulated) and finalised trajectory.",
            tools_used=["update_memory_state"],
            notes={"final_decision_summary": final_summary},
        )

        trajectory_log = TrajectoryLog(
            session_id=session_id,
            steps=steps,
            final_decision_summary=final_summary,
        )

        return {
            "final_post": best_candidate,
            "judge_feedback": best_feedback,
            "trajectory_log": trajectory_log,
        }
