# AWS Organizations Setup Guide

## Overview

AWS Organizations allows you to manage multiple AWS accounts under a single master (payer) account. This provides consolidated billing, centralized security policies, and better resource isolation.

## Creating an Organization

### Step 1: Enable AWS Organizations

1. Log into your master AWS account
2. Navigate to AWS Organizations service
3. Click "Create an organization"
4. Choose "All features" for full functionality
5. Your account becomes the Management Account

### Step 2: Create Organizational Units (OUs)

Organize accounts by purpose. A typical structure includes:

- Security OU
- Infrastructure OU
- Workloads OU (with Dev, Staging, and Prod sub-OUs)
- Sandbox OU

## Creating Member Accounts

### Method 1: Create New Accounts

1. In AWS Organizations console, click "Add an account"
2. Choose "Create account"
3. Provide account details:
   - Account name: Descriptive name (e.g., "dev-sandbox")
   - Email address: Unique email using aliases
   - IAM role name: (Optional) Cross-account access role
4. AWS creates the account and provides account ID

### Method 2: Invite Existing Accounts

1. Click "Add an account"
2. Choose "Invite account"
3. Enter the email address of the account to invite
4. The account owner accepts the invitation

## Email Alias Strategy

### Why Unique Emails Are Required

- Each AWS account requires a unique email address
- No email reuse across AWS accounts
- Required for account verification and recovery

### Practical Email Alias Solutions

#### Gmail/Google Workspace (+ Aliases)

Use the + symbol to create unique aliases that all deliver to your main inbox:

- your.email+aws-master@gmail.com (Management account)
- your.email+aws-security@gmail.com (Security account)
- your.email+aws-dev@gmail.com (Development account)
- your.email+aws-prod@gmail.com (Production account)
- your.email+aws-sandbox@gmail.com (Sandbox account)

Gmail ignores everything after the + symbol, so all emails come to your main inbox.

#### Outlook/Hotmail

Outlook also supports + aliasing in the same way as Gmail.

#### Custom Domain Aliases

If you have your own domain, you can create specific aliases:

- aws-master@yourdomain.com
- aws-dev@yourdomain.com
- aws-prod@yourdomain.com

## Best Practices

### 1. Account Structure

- Master Account: Only for billing and organization management
- Security Account: Centralized logging, security tools
- Shared Services: Common infrastructure (VPN, DNS, CI/CD)
- Workload Accounts: Per environment (dev, staging, prod) per project

### 2. Security

- Enable MFA on all root accounts immediately
- Use SCPs (Service Control Policies) to enforce guardrails
- Apply least privilege principles with IAM roles
- Never use root for daily operations

### 3. Cost Management

- Set up billing alerts in the master account
- Use cost allocation tags to track spending per project
- Implement budgets for each account/OU
- Monitor Cost Explorer regularly

### 4. Naming Conventions

Use consistent naming patterns:

- Account Naming: {company}-{env}-{purpose} (Example: acme-prod-ecommerce)
- Resource Tagging: Include project, environment, owner, and cost center tags

## Example Account Setup

Management & Core Accounts:

- your.email+aws-master@gmail.com (Billing & Org management)
- your.email+aws-security@gmail.com (Security tools & logging)
- your.email+aws-shared@gmail.com (Shared infrastructure)

Development Environments:

- your.email+aws-dev@gmail.com (Development workloads)
- your.email+aws-staging@gmail.com (Staging environment)
- your.email+aws-prod@gmail.com (Production workloads)

Learning & Sandbox:

- your.email+aws-sandbox@gmail.com (Personal experiments)

## Important Notes

- AWS Organizations is free - no additional cost for the service
- Free tier limits are shared across all accounts in the organization
- Consolidated billing provides volume discounts across all accounts
- SCPs (Service Control Policies) apply to all accounts in an OU for centralized governance

## Next Steps

1. Enable AWS Organizations in your master account
2. Create your first member account using email aliases
3. Set up basic SCPs for security guardrails
4. Configure Cost Explorer and billing alerts
5. Implement cross-account IAM roles for access

## Resources

- AWS Organizations Documentation
- Service Control Policies (SCPs) Guide
- AWS Control Tower (for enterprise setups)
