from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="DocBot Service API")

# Configuration from environment variables
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GOOGLE_AI_API_KEY = os.getenv("GOOGLE_AI_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "10"))
MAX_UPLOAD_FILES = int(os.getenv("MAX_UPLOAD_FILES", "10"))

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store uploaded files in memory (temporary - replace with proper storage later)
uploaded_documents = {}

class ChatRequest(BaseModel):
    message: str
    files: Optional[List[str]] = []

class ChatResponse(BaseModel):
    response: str

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

@app.get("/")
async def root():
    return {"message": "DocBot Service API is running"}

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "llm_provider": LLM_PROVIDER,
        "model_name": MODEL_NAME,
        "api_key_configured": bool(OPENAI_API_KEY or ANTHROPIC_API_KEY or GOOGLE_AI_API_KEY)
    }

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Process a chat message and return a response.
    This is a placeholder that will later connect to an LLM model.
    """
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    # Placeholder response - replace this with actual LLM integration later
    file_context = ""
    if request.files:
        file_context = f" (Context: {len(request.files)} document(s) uploaded)"

    response_text = f"You asked: '{request.message}'{file_context}\n\nThis is a placeholder response. I'm ready to help you with your documents once the LLM integration is complete!"

    return ChatResponse(response=response_text)

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a document file.
    This is a placeholder for file upload functionality.
    """
    try:
        contents = await file.read()
        uploaded_documents[file.filename] = {
            "content": contents,
            "size": len(contents),
            "content_type": file.content_type
        }
        return {
            "filename": file.filename,
            "size": len(contents),
            "message": "File uploaded successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")

@app.get("/api/documents")
async def list_documents():
    """
    List all uploaded documents.
    """
    return {
        "documents": [
            {"name": name, "size": info["size"]}
            for name, info in uploaded_documents.items()
        ]
    }

@app.post("/api/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """
    Process a query and return a response.
    This is a placeholder that will later connect to an LLM model.
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    # Placeholder response - replace this with actual LLM integration later
    response_text = f"You asked: '{request.query}'. This is a placeholder response. LLM integration coming soon!"

    return QueryResponse(response=response_text)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
