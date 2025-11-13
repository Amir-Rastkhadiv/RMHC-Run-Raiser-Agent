# 🚀 RMHC Run-Raiser Agent: A Context-Engineered Social Fundraising Agent

## Project Overview
This Capstone Project demonstrates the development of an autonomous AI agent to amplify fundraising efforts for the Ronald McDonald House Charities (RMHC). The agent utilizes Google's **Agent Development Kit (ADK)** and the Gemini API to dynamically generate and post personalized social media content based on real-time event data (running activity, donation progress).

## Architectural Pillars (Based on Google's ADK Whitepapers)

This agent is built upon a state-of-the-art architecture:

| Pillar | Concept (Whitepaper Day) | Implementation Detail |
| :--- | :--- | :--- |
| **Brain** | Level 1: Connected Problem-Solver (Day 1) | Gemini 2.5 Pro/Flash for complex reasoning and creative text generation. |
| **Hands** | Custom Tools & Function Calling (Day 2) | Custom `SocialPosterTool` and `FundTrackerTool` for external API interaction. |
| **Memory** | Extraction & Retrieval (Day 3) | Uses a **Vector Database** (e.g., ChromaDB/Pinecone) to store and retrieve long-term donor preferences and running milestones. |
| **Quality** | Trajectory Evaluation (Day 4) | Uses the LLM-as-a-Judge paradigm to evaluate post quality (e.g., effectiveness, tone adherence). |

## Codelab Execution
The full code and execution environment are available in the following Google Colab/Kaggle notebook:
- [Capstone_Codelab.ipynb](notebooks/Capstone_Codelab.ipynb)
