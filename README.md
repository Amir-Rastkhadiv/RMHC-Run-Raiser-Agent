# 🚀 RMHC Run-Raiser Agent: A Production-Ready Social Fundraising Agent

## Project Overview
This Capstone Project demonstrates the development of an autonomous AI agent to amplify fundraising efforts for the Ronald McDonald House Charities (RMHC). The agent utilizes Google's **Agent Development Kit (ADK)** and the Gemini API to dynamically generate and post personalized social media content based on real-time event and running data.

## Architectural Pillars (Leveraging Day 1 - Day 5 Frameworks)

This agent is built upon a state-of-the-art, production-grade architecture:

| Pillar | Core Concept (Whitepaper Day) | Implementation Detail |
| :--- | :--- | :--- |
| **Brain** | [cite_start]Level 1: Connected Problem-Solver (Day 1) [cite: 1119] | Gemini 2.5 Pro/Flash for complex reasoning and creative text generation. |
| **Hands** | [cite_start]Custom Agent Tools (Day 2) [cite: 2012] | Custom `SocialPosterTool` and `FundTrackerTool` for external API interaction. [cite_start]**Best practice:** granular tools with concise output[cite: 2012]. |
| **Memory** | [cite_start]Multimodal Context & Extraction (Day 3) [cite: 2970, 2968] | [cite_start]Uses a **Vector Database** for **Multimodal Memory** storage, retrieving running images (like the QR code/route map) and donor facts for personalization[cite: 2970]. |
| **Quality** | [cite_start]Trajectory Evaluation (Day 4) [cite: 4136] | [cite_start]Leverages the **LLM-as-a-Judge** paradigm to automatically evaluate post quality (e.g., tone adherence, motivational impact) before posting[cite: 4138]. |
| **Operations**| [cite_start]CI/CD & Safe Rollout (Day 5)  | [cite_start]Designed for an **Automated CI/CD Pipeline** with **Evaluation as a Quality Gate** before deploying new agent versions to production[cite: 5159, 5160, 5159, 5160, 5159, 5160, 5159, 5160]. |


---

## ⚙️ Agent Architecture & Orchestration

This agent is designed as a **Strategic Problem-Solver (Level 2)**, capable of contextual reasoning, tone switching, and multi-platform action. This complexity is managed through a clear separation of Model, Tools, and Orchestration.

### 1. Model & Persona Management (The Brain)

| Component | Description | Key Mechanism |
| :--- | :--- | :--- |
| **System Instruction** | Defines the agent's core goal (fundraising communications) and its conditional personas. | **Tone Switching:** Uses `IF/THEN` logic to adopt **Professional** (LinkedIn), **Athletic** (Strava), or **Mission-Driven** (Blink) tones. |
| **Data Relevance** | Prioritizes the data based on the platform and audience. | **Priority Rule:** Financial Data for LinkedIn, Athletic Data for Strava, Mission Data for Blink. |

### 2. Tools & Capabilities (The Hands)

Following the **Principle of Granularity**, the agent uses three specialized, action-oriented tools.

| Tool Name | Target Platform | Purpose |
| :--- | :--- | :--- |
| `LinkedInPosterTool` | LinkedIn | Publishes professional content, prioritizing financial impact and corporate partnerships. |
| `StravaUploaderTool` | Strava | Publishes motivational running content, requiring verified athletic data (distance, pace). |
| `InternalCommsTool` | Blink (McD Connect) | Publishes mission-focused updates for internal RMHC and UK McDonald's colleagues. |

### 3. Orchestration Trajectory (The Workflow)

This 7-step process ensures reliability and consistency for every post generated.

1.  **Retrieve Memory:** Pull current fundraising and running totals (Statistical Memory).
2.  **Data Retrieval:** Fetch the latest activity and donation data.
3.  **Contextual Reasoning:** Select the target platform, tone, and data focus based on the System Instruction.
4.  **Content Generation:** Draft the post, ensuring the **Conditional Call-to-Action (CTA)** is included.
5.  **Quality Gate Check:** Run platform-specific compliance and accuracy checks (e.g., *Compliance Gate* for LinkedIn).
6.  **Tool Execution:** Call the specific posting tool (e.g., `StravaUploaderTool`).
7.  **Update Memory:** Store new running totals and a record of the post (Episodic Memory).

### 4. Memory System (The History)

| Type | Data Stored | Function in Workflow |
| :--- | :--- | :--- |
| **Statistical Memory** | Total money raised, total kilometers run, percentage to goal. | Provides cumulative totals for milestone-based content. |
| **Episodic Memory** | Records of the last 10 posts, post sentiment, and resulting engagement. | Used to vary post tone and content, avoiding repetition. |

---

6.  **Commit the Changes:** Scroll to the bottom of the edit screen. The default commit message will be fine (e.g., "Update README.md"), or you can type a more descriptive one like: `feat: Add detailed multi-platform agent architecture to README`.
7.  Click the green **"Commit changes"** button.

Once you confirm the update is complete, we can start writing the actual code in your Colab/Kaggle notebook!

## Execution and Observability
The full code and execution environment are available in the [Capstone_Codelab.ipynb](notebooks/Capstone_Codelab.ipynb). [cite_start]**Observability** (Logging, Tracing, Metrics) is foundational for ensuring the agent is reliable and trustworthy[cite: 4138].



