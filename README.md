# quickview-clickhouse

[![license](https://img.shields.io/:license-Apache%202-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)

# Docker

- Start all services to deploy needed environment:

```bash
docker-compose up -d --build --force-recreate
```

- Stop all services:

```bash
docker-compose down
```

# Versions

- The `latest` tag points to the latest release of the latest stable branch.

# Volumes

- `/docker-entrypoint-initdb.d/` — folder with database initialization scripts.
- `sed.sh` — script to substitute variables in `docker-entrypoint-initdb.sql`.

# Configuration

### Kafka environment variables

- `KAFKA_BROKER_LIST`: Kafka application broker list.
- `KAFKA_TOPIC_LIST`: Kafka application topic list.
- `KAFKA_GROUP_NAME`: Kafka application group name.

### ClickHouse environment variables

- `CLICKHOUSE_DEFAULT_ACCESS_MANAGEMENT`: ClickHouse application default access management.
- `CLICKHOUSE_HOST`: ClickHouse application host.
- `CLICKHOUSE_DB`: ClickHouse application database name.
- `CLICKHOUSE_USER`: ClickHouse application user.
- `CLICKHOUSE_PASSWORD`: ClickHouse application password.
