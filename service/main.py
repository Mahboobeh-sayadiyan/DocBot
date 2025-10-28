from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="DocBot Service API")

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
    return {"status": "healthy"}

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
