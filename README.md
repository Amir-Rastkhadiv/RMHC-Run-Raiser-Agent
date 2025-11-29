# 🚀 RMHC Run-Raiser Agent: Autonomous, Brand-Safe Fundraising Communications

**Subtitle:** A Level 2 Strategic Agent for the Enterprise Agents track, powered by Gemini.

The **RMHC Run-Raiser Agent** is designed for the Enterprise Agents track of the Google × Kaggle AI Agents Intensive Capstone. It automates the creation of high-quality, on-brand fundraising communications for Ronald McDonald House Charities UK (RMHC).

This project is inspired by a real fundraising journey that **raised £507.15 from 68 donations**, supported by milestone assets including a “£500+ THANK YOU” poster. The agent transforms live running activity and fundraising data into safe, platform-specific messaging while enforcing tone, accuracy, and charity-appropriate sensitivity.

---

## 🎯 Problem, Solution, & Real-World Impact

### ❌ The Problem

Fundraisers and CSR leads face two major challenges:

* **Slow, Manual Communication Workflows:** Crafting posts for LinkedIn, Strava, and internal channels takes time. Milestones (e.g., £500+) need immediate amplification to sustain momentum.
* **Brand Safety Risk:** Charity communications must be empathetic, accurate, and sensitive. Manual drafting risks tone mistakes that may harm trust and brand integrity.

### ✅ The Solution: RMHC Run-Raiser Agent

A fully autonomous agent that:
* Monitors donation totals and running activity.
* Generates platform-specific messages (LinkedIn, Strava, Internal Comms).
* Performs strict **LLM-as-a-Judge** evaluation to ensure brand safety.
* Ensures every post is safe, accurate, and aligned with RMHC values.

### 🌟 Real-World Impact

The agent is validated with real fundraising data: **£507.15 raised, 68 donations**, and a milestone £500+ celebratory asset. These provide authentic, high-value demonstration scenarios, proving the agent's ability to drive fundraising momentum in an enterprise context.

---

## 🧠 Architecture Overview: Level 2 Strategic Problem-Solver

The RMHC Run-Raiser Agent is designed as a Level 2 autonomous system with structured reasoning, memory, and observability.

### 1️⃣ Orchestrator (The Brain) – `src/agent.py`

The agent follows a strict **7-Step Trajectory** defined in the `SYSTEM_INSTRUCTION` (Context Engineering):

1.  Retrieve memory state.
2.  Retrieve donation + activity data.
3.  Select persona + communication strategy (Formulate `PostRequest`).
4.  Generate post candidates (Gemini call).
5.  **Quality Gate: LLM-as-a-Judge** (Mandatory evaluation).
6.  Execute publish action (simulated).
7.  Update memory and close the loop.

The agent dynamically adapts messaging personas:
* **LinkedIn:** Professional, CSR-focused
* **Strava:** Motivational, athletic tone
* **Internal Comms:** Empathetic, mission-driven

### 2️⃣ Tools (The Hands) – `src/tools.py`

Seven custom tools power the agent's actions and data retrieval:

| Tool Category | Tool Name | Type | Purpose |
| :--- | :--- | :--- | :--- |
| **Retrieval (R)** | `get_activity_summary` | R | Fetches latest running data. |
| **Retrieval (R)** | `get_fundraising_summary` | R | Fetches donation totals (£507.15). |
| **Retrieval (R)** | `get_memory_state` | R | Fetches statistical/episodic memory. |
| **Generation (A)** | `generate_post_candidates` | A | Uses Gemini for content creation. |
| **Evaluation (A)** | `judge_post_quality` | A | **LLM-as-a-Judge** (Scores 0–100, rejects unsafe content). |
| **Action (A)** | `simulate_publish_post` | A | Logs the final approved post. |
| **Action (A)** | `update_memory_state` | A | Records the successful run. |

### 3️⃣ Memory – `src/memory_schema.py`

* **Statistical Memory:** Stores campaign totals, trends, and key milestones.
* **Episodic Memory:** Stores a list of previously approved posts and historical decisions.

### 4️⃣ Observability – `TrajectoryLog`

Every agent run generates and prints a structured **7-step reasoning trace** (`TrajectoryLog`). This audit trail captures: Tool calls, retrieved data, judge scores, and the final decision rationale. This provides a transparent, auditable **"Glass-Box"** agent suitable for enterprise use.

---

## 🔑 Course Concepts Demonstrated (Scoring Requirements)

| Kaggle Course Concept | Status | Implementation Detail |
| :--- | :--- | :--- |
| **LLM-Powered Agent** | ✅ | Gemini powers content generation + Judge logic. |
| **Custom Tools** | ✅ | 7 custom tools with Pydantic request/response models. |
| **Sessions & Memory** | ✅ | Episodic + statistical memory used to inform decisions. |
| **Context Engineering** | ✅ | Detailed system prompt enforces the 7-Step Trajectory. |
| **Observability** | ✅ | Full `TrajectoryLog` is generated and displayed in every execution. |
| **Agent Evaluation** | ✅ | Strict **LLM-as-a-Judge** workflow as the Quality Gate. |
| **Sequential Orchestration** | ✅ | Multi-step agent with deterministic flow (Level 2). |

**Note:** This project exceeds the required minimum of 3 core concepts.

---

## 📁 Repository Structure

RMHC-Run-Raiser-Agent/ ├── src/ │ ├── agent.py # Orchestration logic, SYSTEM_INSTRUCTION │ ├── tools.py # All 7 custom tools (R/A/Judge) │ ├── schemas.py # Pydantic I/O models, JudgeFeedback, TrajectoryLog │ ├── memory_schema.py # Memory structures (Statistical/Episodic) │ └── demo.py # CLI execution script ├── notebooks/ │ └── Capstone_Codelab.ipynb # Walkthrough notebook ├── requirements.txt # Dependencies: google-genai, pydantic └── README.md


## ▶️ How to Run the Demo

### Prerequisites
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Set your Gemini API key:
    ```bash
    export GEMINI_API_KEY="your_key_here"
    ```

### Execution
Run the agent demo from the root directory:
```bash
python -m src.demo

### Output Includes:

Final approved post

Full TrajectoryLog

Proof of tools → memory → judge → publish loop

