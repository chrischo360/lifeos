# System Patterns: LifeOS

## System Architecture

LifeOS follows a client-server architecture with a clear separation of concerns:

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Client    │◄────►│   Server    │◄────►│  Database   │
│  (Next.js)  │      │  (Python)   │      │ (DynamoDB)  │
└─────────────┘      └─────────────┘      └─────────────┘
```

### Client Architecture

The client follows a component-based architecture using Next.js and React:

```
┌─────────────────────────────────────────┐
│               Next.js App               │
│                                         │
│  ┌─────────────┐     ┌─────────────┐    │
│  │    Pages    │     │  Components │    │
│  └─────────────┘     └─────────────┘    │
│                                         │
│  ┌─────────────┐     ┌─────────────┐    │
│  │    State    │     │    API      │    │
│  │  Management │     │   Client    │    │
│  └─────────────┘     └─────────────┘    │
└─────────────────────────────────────────┘
```

### Server Architecture

The server uses AWS Chalice for serverless API endpoints:

```
┌─────────────────────────────────────────┐
│               AWS Chalice               │
│                                         │
│  ┌─────────────┐     ┌─────────────┐    │
│  │   Routes    │     │   Models    │    │
│  └─────────────┘     └─────────────┘    │
│                                         │
│  ┌─────────────┐     ┌─────────────┐    │
│  │  Services   │     │ DynamoDB    │    │
│  │             │     │ Integration │    │
│  └─────────────┘     └─────────────┘    │
└─────────────────────────────────────────┘
```

## Key Technical Decisions

1. **Next.js for Frontend**

    - Provides server-side rendering capabilities
    - Offers file-based routing
    - Supports TypeScript for type safety
    - Enables API routes for backend functionality

2. **Mantine UI for Components**

    - Provides accessible, customizable components
    - Offers theming capabilities
    - Includes form handling utilities
    - Reduces need for custom component development

3. **Python with Chalice for Backend**

    - Serverless architecture reduces operational complexity
    - AWS integration simplifies cloud deployment
    - Python enables rapid development
    - Chalice handles API routing and AWS resource management

4. **DynamoDB for Data Storage**

    - Serverless database with automatic scaling
    - Flexible schema for evolving data models
    - Low latency for fast read/write operations
    - Pay-per-use pricing model

5. **AWS for Cloud Infrastructure**
    - Serverless architecture with Lambda functions
    - API Gateway for HTTP endpoints
    - IAM for security and access control
    - CloudWatch for monitoring and logging

## Design Patterns

1. **Component Pattern**

    - UI elements are broken down into reusable components
    - Components maintain their own state when appropriate
    - Props are used for component configuration
    - Example: GoalInput component for creating goals

2. **Container/Presenter Pattern**

    - Separation between data handling and presentation
    - Container components manage state and data fetching
    - Presenter components focus on rendering UI
    - Improves testability and separation of concerns

3. **Repository Pattern**

    - Abstracts data access logic
    - Provides consistent interface for database operations
    - Centralizes data manipulation logic
    - Simplifies testing with mock repositories

4. **Service Pattern**

    - Encapsulates business logic
    - Provides reusable services for common operations
    - Separates concerns between data access and business rules
    - Improves maintainability and testability

5. **State Management**
    - Local component state for UI-specific state
    - Potential for global state management as app grows
    - Clear data flow patterns from parent to child components
    - API calls for server-side data operations

## Component Relationships

### Frontend Components

```
┌─────────────────────────────────────────┐
│               App (_app.tsx)            │
└───────────────────┬─────────────────────┘
                    │
        ┌───────────┴─────────────┐
        │                         │
┌───────▼──────────┐     ┌────────▼─────────┐
│    HomePage      │     │   [Other Pages]   │
└───────┬──────────┘     └──────────────────┘
        │
┌───────▼──────────┐
│    GoalInput     │
└──────────────────┘
```

### Backend Components

```
┌─────────────────────────────────────────┐
│               Chalice App               │
└───────────────────┬─────────────────────┘
                    │
        ┌───────────┴─────────────┐
        │                         │
┌───────▼──────────┐     ┌────────▼─────────┐
│  /goals Route    │     │   /goal Route    │
└───────┬──────────┘     └────────┬─────────┘
        │                         │
┌───────▼──────────┐     ┌────────▼─────────┐
│  DynamoDB Table  │     │  DynamoDB Table  │
└──────────────────┘     └──────────────────┘
```

## Critical Implementation Paths

### Goal Creation Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ User enters │     │ Client-side │     │ API request │     │ Server      │
│ goal data   ├────►│ validation  ├────►│ to /goal    ├────►│ processes   │
│             │     │             │     │             │     │ request     │
└─────────────┘     └─────────────┘     └─────────────┘     └──────┬──────┘
                                                                   │
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌──────▼──────┐
│ Client      │     │ User sees   │     │ Response    │     │ Save to     │
│ updates UI  │◄────┤ confirmation│◄────┤ returned to │◄────┤ DynamoDB    │
│             │     │             │     │ client      │     │             │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

### Goal Retrieval Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ User        │     │ Client      │     │ API request │     │ Server      │
│ requests    ├────►│ initiates   ├────►│ to /goals   ├────►│ processes   │
│ goals       │     │ fetch       │     │             │     │ request     │
└─────────────┘     └─────────────┘     └─────────────┘     └──────┬──────┘
                                                                   │
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌──────▼──────┐
│ Client      │     │ User sees   │     │ Response    │     │ Query       │
│ renders     │◄────┤ goals       │◄────┤ returned to │◄────┤ DynamoDB    │
│ goals       │     │             │     │ client      │     │             │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

## Data Models

### Goal Model

```
Goal {
  goalId: string (UUID)
  title: string
  description: string (optional)
  tags: string[]
  category: enum (from goal_category)
  status: enum (from status)
  priority: enum (from priority)
  isParent: boolean
  nextAction: boolean
  nextGoal: string (UUID, optional)
  framework: enum (from framework)
  lastProgress: date
}
```

## Future Architecture Considerations

1. **State Management Evolution**

    - As the application grows, consider implementing a more robust state management solution (Redux, Zustand, etc.)
    - Implement caching strategies for improved performance

2. **Authentication and Authorization**

    - Add user authentication for personalized experiences
    - Implement role-based access control if multi-user features are added

3. **Offline Capabilities**

    - Implement offline storage and synchronization
    - Use service workers for progressive web app capabilities

4. **Performance Optimizations**
    - Implement code splitting for faster initial load
    - Add pagination for large data sets
    - Consider implementing server-side rendering for improved SEO and performance
