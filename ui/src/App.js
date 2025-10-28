import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import Chat from './components/Chat';
import './styles/App.css';

function App() {
  const [uploadedFiles, setUploadedFiles] = useState([]);

  return (
    <div className="App">
      <header className="App-header">
        <div className="header-content">
          <h1>🤖 DocBot</h1>
          <p>AI-Powered Document Assistant</p>
        </div>
      </header>
      <main className="main-content">
        <aside className="sidebar">
          <FileUpload files={uploadedFiles} setFiles={setUploadedFiles} />
        </aside>
        <div className="chat-section">
          <Chat uploadedFiles={uploadedFiles} />
        </div>
      </main>
    </div>
  );
}

export default App;
