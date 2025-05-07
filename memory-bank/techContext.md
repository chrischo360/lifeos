# Technical Context: LifeOS

## Technologies Used

### Frontend

1. **Next.js**

    - Version: Latest stable (as of project start)
    - Purpose: React framework for building the user interface
    - Key features used:
        - File-based routing
        - TypeScript integration
        - API routes
        - Server-side rendering capabilities

2. **React**

    - Version: Compatible with Next.js version
    - Purpose: UI component library
    - Key features used:
        - Functional components
        - React Hooks (useState, useEffect, etc.)
        - Context API (potential future use)

3. **TypeScript**

    - Version: Latest stable (as of project start)
    - Purpose: Type safety and improved developer experience
    - Key features used:
        - Interfaces for data models
        - Type checking for component props
        - Type definitions for API responses

4. **Mantine UI**
    - Version: Latest stable (as of project start)
    - Purpose: Component library for UI elements
    - Key features used:
        - Form components (TextInput, Textarea, Button, etc.)
        - Layout components (Container, Group, etc.)
        - Theming capabilities

### Backend

1. **Python**

    - Version: 3.9+
    - Purpose: Server-side logic and API endpoints
    - Key features used:
        - Type hints
        - Modern Python syntax
        - AWS SDK integration

2. **AWS Chalice**

    - Version: Latest stable (as of project start)
    - Purpose: Serverless framework for Python
    - Key features used:
        - API routing
        - AWS resource management
        - CORS configuration
        - Error handling

3. **AWS Services**
    - **DynamoDB**: NoSQL database for storing goal data
    - **Lambda**: Serverless compute for API handlers
    - **API Gateway**: HTTP endpoint management
    - **IAM**: Security and access control
    - **CloudWatch**: Monitoring and logging

## Development Setup

### Local Environment Requirements

1. **Node.js and npm/yarn**

    - Required for frontend development
    - Recommended version: Latest LTS
    - Package manager preference: yarn

2. **Python and pipenv**

    - Required for backend development
    - Python version: 3.9+
    - Virtual environment management: pipenv

3. **AWS CLI**

    - Required for backend deployment and local testing
    - Configuration:
        - Credentials stored in `~/.aws/credentials`
        - Region configuration in `~/.aws/config`

4. **Code Editor**
    - Recommended: Visual Studio Code
    - Useful extensions:
        - ESLint
        - Prettier
        - Python
        - TypeScript
        - AWS Toolkit

### Development Workflow

1. **Frontend Development**

    - Start development server: `cd client && yarn run dev`
    - Server runs on: `http://localhost:3000`
    - Build for production: `yarn build`

2. **Backend Development**

    - Start local API server: `cd server && pipenv shell && chalice local`
    - Server runs on: `http://localhost:8000`
    - Deploy to AWS: `chalice deploy`

3. **Full-Stack Testing**
    - Run frontend and backend servers simultaneously
    - Frontend configured to connect to local backend by default
    - Test API endpoints using browser or tools like Postman

## Technical Constraints

1. **Frontend Constraints**

    - Browser compatibility: Modern browsers only (Chrome, Firefox, Safari, Edge)
    - Mobile responsiveness: Required for all views
    - Accessibility: Must meet WCAG 2.1 AA standards
    - Performance: Initial load under 2 seconds on broadband

2. **Backend Constraints**

    - API response time: Under 300ms for standard operations
    - Serverless architecture: Functions must complete within AWS Lambda limits
    - DynamoDB throughput: Consider provisioned capacity for consistent performance
    - AWS region: us-east-1 (North Virginia)

3. **Data Constraints**
    - Goal limit: No hard limit, but UI optimized for dozens to hundreds of goals
    - Text field limits: Title (100 chars), Description (1000 chars)
    - Tags: Maximum 10 tags per goal
    - API payload size: Under 6MB (AWS API Gateway limit)

## Dependencies

### Frontend Dependencies

```
// Core dependencies
"next": "^13.0.0",
"react": "^18.2.0",
"react-dom": "^18.2.0",
"typescript": "^4.8.4",

// UI dependencies
"@mantine/core": "^5.8.0",
"@mantine/hooks": "^5.8.0",
"@mantine/form": "^5.8.0",

// Development dependencies
"eslint": "^8.26.0",
"prettier": "^2.7.1",
"@types/react": "^18.0.24",
"@types/node": "^18.11.9"
```

### Backend Dependencies

```
# Core dependencies
chalice==1.27.1
boto3==1.24.71
pydantic==1.10.2

# Development dependencies
pytest==7.2.0
mypy==0.982
black==22.10.0
```

## Tool Usage Patterns

### Code Organization

1. **Frontend Structure**

    ```
    client/
    ├── public/            # Static assets
    ├── src/
    │   ├── components/    # Reusable UI components
    │   ├── pages/         # Next.js pages
    │   ├── styles/        # Global styles
    │   ├── types/         # TypeScript type definitions
    │   ├── utils/         # Utility functions
    │   └── api/           # API client functions
    ├── next.config.js     # Next.js configuration
    ├── tsconfig.json      # TypeScript configuration
    └── package.json       # Dependencies and scripts
    ```

2. **Backend Structure**
    ```
    server/
    ├── app.py             # Main Chalice application
    ├── chalicelib/        # Supporting modules
    │   ├── models.py      # Data models
    │   ├── services.py    # Business logic
    │   └── utils.py       # Utility functions
    ├── .chalice/          # Chalice configuration
    │   └── config.json    # AWS deployment settings
    ├── requirements.txt   # Python dependencies
    └── Pipfile            # Pipenv configuration
    ```

### Coding Standards

1. **TypeScript/JavaScript**

    - Use TypeScript for all new code
    - Follow ESLint configuration
    - Format with Prettier
    - Use functional components with hooks
    - Prefer explicit typing over `any`

2. **Python**

    - Follow PEP 8 style guide
    - Use type hints
    - Format with Black
    - Use meaningful docstrings
    - Write unit tests for critical functions

3. **API Design**
    - RESTful endpoints
    - JSON request/response format
    - Consistent error handling
    - Proper HTTP status codes
    - CORS configuration for local development

### Testing Approach

1. **Frontend Testing**

    - Component testing with React Testing Library
    - End-to-end testing with Cypress (future)
    - Manual testing of UI flows

2. **Backend Testing**
    - Unit testing with pytest
    - API testing with requests library
    - Local testing with chalice local
    - AWS integration testing after deployment

## Deployment Process

1. **Frontend Deployment**

    - Build Next.js application: `yarn build`
    - Deploy to hosting service (AWS S3, Vercel, etc.)
    - Configure environment variables for production API endpoints

2. **Backend Deployment**

    - Deploy to AWS using Chalice: `chalice deploy`
    - Chalice automatically provisions required AWS resources
    - Update frontend configuration to point to new API endpoints

3. **Database Management**
    - DynamoDB tables created through AWS CloudFormation (managed by Chalice)
    - Backup strategy: Point-in-time recovery enabled
    - Schema evolution: Handle in application code due to schemaless nature

## Monitoring and Maintenance

1. **Frontend Monitoring**

    - Error tracking with browser console logging (future: dedicated error tracking service)
    - Performance monitoring through browser developer tools
    - User behavior analytics (future)

2. **Backend Monitoring**

    - AWS CloudWatch for logs and metrics
    - Lambda function performance monitoring
    - DynamoDB throughput and capacity monitoring
    - API Gateway request/response monitoring

3. **Maintenance Tasks**
    - Regular dependency updates
    - Security patches
    - Performance optimization
    - Feature enhancements based on user feedback
