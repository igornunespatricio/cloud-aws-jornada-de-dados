# Event-Driven Architecture with AWS Lambda and S3

## Overview

This project demonstrates an event-driven architecture using AWS Lambda functions triggered by S3 events. When a file is uploaded to a source S3 bucket, it automatically triggers a Lambda function that copies the object to a destination S3 bucket.

## Architecture Components

- **Event Source**: S3 bucket upload operation
- **Event Bus**: AWS EventBridge (implicit)
- **Compute**: AWS Lambda function
- **Storage**: Two S3 buckets (source and destination)
- **Monitoring**: AWS CloudWatch Logs

## Prerequisites

- AWS CLI configured with appropriate permissions
- Basic understanding of IAM roles and policies

## Implementation Steps

### 1. Create S3 Buckets

Create both source and destination S3 buckets using AWS CLI or Console.

### 2. Create Lambda Function

Create a Python Lambda function that handles the S3 copy operation. The function will be triggered when objects are added to the source bucket.

### 3. Create Policy

Create an IAM role for Lambda with permissions to:

- Read from the source S3 bucket
- Write to the destination S3 bucket
- Write logs to CloudWatch

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:GetObjectVersion"],
      "Resource": "arn:aws:s3:::source-bucket-name/*"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject"],
      "Resource": "arn:aws:s3:::destination-bucket-name/*"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::source-bucket-name",
        "arn:aws:s3:::destination-bucket-name"
      ]
    }
  ]
}
```

This policy will need to be attached to the role created for the Lambda function.

### 4. Add trigger to Lambda function

Add trigger to lambda function when new file is added to source bucket.

### 5. Test the Implementation

Upload a CSV file to the source bucket and verify it gets copied to the destination bucket.

## Verification Steps

### 1. File Copy Verification

- List files in the destination bucket to confirm the copy operation
- Compare file contents between source and destination
- Verify file metadata and integrity

### 2. CloudWatch Logs Verification

- Check CloudWatch logs for the Lambda function execution
- Verify there are no errors in the log streams
- Confirm successful execution metrics
