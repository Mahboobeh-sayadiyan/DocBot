# DocBot

AI-Powered Document Assistant with React UI and Python FastAPI backend.

## Project Structure

```
DocBot/
├── ui/                      # React frontend application
│   ├── public/
│   ├── src/
│   ├── Dockerfile
│   ├── nginx.conf
│   └── package.json
├── service/                 # Python FastAPI backend
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
└── docker-compose.yml       # Docker Compose configuration
```

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd DocBot
```

2. Start the services using Docker Compose:
```bash
docker-compose up --build
```

3. Access the applications:
   - UI (Frontend): http://localhost:3000
   - API (Backend): http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Development

### UI (React Application)

The UI is built with React and includes:
- Modern, responsive interface
- API integration with the backend service
- Nginx reverse proxy for production deployment

To develop locally without Docker:
```bash
cd ui
npm install
npm start
```

### Service (Python FastAPI)

The service is a FastAPI application that will connect to LLM models. Currently includes:
- RESTful API endpoints
- CORS configuration
- Health check endpoint
- Query processing endpoint (placeholder for LLM integration)

To develop locally without Docker:
```bash
cd service
pip install -r requirements.txt
python main.py
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /api/query` - Process queries (LLM integration coming soon)

## Docker Commands

Build and start all services:
```bash
docker-compose up --build
```

Start services in detached mode:
```bash
docker-compose up -d
```

Stop all services:
```bash
docker-compose down
```

View logs:
```bash
docker-compose logs -f
```

Rebuild a specific service:
```bash
docker-compose build service
docker-compose build ui
```

## Next Steps

- Integrate LLM model (OpenAI, Anthropic, or local models)
- Add document processing capabilities
- Implement user authentication
- Add database for conversation history
- Enhance UI with more features

## License

MIT