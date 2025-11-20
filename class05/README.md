## VPC Summary

A **Virtual Private Cloud (VPC)** is your isolated network in AWS. Think of it as your private data center within AWS cloud.

---

## Key Components & Examples

### **Public Subnet**

- **Has route to Internet Gateway** (`0.0.0.0/0 → igw-xxxx`)
- **Use Case:** Resources needing direct internet access
- **Examples:**
  - Web servers facing users
  - Load Balancers
  - NAT Gateways

### **Private Subnet**

- **NO route to Internet Gateway**
- **Use Case:** Backend resources, databases
- **Examples:**
  - Database servers (RDS, EC2 with MySQL)
  - Application servers
  - Internal microservices

### **NAT Gateway**

- **Purpose:** Allows private subnets to initiate outbound internet connections
- **Lives in:** Public subnet
- **Example:**
  - EC2 in private subnet needs to download security patches → traffic goes through NAT Gateway in public subnet

### **VPC Endpoint**

- **Purpose:** Private connection to AWS services (bypasses internet)
- **Types:** Gateway (S3, DynamoDB) & Interface (all other AWS services)
- **Example:**
  - EC2 in private subnet needs to read from S3 bucket → use VPC Endpoint for S3 (no NAT Gateway needed)

_Full details can be found at the course's github repository https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Cloud%20para%20dados/Aula_05_
