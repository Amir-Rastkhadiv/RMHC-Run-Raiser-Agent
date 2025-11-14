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

## Execution and Observability
The full code and execution environment are available in the [Capstone_Codelab.ipynb](notebooks/Capstone_Codelab.ipynb). [cite_start]**Observability** (Logging, Tracing, Metrics) is foundational for ensuring the agent is reliable and trustworthy[cite: 4138].



