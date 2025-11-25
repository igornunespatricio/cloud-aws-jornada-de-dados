import json
import boto3
import urllib.parse


def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client("s3")

    # Bucket names - make sure these are correct
    source_bucket = "raw-test-bucket-8623543"
    destination_bucket = "silver-test-bucket-743653485"

    print(f"Processing event for source bucket: {source_bucket}")

    try:
        for record in event["Records"]:
            # Get the bucket name and object key from the event
            event_bucket = record["s3"]["bucket"]["name"]
            object_key = urllib.parse.unquote_plus(
                record["s3"]["object"]["key"], encoding="utf-8"
            )

            print(f"Event received - Bucket: {event_bucket}, Key: {object_key}")

            # Verify the event came from the correct source bucket
            if event_bucket != source_bucket:
                print(
                    f"Warning: Event from unexpected bucket: {event_bucket}. Expected: {source_bucket}"
                )
                continue

            print(
                f"Copying object: {object_key} from {source_bucket} to {destination_bucket}"
            )

            # Copy the object to destination bucket
            copy_source = {"Bucket": source_bucket, "Key": object_key}

            try:
                # Perform the copy operation
                response = s3.copy_object(
                    Bucket=destination_bucket, Key=object_key, CopySource=copy_source
                )

                print(f"Successfully copied {object_key} to {destination_bucket}")
                print(
                    f"Copy response: {response['ResponseMetadata']['HTTPStatusCode']}"
                )

            except Exception as copy_error:
                print(f"Error during copy operation: {str(copy_error)}")
                raise copy_error

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "File copied successfully",
                    "source_bucket": source_bucket,
                    "destination_bucket": destination_bucket,
                }
            ),
        }

    except Exception as e:
        error_msg = f"Error processing file: {str(e)}"
        print(error_msg)

        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to copy file", "message": str(e)}),
        }
