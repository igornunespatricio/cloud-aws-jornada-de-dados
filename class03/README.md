# 🚀 Airflow Bootcamp: Cloud Data Engineering Setup Guide

A comprehensive, step-by-step guide to deploy Apache Airflow on AWS EC2 and build your first data pipeline in the cloud.

Reference: https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Cloud%20para%20dados/Aula_03

---

## 📋 Prerequisites

Before you begin, ensure you have:

- An AWS account with EC2 access
- Basic terminal/command line knowledge
- A text editor or IDE (VS Code recommended)

---

## 🖥️ Step 1: Launch Your EC2 Instance

1. **Navigate to AWS EC2 Console**
2. **Launch Instance** with the following configuration:
   - **AMI**: Ubuntu Server 22.04 LTS (Recommended)
   - **Instance Type**: t2.micro (Free tier eligible)
   - **Key Pair**: Create new or use existing `.pem` file
   - **Security Groups**: Ensure SSH access (port 22) is enabled

---

## 🔐 Step 2: Configure Security Groups

**Add Airflow Web UI Access:**

- Go to **Security Groups** → Edit **Inbound Rules**
- **Add Rule**:
  - Type: `Custom TCP`
  - Port Range: `8080`
  - Source: `0.0.0.0/0` (or restrict to your IP for security)

---

## ⚡ Step 3: Connect & Setup Environment

### Connect via SSH:

Navigate to folder containing your `.pem` file and connect using SSH with your key pair.

### System Setup:

Update system packages and install essential dependencies including Python, pip, SQLite, virtual environment, and PostgreSQL development libraries. Commands below:

```bash
sudo apt update
sudo apt upgrade -y
```

```bash
sudo apt install -y python3-pip
```

```bash
sudo apt install -y sqlite3
```

```bash
sudo apt install -y python3.12-venv
```

```bash
sudo apt-get install -y libpq-dev
```

---

## 🐍 Step 4: Install Apache Airflow

### Create Virtual Environment:

Set up a Python virtual environment to isolate your Airflow installation.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Airflow with Constraints:

Install Apache Airflow version 2.10.0 with Celery executor using the official constraints file to ensure compatibility.

```bash
pip install "apache-airflow[celery]==2.10.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.0/constraints-3.8.txt"
```

---

## 🗄️ Step 5: Configure Airflow

### Initialize Database:

Run database migration to set up Airflow's metadata database.

### Create Admin User:

Create your first Airflow administrator account with superuser privileges.

```bash
airflow db migrate
```

```bash
airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org
```

\*_input password when asked_

---

## 🚀 Step 6: Start Airflow Services

### Launch Webserver:

Start the Airflow webserver in background mode to serve the web interface.

```bash
airflow webserver &
```

### Launch Scheduler:

Start the Airflow scheduler in background mode to execute and monitor your workflows.

```bash
airflow scheduler &
```

---

## 🌐 Step 7: Access Airflow Web UI

1. **Copy your EC2 Public DNS** from AWS Console
2. **Open browser** and navigate to your instance on port 8080. Link should be something like 'http://{your public dns}:8080'
3. **Login** with the admin credentials you created

---

## 💻 Step 8: VS Code Remote Development

### Install Remote SSH Extension:

Add the Remote SSH extension to VS Code for seamless remote development.

### Configure SSH Connection:

Edit your SSH config file to add your EC2 instance as a remote host.

The path to the config file should be something like this: "c:/Users/{username}/.ssh/config". You can open it in vs code and add the following:

```text
Host {copy public dns}
    HostName {copy public dns}
    User ubuntu
    IdentityFile path to downloaded .pem file
```

### Connect to Remote Instance:

Use VS Code's Remote Explorer to connect to your EC2 instance using the SSH and open the Airflow directory.

---

## 📁 Step 9: Create Your First DAG

### Navigate to DAGs Folder:

Create and access the `airflow/dags` directory in your remote VS Code session.

### Create Your First DAG:

Build a simple DAG file that defines your data pipeline workflow with a start task.

my_dag.py

```python
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 26),
}

with DAG('my_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    start = DummyOperator(task_id='start')

    start
```

### Verify in Airflow UI:

Your new DAG should appear in the Airflow web interface within seconds, ready to be triggered and monitored.

---

## 🎯 Next Steps

- Explore Airflow operators for different data sources
- Set up connections to databases and cloud services
- Learn about scheduling and dependencies
- Monitor and troubleshoot your data pipelines

---

## ⚠️ Troubleshooting Tips

- **Port 8080 not accessible**: Double-check security group inbound rules
- **Airflow commands not found**: Ensure virtual environment is activated
- **DAGs not appearing**: Verify scheduler is running and check logs
- **Connection issues**: Validate SSH key permissions and instance status

---

## 📚 Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [VS Code Remote Development](https://code.visualstudio.com/docs/remote/ssh)

**Happy data engineering! 🎉**
