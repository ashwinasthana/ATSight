# Deployment Guide

## Local Development

```bash
# Terminal 1: Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend
npm install
npm run dev
```

## Docker Compose (Local)

```bash
docker-compose up -d
```

Access:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Database: localhost:5432

## Production Deployment

### Option 1: AWS (Recommended)

#### Backend (ECS + Fargate)

1. **Build and push Docker image**
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

docker build -t atsight-backend ./backend
docker tag atsight-backend:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/atsight-backend:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/atsight-backend:latest
```

2. **Create ECS task definition**
```json
{
  "family": "atsight-backend",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "containerDefinitions": [
    {
      "name": "atsight-backend",
      "image": "<account-id>.dkr.ecr.us-east-1.amazonaws.com/atsight-backend:latest",
      "portMappings": [
        {
          "containerPort": 8000,
          "hostPort": 8000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "OPENAI_API_KEY",
          "value": "sk-..."
        },
        {
          "name": "DATABASE_URL",
          "value": "postgresql://..."
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/atsight-backend",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

3. **Create ECS service**
```bash
aws ecs create-service \
  --cluster atsight \
  --service-name atsight-backend \
  --task-definition atsight-backend \
  --desired-count 2 \
  --launch-type FARGATE \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-xxx],securityGroups=[sg-xxx],assignPublicIp=ENABLED}" \
  --load-balancers targetGroupArn=arn:aws:elasticloadbalancing:...,containerName=atsight-backend,containerPort=8000
```

#### Frontend (Vercel or Amplify)

**Option A: Vercel (Recommended)**
```bash
npm install -g vercel
vercel --prod
```

**Option B: AWS Amplify**
```bash
npm install -g @aws-amplify/cli
amplify init
amplify publish
```

#### Database (RDS)

```bash
aws rds create-db-instance \
  --db-instance-identifier atsight-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username atsight \
  --master-user-password <strong-password> \
  --allocated-storage 20 \
  --publicly-accessible false
```

### Option 2: Heroku

**Backend**
```bash
heroku create atsight-backend
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku config:set OPENAI_API_KEY=sk-...
```

**Frontend**
```bash
heroku create atsight-frontend
git push heroku main
```

### Option 3: DigitalOcean App Platform

1. Connect GitHub repository
2. Create app.yaml:

```yaml
name: atsight
services:
- name: backend
  github:
    repo: username/atsight
    branch: main
  build_command: pip install -r requirements.txt
  run_command: uvicorn app.main:app --host 0.0.0.0 --port 8080
  http_port: 8080
  envs:
  - key: OPENAI_API_KEY
    value: ${OPENAI_API_KEY}
  - key: DATABASE_URL
    value: ${DATABASE_URL}

- name: frontend
  github:
    repo: username/atsight
    branch: main
  build_command: npm install && npm run build
  run_command: npm start
  http_port: 3000
  envs:
  - key: NEXT_PUBLIC_API_URL
    value: https://backend-xxx.ondigitalocean.app

databases:
- name: postgres
  engine: PG
  version: "15"
```

## Environment Variables

### Backend Production

```bash
OPENAI_API_KEY=sk-...
DATABASE_URL=postgresql://user:pass@host:5432/atsight
JWT_SECRET=<generate-strong-secret>
JWT_ALGORITHM=HS256
ENVIRONMENT=production
```

### Frontend Production

```bash
NEXT_PUBLIC_API_URL=https://api.atsight.com
```

## SSL/TLS Certificate

### Using Let's Encrypt (Free)

```bash
# Install certbot
sudo apt-get install certbot python3-certbot-nginx

# Generate certificate
sudo certbot certonly --standalone -d api.atsight.com

# Auto-renewal
sudo systemctl enable certbot.timer
```

### Using AWS Certificate Manager

```bash
aws acm request-certificate \
  --domain-name api.atsight.com \
  --validation-method DNS
```

## Monitoring & Logging

### CloudWatch (AWS)

```bash
# View logs
aws logs tail /ecs/atsight-backend --follow

# Create alarm
aws cloudwatch put-metric-alarm \
  --alarm-name atsight-backend-errors \
  --alarm-description "Alert on backend errors" \
  --metric-name Errors \
  --namespace AWS/ECS \
  --statistic Sum \
  --period 300 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold
```

### Sentry (Error Tracking)

```python
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

sentry_sdk.init(
    dsn="https://xxx@sentry.io/xxx",
    integrations=[FastApiIntegration()],
    traces_sample_rate=0.1
)
```

## Performance Optimization

### Backend
- Enable gzip compression
- Use connection pooling
- Cache LLM responses
- Implement rate limiting

### Frontend
- Enable Next.js image optimization
- Use dynamic imports
- Implement service workers
- Cache API responses

## Backup & Recovery

### Database Backups

```bash
# Automated daily backups (AWS RDS)
aws rds modify-db-instance \
  --db-instance-identifier atsight-db \
  --backup-retention-period 30 \
  --preferred-backup-window "03:00-04:00"

# Manual backup
aws rds create-db-snapshot \
  --db-instance-identifier atsight-db \
  --db-snapshot-identifier atsight-backup-$(date +%Y%m%d)
```

## Scaling

### Horizontal Scaling

**Backend (ECS)**
```bash
aws ecs update-service \
  --cluster atsight \
  --service atsight-backend \
  --desired-count 5
```

**Frontend (Vercel)**
- Automatic scaling included

### Vertical Scaling

**Backend (ECS)**
```bash
# Update task definition with more CPU/memory
aws ecs register-task-definition \
  --family atsight-backend \
  --cpu 512 \
  --memory 1024
```

## Cost Optimization

- Use spot instances for non-critical workloads
- Enable auto-scaling based on metrics
- Use CDN for static assets
- Optimize LLM API calls (caching, batching)
- Monitor and alert on cost anomalies

## Rollback Procedure

```bash
# View previous deployments
aws ecs describe-services --cluster atsight --services atsight-backend

# Rollback to previous task definition
aws ecs update-service \
  --cluster atsight \
  --service atsight-backend \
  --task-definition atsight-backend:5
```

## Health Checks

```bash
# Backend
curl https://api.atsight.com/health

# Frontend
curl https://atsight.com
```

## Maintenance

### Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "Add users table"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

### Dependency Updates

```bash
# Backend
pip list --outdated
pip install --upgrade package-name

# Frontend
npm outdated
npm update package-name
```
