export const environment = {
  production: false,
  apiUrl: 'http://localhost:3000/v1',
  kafkaConfig: {
    brokerUrl: 'http://localhost:9092',
    clientId: 'kafka-help-app-client-dev',
    defaultTopic: 'kafka-support-topic-dev'
  },
  logging: {
    level: 'debug',  // Set to 'debug' for more verbose logging in development
    enableConsole: true  // Enable console logs to assist with debugging
  },
  featureFlags: {
    enableAdvancedKafkaMetrics: false,  // May disable in dev for performance
    enableUserFeedback: true
  }
};
