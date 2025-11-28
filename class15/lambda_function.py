import json
import boto3
from datetime import datetime
import os

TABLE_NAME = os.environ.get("TABLE_NAME")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    value = body.get("value")
    if not value:
        return {"statusCode": 400, "body": json.dumps({"message": "Value is required"})}

    item = {"id": str(int(datetime.utcnow().timestamp() * 1000)), "value": value}

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Value added successfully!", "item": item}),
    }
