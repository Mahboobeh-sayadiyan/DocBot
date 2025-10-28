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

2. Set up environment variables:
```bash
# Copy example environment files
cp service/.env.example service/.env
cp ui/.env.example ui/.env

# Edit service/.env and add your API keys
# For example, add your OpenAI API key:
# OPENAI_API_KEY=sk-your-key-here
```

3. Start the services using Docker Compose:
```bash
docker-compose up --build
```

4. Access the applications:
   - UI (Frontend): http://localhost:3000
   - API (Backend): http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Environment Configuration

### Service Environment Variables

The service uses the following environment variables (defined in `service/.env`):

**LLM API Keys:**
- `OPENAI_API_KEY` - OpenAI API key for GPT models
- `ANTHROPIC_API_KEY` - Anthropic API key for Claude models
- `GOOGLE_AI_API_KEY` - Google AI API key for Gemini models
- `HUGGINGFACE_API_KEY` - Hugging Face API key for open-source models

**Model Configuration:**
- `LLM_PROVIDER` - Which provider to use (openai, anthropic, google, huggingface)
- `MODEL_NAME` - Specific model name (e.g., gpt-3.5-turbo, claude-3-opus)

**Application Settings:**
- `MAX_FILE_SIZE_MB` - Maximum file upload size (default: 10MB)
- `MAX_UPLOAD_FILES` - Maximum number of files to upload (default: 10)

See `service/.env.example` for a complete list of available options.

## Development

### UI (React Application)

The UI is built with React and Webpack, featuring:
- ChatGPT-style interface with message history
- File upload with drag-and-drop support
- Side-by-side layout with file management sidebar
- Modern, responsive design
- Nginx reverse proxy for production deployment

To develop locally without Docker:
```bash
cd ui
npm install
npm start
```

### Service (Python FastAPI)

The service is a FastAPI application that connects to LLM models. Features:
- RESTful API endpoints
- Environment-based configuration
- CORS configuration
- File upload and management
- Chat endpoint for LLM integration
- Health check with configuration status

To develop locally without Docker:
```bash
cd service
cp .env.example .env
# Edit .env and add your API keys
pip install -r requirements.txt
python main.py
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check with configuration status
- `POST /api/chat` - Chat with document context
- `POST /api/upload` - Upload document files
- `GET /api/documents` - List uploaded documents
- `POST /api/query` - Process queries (legacy endpoint)

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

## LLM Integration

To integrate with an LLM provider:

1. **Add your API key** to `service/.env`:
   ```bash
   OPENAI_API_KEY=sk-your-key-here
   LLM_PROVIDER=openai
   MODEL_NAME=gpt-3.5-turbo
   ```

2. **Install the provider's SDK** in `service/requirements.txt`:
   - OpenAI: `openai>=1.0.0`
   - Anthropic: `anthropic>=0.18.0`
   - Google: `google-generativeai>=0.3.0`

3. **Update the chat endpoint** in `service/main.py` to call your LLM

4. **Restart the service**:
   ```bash
   docker-compose restart service
   ```

## Next Steps

- Complete LLM integration with document processing
- Add vector database for document embeddings
- Implement conversation history persistence
- Add user authentication
- Support more document formats (PDF parsing, OCR, etc.)

## License

MIT