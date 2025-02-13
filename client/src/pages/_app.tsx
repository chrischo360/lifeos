import '@mantine/core/styles.css';
import type { AppProps } from 'next/app';
import { AppShell, MantineProvider, Container } from '@mantine/core';
import Head from 'next/head';
import { theme } from '../../theme';

export default function App({ Component, pageProps }: AppProps) {
  return (
    <MantineProvider theme={theme}>
      <Head>
        <title>LifeOS Client</title>
        <meta
          name="viewport"
          content="minimum-scale=1, initial-scale=1, width=device-width, user-scalable=no"
        />
        <link rel="shortcut icon" href="/favicon.svg" />
      </Head>
      <AppShell
        header={{
          height: 60,
          collapsed: false,
          offset: true
        }}
        footer={{ height: 60 }}
        padding="md"
      >
        <AppShell.Header>
          <></>
        </AppShell.Header>
        <AppShell.Main>
          <Container size="sm" py="xl">
            <Component {...pageProps} />
          </Container>
        </AppShell.Main>
        <AppShell.Footer />
      </AppShell>
    </MantineProvider>
  );
}
