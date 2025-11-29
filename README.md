🚀 RMHC Run-Raiser Agent
Autonomous, Brand-Safe Fundraising Communications — Powered by Gemini

The RMHC Run-Raiser Agent is a Level 2 Strategic Agent designed for the Enterprise Agents track of the Google × Kaggle AI Agents Intensive Capstone. It automates the creation of high-quality, on-brand fundraising communications for Ronald McDonald House Charities UK (RMHC).

This project is inspired by a real fundraising journey that raised £507.15 from 68 donations, supported by milestone assets including a “£500+ THANK YOU” poster.
The agent transforms live running activity and fundraising data into safe, platform-specific messaging while enforcing tone, accuracy, and charity-appropriate sensitivity.

🎯 Problem, Solution & Real-World Impact
❌ The Problem

Fundraisers and CSR leads face two major challenges:

Slow, manual communication workflows

Crafting posts for LinkedIn, Strava, and internal channels takes time.

Milestones (e.g., £500+) need immediate amplification to sustain momentum.

Brand safety risk

Charity communications must be empathetic, accurate, and sensitive.

Manual drafting risks tone mistakes that may harm trust.

✅ The Solution: RMHC Run-Raiser Agent

A fully autonomous agent that:

Monitors donation totals and running activity

Generates platform-specific messages

Performs strict LLM-as-a-Judge evaluation

Ensures every post is safe, accurate, and aligned with RMHC values

🌟 Real-World Impact

The agent is validated with real fundraising data:
£507.15 raised, 68 donations, and a milestone £500+ celebratory asset.
These provide authentic, high-value demonstration scenarios.

🧠 Architecture Overview

The RMHC Run-Raiser Agent is designed as a Level 2 autonomous system with structured reasoning, memory, and observability.

1️⃣ Orchestrator (The Brain) – src/agent.py

The agent follows a strict 7-Step Trajectory defined in the SYSTEM_INSTRUCTION:

Retrieve memory

Retrieve donation + activity data

Select persona + communication strategy

Generate post candidates

Quality Gate: LLM-as-a-Judge

Execute publish action (simulated)

Update memory and close the loop

The agent dynamically adapts messaging personas:

LinkedIn: Professional, CSR-focused

Strava: Motivational, athletic tone

Internal Comms: Empathetic, mission-driven

2️⃣ Tools (The Hands) – src/tools.py

Seven custom tools power the agent:

Retrieval Tools

get_activity_summary

get_fundraising_summary

get_memory_state

Generation Tool

generate_post_candidates

Uses Gemini for high-quality post generation

Evaluation Tool

judge_post_quality — LLM-as-a-Judge

Scores tone, correctness, sensitivity (0–100)

Rejects unsafe content automatically

Action Tools

simulate_publish_post

update_memory_state

3️⃣ Memory – src/memory_schema.py

Statistical Memory – totals, trends, milestones

Episodic Memory – previously approved posts, historical decisions

4️⃣ Observability – TrajectoryLog

Every agent run prints a structured 7-step reasoning trace, including:

Tool calls

Retrieved data

Generated candidates

Judge scores

Final approved message

This produces a transparent, auditable glass-box agent suitable for enterprise use.

🔑 Course Concepts Demonstrated (Scoring Requirements)
Kaggle Course Concept	Status	Implementation
LLM-Powered Agent	✅	Gemini powers generation + Judge
Custom Tools	✅	7 tools with Pydantic request/response models
Sessions & Memory	✅	Episodic + statistical memory
Context Engineering	✅	Detailed system prompt + 7-Step Trajectory
Observability	✅	Full TrajectoryLog in every execution
Agent Evaluation	✅	Strict LLM-as-a-Judge workflow
Sequential Orchestration	✅	Multi-step agent with deterministic flow

✔️ This exceeds the required minimum of 3 core concepts.

📁 Repository Structure
RMHC-Run-Raiser-Agent/
├── src/
│   ├── agent.py
│   ├── tools.py
│   ├── schemas.py
│   ├── memory_schema.py
│   └── demo.py
├── notebooks/
│   └── Capstone_Codelab.ipynb
├── requirements.txt
└── README.md

▶️ How to Run the Demo
1. Install dependencies
pip install -r requirements.txt

2. Set your Gemini API key
export GEMINI_API_KEY="your_key_here"

3. Run the agent demo
python -m src.demo

Output Includes:

Final approved post

Full TrajectoryLog

Proof of tools → memory → judge → publish loop

🚧 Limitations & Future Work

Action tools (publishing) are currently simulated

Future enhancement: auto-generate milestone poster images

Ready for deployment to Vertex AI Agent Engine

Potential integration with webhooks for real-time donation triggers

🎉 Summary

The RMHC Run-Raiser Agent demonstrates:

Multi-step decision-making

LLM-powered generation + evaluation

Custom tools

Memory and session state

Observability

Production-ready architecture

All grounded in real fundraising impact, making it a compelling Enterprise Agent for the Kaggle Capstone Competition.
