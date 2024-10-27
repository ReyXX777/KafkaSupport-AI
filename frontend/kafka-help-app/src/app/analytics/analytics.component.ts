import { Component, OnInit } from '@angular/core';
import { AnalyticsService } from '../services/analytics.service';
import { Chart, registerables } from 'chart.js';

interface Metric {
  title: string;
  value: string | number;
  description: string;
}

interface KafkaData {
  topic: string;
  messagesSent: number;
  messagesReceived: number;
  errors: number;
  timestamp: Date;
}

@Component({
  selector: 'app-analytics',
  templateUrl: './analytics.component.html',
  styleUrls: ['./analytics.component.css']
})
export class AnalyticsComponent implements OnInit {
  metrics: Metric[] = [];
  kafkaData: KafkaData[] = [];
  loading = true;
  messageRateChart: Chart | undefined;

  constructor(private analyticsService: AnalyticsService) {
    Chart.register(...registerables);
  }

  ngOnInit(): void {
    this.fetchSummaryMetrics();
    this.fetchKafkaData();
    this.initializeMessageRateChart();
  }

  private fetchSummaryMetrics(): void {
    this.analyticsService.getSummaryMetrics().subscribe({
      next: (data) => {
        this.metrics = data;
      },
      error: (error) => {
        console.error('Error fetching summary metrics:', error);
      }
    });
  }

  private fetchKafkaData(): void {
    this.loading = true;
    this.analyticsService.getKafkaData().subscribe({
      next: (data) => {
        this.kafkaData = data;
        this.loading = false;
        this.updateMessageRateChart(data);
      },
      error: (error) => {
        console.error('Error fetching Kafka data:', error);
        this.loading = false;
      }
    });
  }

  private initializeMessageRateChart(): void {
    const ctx = document.getElementById('messageRateChart') as HTMLCanvasElement;
    this.messageRateChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: [], // Will be populated dynamically
        datasets: [
          {
            label: 'Messages Sent',
            data: [],
            borderColor: 'blue',
            fill: false
          },
          {
            label: 'Messages Received',
            data: [],
            borderColor: 'green',
            fill: false
          }
        ]
      },
      options: {
        responsive: true,
        scales: {
          x: {
            title: {
              display: true,
              text: 'Time'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Message Count'
            }
          }
        }
      }
    });
  }

  private updateMessageRateChart(data: KafkaData[]): void {
    if (this.messageRateChart) {
      const timestamps = data.map(d => d.timestamp.toLocaleTimeString());
      const messagesSent = data.map(d => d.messagesSent);
      const messagesReceived = data.map(d => d.messagesReceived);

      this.messageRateChart.data.labels = timestamps;
      (this.messageRateChart.data.datasets[0].data as number[]) = messagesSent;
      (this.messageRateChart.data.datasets[1].data as number[]) = messagesReceived;

      this.messageRateChart.update();
    }
  }
}
