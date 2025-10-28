import React, { useRef } from 'react';
import '../styles/FileUpload.css';

function FileUpload({ files, setFiles }) {
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    const selectedFiles = Array.from(e.target.files);
    const newFiles = selectedFiles.map((file) => ({
      id: Date.now() + Math.random(),
      name: file.name,
      size: file.size,
      type: file.type,
      file: file,
    }));
    setFiles((prev) => [...prev, ...newFiles]);
  };

  const handleRemoveFile = (fileId) => {
    setFiles((prev) => prev.filter((f) => f.id !== fileId));
  };

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
  };

  const getFileIcon = (type) => {
    if (type.includes('pdf')) return '📄';
    if (type.includes('image')) return '🖼️';
    if (type.includes('text')) return '📝';
    if (type.includes('word')) return '📘';
    if (type.includes('sheet') || type.includes('excel')) return '📊';
    return '📎';
  };

  return (
    <div className="file-upload-container">
      <div className="upload-header">
        <h2>Upload Documents</h2>
        <p>Upload files to ask questions about them</p>
      </div>

      <div
        className="upload-area"
        onClick={() => fileInputRef.current?.click()}
      >
        <div className="upload-icon">📁</div>
        <p className="upload-text">Click to upload or drag and drop</p>
        <p className="upload-hint">PDF, TXT, DOCX, Images, etc.</p>
        <input
          ref={fileInputRef}
          type="file"
          multiple
          onChange={handleFileChange}
          style={{ display: 'none' }}
          accept=".pdf,.txt,.doc,.docx,.jpg,.jpeg,.png,.md"
        />
      </div>

      {files.length > 0 && (
        <div className="files-list">
          <div className="files-list-header">
            <h3>Uploaded Files ({files.length})</h3>
          </div>
          {files.map((file) => (
            <div key={file.id} className="file-item">
              <div className="file-info">
                <span className="file-icon">{getFileIcon(file.type)}</span>
                <div className="file-details">
                  <div className="file-name">{file.name}</div>
                  <div className="file-size">{formatFileSize(file.size)}</div>
                </div>
              </div>
              <button
                className="remove-button"
                onClick={() => handleRemoveFile(file.id)}
                title="Remove file"
              >
                ×
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default FileUpload;
