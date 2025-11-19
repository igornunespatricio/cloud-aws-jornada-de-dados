## Why Use an IAM Role with EC2?

### Security

- **Eliminates embedded credentials**: Avoids storing AWS credentials directly on the instance, which could be compromised
- **Temporary credentials**: Uses automatically rotated temporary security credentials instead of long-term access keys
- **Reduced exposure**: No sensitive access keys stored in configuration files or environment variables

### Simplified Management

- **Centralized permissions**: Permissions are managed centrally in the IAM role and can be adjusted without modifying instance configuration
- **No credential distribution**: No need to distribute and rotate access keys across multiple instances
- **Unified policy management**: Apply consistent permissions across fleets of EC2 instances

### Automation & Scalability

- **Seamless scaling**: New instances automatically inherit the appropriate permissions when launched with the same role
- **Environment consistency**: Ensures consistent access patterns across development, staging, and production environments
- **Easy maintenance**: Permission changes apply to all instances using the role without manual intervention

### Operational Benefits

- **Dynamic credential rotation**: AWS automatically handles credential rotation in the background
- **Service-specific access**: Roles can be tailored to provide least-privilege access for specific workloads
- **Audit trail**: Clear visibility into which roles are assigned to which instances

This is a common and crucial pattern in cloud projects where security and manageability are essential for successful infrastructure maintenance and operations.

See repository of class below for full details

https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Cloud%20para%20dados/Aula_04
