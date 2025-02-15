import React, { useState } from 'react';
import { TextInput, Textarea, Button, Group, Box, TagsInput } from '@mantine/core';

interface Goal {
  id?: string;
  title: string;
  description: string;
  tags: string[];
}

export function GoalInput() {
  const [goal, setGoal] = useState<Goal>({
    title: '',
    description: '',
    tags: []
  });

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/goal', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(goal)
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log('Goal created:', data);
      // Reset form or show success message
      setGoal({ title: '', description: '', tags: [] });
    } catch (error) {
      console.error('Error creating goal:', error);
      // Handle error (show error message, etc.)
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit}>
      <TextInput
        label="Goal Title"
        value={goal.title}
        onChange={(event) => setGoal((prev) => ({ ...prev, title: event.target.value }))}
        required
      />
      <Textarea
        label="Goal Description"
        value={goal.description}
        onChange={(event) => setGoal((prev) => ({ ...prev, description: event.target.value }))}
        minRows={3}
      />
      <TagsInput
        label="Tags"
        value={goal.tags}
        onChange={(tags) => setGoal((prev) => ({ ...prev, tags }))}
        placeholder="Add tags"
      />
      <Group justify="flex-end" mt="md">
        <Button type="submit">Create Goal</Button>
      </Group>
    </Box>
  );
}
