"""
demo.py

Simple CLI demo for the RMHC Run-Raiser Agent.

Run from repo root with:
    python -m src.demo
"""

from __future__ import annotations

from textwrap import indent

from .agent import RMHCRunRaiserAgent
from .schemas import Platform, Tone, PostRequest, TrajectoryLog


def pretty_print_trajectory(log: TrajectoryLog) -> None:
    """Print the TrajectoryLog in a judge-friendly way."""
    print("\n==================== TRAJECTORY LOG ====================")
    print(f"Session ID: {log.session_id}")
    print("--------------------------------------------------------")

    for step in log.steps:
        print(f"[Step {step.step_number}] {step.step_name} @ {step.timestamp}")
        print(indent(step.description, prefix="  "))
        if step.tools_used:
            print(f"  Tools used: {', '.join(step.tools_used)}")
        if step.notes:
            print("  Notes:")
            for k, v in (step.notes or {}).items():
                print(f"    - {k}: {v}")
        print("--------------------------------------------------------")

    print("FINAL DECISION SUMMARY:")
    print(indent(log.final_decision_summary, prefix="  "))
    print("========================================================\n")


def main() -> None:
    post_request = PostRequest(
        target_platform=Platform.LINKEDIN,
        tone=Tone.PROFESSIONAL,
        objective="Celebrate hitting the £500+ fundraising milestone and encourage further support.",
        audience="Corporate partners and professional network",
        call_to_action_hint="Invite colleagues and partners to donate or share the campaign.",
    )

    agent = RMHCRunRaiserAgent()
    result = agent.run(post_request)

    final_post = result["final_post"]
    judge_feedback = result["judge_feedback"]
    trajectory_log: TrajectoryLog = result["trajectory_log"]

    print("\n==================== FINAL APPROVED POST ====================")
    print(f"Platform: {final_post.platform.value}")
    print("Text:")
    print(indent(final_post.text, prefix="  "))
    print("\nRationale:")
    print(indent(final_post.rationale, prefix="  "))
    print("\nJudge Feedback:")
    print(f"  Score:    {judge_feedback.score_0_100}")
    print(f"  Decision: {judge_feedback.decision}")
    print(f"  Reasons:  {judge_feedback.reasons}")
    if judge_feedback.required_edits:
        print(f"  Required edits: {judge_feedback.required_edits}")
    print("=============================================================")

    pretty_print_trajectory(trajectory_log)


if __name__ == "__main__":
    main()
