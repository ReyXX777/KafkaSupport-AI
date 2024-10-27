export const environment = {
  production: true,
  apiUrl: 'https://api.kafkasupport-ai.com/v1',
  kafkaConfig: {
    brokerUrl: 'https://broker.kafkasupport-ai.com',
    clientId: 'kafka-help-app-client',
    defaultTopic: 'kafka-support-topic'
  },
  logging: {
    level: 'error',  // Adjust the logging level for production, e.g., 'error' or 'warn'
    enableConsole: false  // Disable console logs for production
  },
  featureFlags: {
    enableAdvancedKafkaMetrics: true,
    enableUserFeedback: true
  }
};
