# Project Brief: LifeOS

## Project Overview

LifeOS is a personal goal management system designed to help users quickly create, categorize, and break down vague ideas into actionable clear goals. The system leverages AI, psychology principles, and two-way communication to create an effective goal management experience.

## Core Requirements

1. **Goal Management**

    - Create and store goals with titles, descriptions, and tags
    - Categorize goals into predefined categories (career, health, etc.)
    - Break down large goals into smaller, actionable steps
    - Track goal status and progress

2. **Psychological Framework Integration**

    - Address procrastination factors (emotional blockage, task size, motivation)
    - Ensure clarity on next actions for each goal
    - Clarify the importance/why behind each goal
    - Support effective prioritization

3. **Multiple Views**
    - Broad overview of all goals
    - Category-specific views
    - Detailed single-goal view
    - Action-oriented views
    - Progress/calendar views

## Technical Requirements

1. **Frontend**

    - Framework: Next.js
    - Styling: Mantine UI
    - Features:
        - Goal input interface
        - List and tree visualization of goals
        - Responsive design

2. **Backend**

    - Language: Python
    - Framework: Chalice (AWS)
    - Database: DynamoDB
    - API endpoints for goal CRUD operations

3. **Deployment**
    - Cloud Service: AWS
    - Local development environment setup

## Project Scope

### In Scope

-   Goal creation, categorization, and breakdown
-   Multiple view interfaces for different goal perspectives
-   Integration of psychological principles into the user experience
-   Basic user authentication and data persistence

### Out of Scope (for initial version)

-   Multi-user collaboration
-   Advanced analytics and reporting
-   Mobile applications (focus on web interface)
-   Integration with third-party productivity tools

## Success Criteria

-   User can create, categorize, and break down goals
-   System effectively addresses psychological aspects of goal management
-   Interface provides multiple useful views of goal data
-   Personal use demonstrates improved goal clarity and action-taking
