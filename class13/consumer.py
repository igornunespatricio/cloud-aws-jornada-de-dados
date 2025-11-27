import os
import boto3
import json
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

QUEUE_URL = os.getenv("QUEUE_URL")
REGION = os.getenv("REGION")


class SQSConsumer:
    def __init__(self, queue_url, region_name="us-east-1"):
        """
        Initialize SQS client

        Args:
            queue_url (str): The URL of your SQS queue
            region_name (str): AWS region name
        """
        self.sqs = boto3.client("sqs", region_name=region_name)
        self.queue_url = queue_url

    def process_message(self, message):
        """
        Process a single message from SQS

        Args:
            message (dict): The SQS message object

        Returns:
            bool: True if message was processed successfully, False otherwise
        """
        try:
            # Extract message body and receipt handle
            body = json.loads(message["Body"])
            receipt_handle = message["ReceiptHandle"]

            # Print message details
            print(f"📨 Received message:")
            print(f"   Message ID: {message['MessageId']}")
            print(f"   Content: {body['message']}")
            print(f"   Priority: {body['priority']}")
            print(f"   Timestamp: {body['timestamp']}")
            print(f"   Processing Time: {body['processing_time']}ms")

            # Simulate message processing
            print(f"   🔄 Processing message...")
            time.sleep(random.uniform(0.1, 0.5))  # Simulate processing time

            # Delete the message from queue after successful processing
            self.delete_message(receipt_handle)
            print(f"   ✅ Message processed and deleted successfully")
            print("-" * 50)

            return True

        except Exception as e:
            print(f"   ❌ Error processing message: {e}")
            return False

    def delete_message(self, receipt_handle):
        """
        Delete a message from SQS queue

        Args:
            receipt_handle (str): The receipt handle of the message to delete
        """
        try:
            self.sqs.delete_message(
                QueueUrl=self.queue_url, ReceiptHandle=receipt_handle
            )
        except Exception as e:
            print(f"   ❌ Error deleting message: {e}")
            raise

    def poll_messages(self, max_messages=10, wait_time=20, poll_interval=5):
        """
        Continuously poll SQS for messages

        Args:
            max_messages (int): Maximum number of messages to retrieve per request (1-10)
            wait_time (int): Long polling wait time in seconds (0-20)
            poll_interval (int): Time to wait between polling attempts in seconds
        """
        print(f"👂 Starting to poll SQS queue for messages...")
        print(f"📋 Queue URL: {self.queue_url}")
        print(f"⏰ Poll interval: {poll_interval} seconds")
        print(f"📦 Max messages per request: {max_messages}")
        print("-" * 50)

        processed_count = 0
        empty_polls = 0

        try:
            while True:
                # Receive messages from SQS
                response = self.sqs.receive_message(
                    QueueUrl=self.queue_url,
                    MaxNumberOfMessages=max_messages,
                    WaitTimeSeconds=wait_time,
                    MessageAttributeNames=["All"],
                )

                messages = response.get("Messages", [])

                if messages:
                    empty_polls = 0  # Reset empty poll counter
                    print(f"🎯 Found {len(messages)} message(s) to process")

                    for message in messages:
                        success = self.process_message(message)
                        if success:
                            processed_count += 1

                    print(f"📊 Total messages processed: {processed_count}")

                else:
                    empty_polls += 1
                    print(f"⏳ No messages available (Empty poll #{empty_polls})")
                    print(f"🔄 Waiting {poll_interval} seconds before next poll...")
                    time.sleep(poll_interval)

                    # Optional: Stop after too many empty polls
                    if empty_polls >= 10:
                        print(
                            "🛑 No messages received for 10 consecutive polls. Stopping..."
                        )
                        break

        except KeyboardInterrupt:
            print(f"\n\n⏹️ Consumer stopped by user")

        except Exception as e:
            print(f"\n❌ Error in polling: {e}")

        finally:
            print(f"\n📈 Summary: Processed {processed_count} messages total")

    def process_single_batch(self, max_messages=10, wait_time=20):
        """
        Process a single batch of messages and then stop

        Args:
            max_messages (int): Maximum number of messages to retrieve
            wait_time (int): Long polling wait time in seconds
        """
        print(f"🔄 Processing single batch of messages...")

        try:
            response = self.sqs.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=max_messages,
                WaitTimeSeconds=wait_time,
                MessageAttributeNames=["All"],
            )

            messages = response.get("Messages", [])

            if not messages:
                print("📭 No messages available in queue")
                return

            print(f"🎯 Processing {len(messages)} message(s)")

            for message in messages:
                self.process_message(message)

        except Exception as e:
            print(f"❌ Error processing batch: {e}")


def main():
    # Create consumer instance
    consumer = SQSConsumer(queue_url=QUEUE_URL, region_name=REGION)

    # Choose one of the following modes:

    # Mode 1: Continuous polling (runs until stopped)
    print("Select operation mode:")
    print("1. Continuous polling (runs until Ctrl+C)")
    print("2. Single batch processing")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "2":
        consumer.process_single_batch(
            max_messages=10,  # Process up to 10 messages at once
            wait_time=20,  # Long polling wait time
        )
    else:
        # Default: Continuous polling
        consumer.poll_messages(
            max_messages=10,  # Process up to 10 messages at once
            wait_time=20,  # Long polling wait time
            poll_interval=5,  # Wait 5 seconds between polls when queue is empty
        )


if __name__ == "__main__":
    # Add random for processing simulation
    import random

    main()
