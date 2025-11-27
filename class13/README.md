# Amazon SQS (Simple Queue Service)

## Overview

Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message-oriented middleware.

## Key Concepts

### Queue Types

- **Standard Queues**: Unlimited throughput, best-effort ordering, and at-least-once delivery
- **FIFO Queues**: Exactly-once processing, first-in-first-out delivery, and limited throughput

### Core Components

- **Messages**: Data up to 256KB containing the information you want to transmit
- **Producers**: Applications that send messages to queues
- **Consumers**: Applications that receive and process messages from queues

## How It Works

1. Producers send messages to SQS queues
2. Messages are stored redundantly across multiple availability zones
3. Consumers poll queues and process messages
4. After successful processing, consumers delete messages from the queue

## Common Use Cases

- Decouple application components
- Buffer and batch work items
- Handle spikes in workload
- Orchestrate microservices
- Distribute tasks across worker nodes

## Benefits

- Fully managed service (no infrastructure to manage)
- Highly scalable and reliable
- Secure (encryption at rest and in transit)
- Cost-effective (pay only for what you use)
- Integrates seamlessly with other AWS services

## Example

Create queue (default type is Standard)

```bash
aws sqs create-queue --queue-name my-queue
```

Create FIFO queue

```bash
aws sqs create-queue --queue-name minha-fila.fifo --attributes FifoQueue=true
```

Send message to queue

```bash
aws sqs send-message --queue-url URL_DA_FILA --message-body "Mensagem para a fila"
```

Receive message from queue

```bash
aws sqs receive-message --queue-url URL_DA_FILA
```

Delete message from queue

```bash
aws sqs delete-message --queue-url URL_DA_FILA --receipt-handle HANDLE_DA_MENSAGEM
```

## SQS Producer-Consumer Example

A simple AWS SQS demonstration with a producer sending messages and a consumer processing them.

## Overview

- **Producer**: Sends 100 random messages to SQS queue with 2-8 second delays
- **Consumer**: Polls queue continuously, processes messages, and deletes them after completion

## Setup

1. Configure AWS credentials
2. Set environment variables in `.env`.
3. Install dependencies: `pip install boto3 python-dotenv`

## How to Run

**Open two separate terminal windows and run:**

**Terminal 1 (Producer):**

```bash
python producer.py
```

**Terminal 2 (Consumer):**

```bash
python consumer.py
```

Watch how the producer sends messages to the SQS queue and the consumer simultaneously processes them in real-time!
