# Waste Reporting App - ELK Stack Lab

## Overview

This project demonstrates a local ELK Stack implementation for a simulated Waste Reporting Application.

The stack consists of:

* Elasticsearch - log storage and search
* Logstash - log collection and parsing
* Kibana - log visualization and analysis
* Python - fake HTTP log generation
* Docker - containerized deployment

The application generates simulated HTTP access logs such as GET and POST requests. Logstash parses the logs and sends the structured events to Elasticsearch, where they can be searched and analyzed in Kibana.

## Architecture

```text
Python Log Generator
        |
        v
logs/waste-app.log
        |
        v
    Logstash
        |
        v
   Elasticsearch
        |
        v
      Kibana
```

## Project Structure

```text
waste-reporting-elk/
├── docker-compose.yml
├── README.md
├── .gitignore
├── logstash/
│   └── pipeline/
│       └── logstash.conf
├── scripts/
│   └── generate_logs.py
├── screenshots/
└── logs/
```

## Technologies Used

* Docker
* Docker Compose
* Elasticsearch 8.15.3
* Logstash 8.15.3
* Kibana 8.15.3
* Python 3
* Grok
* REST API

## Setup

### 1. Start the ELK Stack

From the project directory:

```bash
sudo docker compose up -d
```

Check the containers:

```bash
sudo docker compose ps
```

The Elasticsearch, Logstash, and Kibana containers should be running.

### 2. Verify Elasticsearch

```bash
curl http://localhost:9200
```

### 3. Generate Fake HTTP Logs

Run:

```bash
python3 scripts/generate_logs.py
```

The script continuously generates simulated HTTP requests and writes them to:

```text
logs/waste-app.log
```

### 4. View Logs in Kibana

Open:

```text
http://localhost:5601
```

Go to:

**Analytics → Discover**

Create/select the following data view:

```text
waste-logs-*
```

Use:

```text
@timestamp
```

as the timestamp field.

The logs can then be searched and analyzed in Discover.

## Log Format

The generated logs follow this format:

```text
timestamp client_ip http_method endpoint status_code response_time
```

Example:

```text
2026-10-07T20:21:10 192.168.1.24 POST /api/report 201 145
```

## Parsed Fields

Logstash extracts the following fields:

| Field           | Description                   |
| --------------- | ----------------------------- |
| `timestamp`     | Original event timestamp      |
| `client_ip`     | Simulated client IP address   |
| `http_method`   | HTTP request method           |
| `endpoint`      | Requested API endpoint        |
| `status_code`   | HTTP response status          |
| `response_time` | Response time in milliseconds |
| `@timestamp`    | Elasticsearch event timestamp |

## Example Use Cases

The logs can be used to investigate:

* Successful API requests
* Failed authentication attempts
* HTTP 4xx errors
* HTTP 5xx errors
* Slow responses
* Frequently accessed endpoints
* Suspicious request patterns

For example, in Kibana Discover:

```text
status_code: 401
```

can be used to find unauthorized requests.

## Screenshots

### Docker Containers

![Docker Containers](screenshots/docker-compose-ps.png)

### Elasticsearch

![Elasticsearch](screenshots/elasticsearch.png)

### Logstash Processing

![Logstash Processing](screenshots/logstash.png)

### Kibana Discover

![Kibana Discover](screenshots/kibana-discover.png)

### Log Generator

![Log Generator](screenshots/log-generator.png)

## Stopping the Environment

To stop the containers:

```bash
sudo docker compose down
```

To start them again:

```bash
sudo docker compose up -d
```

## Conclusion

This project demonstrates a complete local log ingestion pipeline using Docker, Logstash, Elasticsearch, and Kibana. Simulated waste reporting application logs are generated, parsed, stored, and visualized for basic monitoring and analysis.
