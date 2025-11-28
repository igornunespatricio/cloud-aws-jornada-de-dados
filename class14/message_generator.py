import os
import boto3
import json
import random
import time
from faker import Faker
from dotenv import load_dotenv

load_dotenv()

TOPIC_ARN = os.getenv("TOPIC_ARN")

# Initialize Faker for random data
fake = Faker()


def generate_random_user():
    """Generate random user data"""
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "cellphone": fake.phone_number(),
    }


def send_random_message():
    """Send random message to SNS topic"""
    sns = boto3.client("sns")

    user_data = generate_random_user()

    response = sns.publish(
        TopicArn=TOPIC_ARN, Message=json.dumps(user_data), Subject="Random User Data"
    )

    print(f"Sent message: {user_data}")
    print(f"Message ID: {response['MessageId']}")
    return response


def main():
    """Send random messages at random intervals"""
    while True:
        try:
            send_random_message()
            # Wait random time between 10-60 seconds
            sleep_time = random.randint(10, 60)
            print(f"Waiting {sleep_time} seconds...")
            time.sleep(sleep_time)
        except KeyboardInterrupt:
            print("Stopped by user")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(30)


if __name__ == "__main__":
    main()
