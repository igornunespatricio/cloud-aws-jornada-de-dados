# Bastion Host

## Components & Flow

### 1. Bastion Host (Public Subnet)

- **Location**: Public subnet with internet gateway
- **Purpose**: SSH/RDP jump server
- **Access**: Only from authorized IPs via Security Groups
- **Role**: No direct S3 access

### 2. Private EC2 (Private Subnet)

- **Location**: Private subnet, no internet access
- **Access**: Only via Bastion host
- **S3 Access**: Through VPC Endpoint or NAT Gateway
- **Role**: Application server that needs S3 access

### 3. S3 Service

- **Access**: Restricted to Private EC2 via IAM Role & Bucket Policy
- **Network**: Accessed via S3 VPC Endpoint (recommended) or NAT Gateway

## Security Configuration

### Security Groups

- **Bastion SG**: Allow SSH (22) from specific IPs only
- **Private EC2 SG**: Allow SSH (22) from Bastion SG only

### IAM Roles

- **Bastion Role**: Minimal permissions (none for S3)
- **Private EC2 Role**: S3 read/write permissions as needed

### Network

- **NAT Gateway**: For Private EC2 to access S3 (if no VPC Endpoint)
- **S3 VPC Endpoint**: Preferred method for private S3 access

## Access Flow

1. User SSH → Bastion EC2 (with key)
2. Bastion EC2 → Private EC2 (SSH tunnel)
3. Private EC2 → S3 Bucket (via IAM role)
4. S3 responds → Private EC2 → User

## Key Points

- Only Private EC2 can access S3
- Bastion only provides access, no S3 permissions
- Complete network isolation for Private EC2
- S3 access stays within AWS network

![architecture](/class06/image.png)

_GitHub repository from course with details https://github.com/lvgalvao/data-engineering-roadmap/blob/main/Bootcamp%20-%20Cloud%20para%20dados/Aula_06/README.md_
