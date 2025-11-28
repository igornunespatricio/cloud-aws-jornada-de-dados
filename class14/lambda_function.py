import json
import boto3
import uuid
from datetime import datetime

s3 = boto3.client("s3")

BUCKET_NAME = "user-data-bucket-97346534"  # Replace with your bucket name


def lambda_handler(event, context):
    """
    Process SNS messages and store them in S3
    """
    try:
        # Process each SNS record
        for record in event["Records"]:
            # Extract SNS message
            sns_message = record["Sns"]
            message_id = sns_message["MessageId"]
            message = sns_message["Message"]
            timestamp = sns_message["Timestamp"]

            # Parse the JSON message
            user_data = json.loads(message)

            # Add metadata
            processed_data = {
                "message_id": message_id,
                "processing_timestamp": datetime.utcnow().isoformat(),
                "received_timestamp": timestamp,
                "user_data": user_data,
            }

            # Create S3 key with timestamp and unique ID
            s3_key = (
                f"user-data/{datetime.utcnow().strftime('%Y/%m/%d')}/{message_id}.json"
            )

            # Upload to S3
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=s3_key,
                Body=json.dumps(processed_data, indent=2),
                ContentType="application/json",
            )

            print(f"Successfully stored message {message_id} in S3: {s3_key}")

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "Successfully processed SNS messages",
                    "processed_count": len(event["Records"]),
                }
            ),
        }

    except Exception as e:
        print(f"Error processing SNS message: {e}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
