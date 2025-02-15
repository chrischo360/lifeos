import { Title, Container } from '@mantine/core';
import { GoalInput } from '../components/GoalInput';

export default function HomePage() {
  return (
    <Container>
      <Title mb="md">LifeOS</Title>
      <GoalInput />
    </Container>
  );
}
