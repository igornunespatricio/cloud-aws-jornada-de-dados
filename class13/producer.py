import os
import boto3
import random
import time
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

QUEUE_URL = os.getenv("QUEUE_URL")
REGION = os.getenv("REGION")


class SQSMessageSender:
    def __init__(self, queue_url, region_name="us-east-1"):
        """
        Initialize SQS client

        Args:
            queue_url (str): The URL of your SQS queue
            region_name (str): AWS region name
        """
        self.sqs = boto3.client("sqs", region_name=region_name)
        self.queue_url = queue_url

    def generate_random_message(self):
        """Generate a random message with timestamp"""
        messages = [
            "Processing user registration request",
            "Order payment completed successfully",
            "Inventory update required for product",
            "Background task started for report generation",
            "Email notification queued for delivery",
            "Database backup initiated",
            "User session created successfully",
            "API rate limit check passed",
            "Cache refresh triggered",
            "Security scan completed",
            "File upload processing started",
            "Data synchronization in progress",
            "System health check performed",
            "Audit log entry created",
            "Performance metrics collected",
        ]

        message_template = random.choice(messages)
        timestamp = datetime.now().isoformat()

        message_body = {
            "message": message_template,
            "message_id": f"msg_{random.randint(1000, 9999)}",
            "timestamp": timestamp,
            "priority": random.choice(["low", "medium", "high"]),
            "processing_time": random.randint(100, 5000),
        }

        return message_body

    def send_message(self, message_body):
        """Send message to SQS queue"""
        try:
            response = self.sqs.send_message(
                QueueUrl=self.queue_url,
                MessageBody=json.dumps(message_body),
                MessageAttributes={
                    "Priority": {
                        "DataType": "String",
                        "StringValue": message_body["priority"],
                    },
                    "Timestamp": {
                        "DataType": "String",
                        "StringValue": message_body["timestamp"],
                    },
                },
            )
            print(
                f"✅ Message sent: {message_body['message']} (ID: {message_body['message_id']})"
            )
            print(f"   Message ID: {response['MessageId']}")
            return response
        except Exception as e:
            print(f"❌ Error sending message: {e}")
            return None

    def start_sending_messages(self, total_messages=20, min_delay=1, max_delay=10):
        """
        Start sending messages at random intervals

        Args:
            total_messages (int): Total number of messages to send
            min_delay (int): Minimum delay between messages in seconds
            max_delay (int): Maximum delay between messages in seconds
        """
        print(f"🚀 Starting to send {total_messages} messages to SQS queue...")
        print(f"📋 Queue URL: {self.queue_url}")
        print("-" * 50)

        sent_count = 0

        try:
            while sent_count < total_messages:
                # Generate and send message
                message = self.generate_random_message()
                self.send_message(message)
                sent_count += 1

                # Calculate random delay for next message
                if sent_count < total_messages:
                    delay = random.randint(min_delay, max_delay)
                    print(f"⏰ Waiting {delay} seconds before next message...\n")
                    time.sleep(delay)

        except KeyboardInterrupt:
            print("\n\n⏹️ Message sending interrupted by user")

        print(f"\n✅ Completed! Sent {sent_count} messages to SQS queue")


def main():

    # Create sender instance
    sender = SQSMessageSender(queue_url=QUEUE_URL, region_name=REGION)

    # Start sending messages
    sender.start_sending_messages(
        total_messages=100,  # Send 20 messages total
        min_delay=2,  # Minimum 2 seconds between messages
        max_delay=8,  # Maximum 8 seconds between messages
    )


if __name__ == "__main__":
    main()
