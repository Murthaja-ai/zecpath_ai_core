# Zecpath - AI-Powered Autonomous Hiring Platform

## 📌 Executive Overview
Zecpath is an end-to-end, AI-first hiring platform designed to fully automate the recruitment lifecycle—from initial resume screening to final offer letter generation. As outlined in the Zecpath 100-Phase Product Requirements Document (PRD), this system eliminates manual HR workloads through AI-driven Applicant Tracking, natural-sounding multilingual Voice AI interviews, behavioral analysis, and automated decision-making.

This repository (`zecpath_ai_core`) contains the foundational backend architecture, structured as a Monorepo containing two distinct enterprise microservices:

1. **The ATS Document Engine (Phases 1-2):** Ingests raw resumes, extracts technical skills via custom Knowledge Graphs, calculates experience relevance, and ranks candidates against job descriptions.
2. **The Voice Screening AI (Phases 3-10):** An automated HR interviewer that reads the ATS shortlist, conducts dynamic voice interviews, grades answers mathematically, handles edge-case chaos (noise/language mixing), and serves the results via a secure API.

## 🗂️ System Documentation Hub
Because of the massive scale of this enterprise architecture, technical documentation is split by microservice. Click the links below to view the detailed architecture, file structures, and execution commands for each system:

* ➡️ **[Phase 1: ATS & Document Intelligence (Days 1 - 21)](./parsers/README.md)**
* ➡️ **[Phase 2: Voice Screening AI & API (Days 22 - 32)](./screening_ai/README.md)**

## 🚀 Global Setup & Installation

**1. Clone the repository**
git clone [https://github.com/Murthaja-ai/zecpath_ai_core.git](https://github.com/Murthaja-ai/zecpath_ai_core.git)
cd zecpath_ai_core

**2. Create and activate a Virtual Environment**
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

**3. Install Dependencies**
pip install -r requirements.txt
pip install sentence-transformers torch flask