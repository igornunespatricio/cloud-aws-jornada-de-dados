# S3 Commands

```bash
aws s3 ls # List all buckets
aws s3 ls s3://bucket-name/ # List bucket contents
aws s3 cp file.txt s3://bucket-name/ # Upload file
aws s3 sync ./local-folder s3://bucket-name/ # Sync folder to S3
aws s3 rm s3://bucket-name/file.txt # Delete file
aws s3 mb s3://new-bucket-name # Create bucket
```

# Lambda Commands

```bash
aws lambda list-functions # List all functions
aws lambda get-function --function-name my-function # Get function details
aws lambda invoke --function-name my-function output.json # Invoke function
aws lambda update-function-code --function-name my-function --zip-file fileb://deploy.zip # Update code
```

# IAM Commands

```bash
aws iam list-users # List IAM users
aws iam list-roles # List IAM roles
aws iam attach-role-policy --role-name my-role --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess # Attach policy
```

# API Gateway Commands

```bash
aws apigateway get-rest-apis # List REST APIs
aws apigateway get-resources --rest-api-id api-id # List API resources
```

# CloudWatch Logs

```bash
aws logs describe-log-groups # List log groups
aws logs filter-log-events --log-group-name /aws/lambda/my-function --start-time 2024-01-01T00:00:00Z # View logs
```

# General Useful Commands

```bash
aws sts get-caller-identity # Show current AWS identity
aws configure list # Show AWS configuration
aws --version # Check AWS CLI version
```

# RDS

```bash
aws rds describe-db-instances
```
