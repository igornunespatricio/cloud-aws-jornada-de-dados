# API Scheduler for Cryptocurrency Data

This project sets up a data pipeline to fetch cryptocurrency data from CoinMarketCap API and store it in a PostgreSQL database on AWS.

## Class Details

- **Link for class details**: [Bootcamp - Cloud para dados - Aula 08](https://github.com/lvgalvao/data-engineering-roadmap/blob/main/Bootcamp%20-%20Cloud%20para%20dados/Aula_08/README.md)
- **API Documentation**: [CoinMarketCap API v1](https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyQuotesLatest)
- **Project Repository**: [api-scheduler-python-rds](https://github.com/lvgalvao/api-scheduler-python-rds)

## Prerequisites

- AWS Account with appropriate permissions
- CoinMarketCap API account (Sign up here: https://coinmarketcap.com/api/)

## Setup Steps

### 1. Create VPC

Use the provided script to create the VPC infrastructure:

```text
./class08/scripts/create_vpc.sh
```

### 2. Create RDS PostgreSQL Instance

- Launch an RDS PostgreSQL instance in the created VPC
- Note down the database endpoint, username, and password
- Default database name: `project`

### 3. Create EC2 Instance

- Launch an EC2 instance with Linux AMI
- Ensure it's in the same VPC as the RDS instance
- Appropriate instance type (t2.micro or larger)
- **Important**: Create or select a key pair during EC2 instance creation and download the .pem file
- Move the downloaded .pem key file to your project root directory for SSH access

### 4. Configure Security Groups

**Critical Step**: Add inbound rule in RDS security group to allow connections from EC2 security group:

- **Type**: PostgreSQL
- **Port**: 5432
- **Source**: EC2 instance's security group ID

### 5. Get CoinMarketCap API Key

1. Create an account at CoinMarketCap API: https://coinmarketcap.com/api/
2. Verify your account and generate an API key
3. Use the generated API key as the value for `CMC_API_KEY` environment variable

### 6. Connect to EC2 and Deploy Application

SSH into your EC2 instance using the key pair:
ssh -i your-key-pair.pem ec2-user@your-ec2-public-ip

Once connected to the EC2 instance, run the following commands:

```bash
sudo su
sudo apt-get update
sudo apt install -y git docker.io docker-compose
git clone https://github.com/lvgalvao/api-scheduler-python-rds.git /app
cd /app
sudo docker build -t api-schedule-app .
docker run -d \
 --name api-schedule-app-container \
 -e DB_HOST=YOUR_RDS_ENDPOINT_HERE \
 -e DB_USER=YOUR_DATABASE_USERNAME_HERE \
 -e DB_PASS=YOUR_DATABASE_PASSWORD_HERE \
 -e DB_NAME=YOUR_DATABASE_NAME_HERE \
 -e CMC_API_KEY=YOUR_CMC_API_KEY_HERE \
 api-schedule-app
```

## Environment Variables

Replace the following placeholders in the `docker run` command:

- `YOUR_RDS_ENDPOINT_HERE`: Your RDS instance endpoint (e.g., `project-rds-ec2-db.region.rds.amazonaws.com`)
- `YOUR_DATABASE_USERNAME_HERE`: Database username (default: `postgres`)
- `YOUR_DATABASE_PASSWORD_HERE`: Database password you set during RDS creation
- `YOUR_DATABASE_NAME_HERE`: Database name (default: `project`)
- `YOUR_CMC_API_KEY_HERE`: Your CoinMarketCap API key

## Verification

Check if the container is running properly:
docker ps
docker logs api-schedule-app-container

## Data Verification

To verify that the data is being successfully inserted into the database:

1. Connect to your RDS PostgreSQL database using a database client (such as pgAdmin, DBeaver, or psql command line)
2. Run the query from the project scripts to check the inserted data:

```txt
class08/scripts/query.sql

```

This will confirm that the cryptocurrency data is being properly fetched from the API and stored in the database.

## Troubleshooting

- Ensure RDS security group allows inbound connections from EC2 security group
- Verify all environment variables are set correctly
- Check Docker container logs for any errors
- Confirm CoinMarketCap API key is valid and has appropriate permissions
- Ensure SSH key file has correct permissions: chmod 400 your-key-pair.pem

## Project Structure

The application automatically:

- Connects to the PostgreSQL database
- Fetches cryptocurrency data from CoinMarketCap API
- Stores the data in the database
- Runs on a scheduled basis (configurable)

```

```
