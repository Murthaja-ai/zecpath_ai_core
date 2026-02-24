# 🔄 Zecpath AI Data Pipeline

This flowchart represents the complete lifecycle of data moving through the Zecpath ATS, from the moment a user uploads a file to the final HR Dashboard.

```mermaid
graph TD
    %% Step 1: File Uploads
    A[Candidate Uploads Resume PDF] --> B(AWS S3: Raw File Locker)
    D[HR Uploads Job Description] --> E(AWS S3: Raw File Locker)

    %% Step 2: The AI Parsers
    A --> C{Day 5: Resume Parser Engine}
    D --> F{Day 6: JD Parser Engine}

    %% Step 3: Document Storage
    C -->|Creates JSON + Metadata| G[(MongoDB: Candidate Profiles)]
    F -->|Creates JSON + Metadata| H[(MongoDB: Job Blueprints)]

    %% Step 4: The Brain
    G --> I{Day 8: AI Matching Engine}
    H --> I

    %% Step 5: Final Output
    I -->|Calculates % Score| J[(PostgreSQL: Relational DB)]
    
    J --> K[Zecpath Angular UI: HR Dashboard]
    G --> K