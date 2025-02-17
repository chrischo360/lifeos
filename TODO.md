# Frontend 
- Display Goals in a list format
- Display Goals in a tree format

# Backend
- Figure out schema for goals and relationships between goals
```
  # This can be just a string, but for now, a limited set and can be expanded by the user
  enum goal_category = {
    career,
    physical_health,
    mental_health,
    intellectual_growth,
    dating,
    finances,
    personal_development,
    friends,
    emotional_growth,
    family,
    spiritual_growth,
    travel,
    life
  }

  enum action_type = {
    vision,
    mindset,
    goal,
    action 
  }

  enum status = {
    standby,
    blocked,
    next_action,
    completed,
    archived
  }

  enum priority = {
    low,
    medium,
    high,
    critical
  }

  enum framework = {
    WOOP,
    SMART,
    System,
    BSQ,
    BHAG
  }
    
  goals = {
    goal_id: string;
    description: string;
    note: file<markdown>;
    category: goal_category[];
    status: status;
    is_parent: boolean;
    priority: priority;
    next_action: true;
    next_goal: goal_id;
    framework: framework;
    last_progress: date;
  }
```

# Dev Tools
