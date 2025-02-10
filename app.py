from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import whisper
import os
import traceback
from werkzeug.utils import secure_filename
from fastapi.middleware.cors import CORSMiddleware
import warnings
'''
# Suppress specific Whisper warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

app = FastAPI()

# Define the home route
@app.get("/")
def home():
    return "Hello, World!"

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Whisper Model
try:
    model = whisper.load_model("base")  # Try "tiny" if RAM is limited
except Exception as e:
    print(f"Error loading Whisper model: {e}")

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...), language: str = Form("auto")):
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        with open(filepath, "wb") as buffer:
            buffer.write(file.file.read())

        print(f"Saved file at: {filepath}")

        # Check if the file is actually saved
        if not os.path.exists(filepath):
            return JSONResponse(content={"error": "File upload failed."}, status_code=500)

        # Transcribe audio
        options = {"language": None if language == "auto" else language}
        result = model.transcribe(filepath, **options)

        return JSONResponse(content={"text": result.get("text", "No transcription found.")})

    except Exception as e:
        error_message = f"Transcription error: {str(e)}\n{traceback.format_exc()}"
        print(error_message)  # Print full error in logs
        return JSONResponse(content={"error": error_message}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
'''
import warnings
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
import whisper
import os
import traceback
from werkzeug.utils import secure_filename
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

# Suppress specific Whisper warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Whisper Model
try:
    model = whisper.load_model("base")  # Use "tiny" or "small" if RAM is limited
except Exception as e:
    print(f"Error loading Whisper model: {e}")
    raise RuntimeError("Failed to load Whisper model.")

# Serve HTML frontend
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Audio Transcription</title>
    </head>
    <body>
        <h1>Upload Audio File</h1>
        <form id="uploadForm">
            <input type="file" name="file" id="fileInput" accept="audio/*" required>
            <button type="submit">Transcribe</button>
        </form>
        <h2>Transcript:</h2>
        <pre id="transcript"></pre>

        <script>
            document.getElementById("uploadForm").addEventListener("submit", async (event) => {
                event.preventDefault();

                const fileInput = document.getElementById("fileInput");
                const formData = new FormData();
                formData.append("file", fileInput.files[0]);

                try {
                    const response = await fetch("/transcribe/", {
                        method: "POST",
                        body: formData,
                    });
                    const data = await response.json();
                    document.getElementById("transcript").textContent = data.text || data.error;
                } catch (error) {
                    console.error("Error:", error);
                    document.getElementById("transcript").textContent = "An error occurred.";
                }
            });
        </script>
    </body>
    </html>
   

# Transcribe audio file
@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...), language: str = Form("auto")):
    try:
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        with open(filepath, "wb") as buffer:
            buffer.write(file.file.read())

        print(f"Saved file at: {filepath}")
        print(f"File size: {os.path.getsize(filepath)} bytes")

        # Check if the file was saved successfully
        if not os.path.exists(filepath):
            raise HTTPException(status_code=500, detail="File upload failed.")

        # Transcribe the audio
        options = {"language": None if language == "auto" else language}
        result = model.transcribe(filepath, **options)
        print(f"Transcription result: {result}")

        # Clean up: Delete the uploaded file after processing
        os.remove(filepath)

        return JSONResponse(content={"text": result.get("text", "No transcription found.")})

    except Exception as e:
        error_message = f"Transcription error: {str(e)}\n{traceback.format_exc()}"
        print(error_message)  # Log the full error
        raise HTTPException(status_code=500, detail=error_message)

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


 """







import warnings
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
import whisper
import os
import traceback
from werkzeug.utils import secure_filename
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

# Suppress specific Whisper warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Whisper Model
try:
    model = whisper.load_model("base")  # Use "tiny" or "small" if RAM is limited
except Exception as e:
    print(f"Error loading Whisper model: {e}")
    raise RuntimeError("Failed to load Whisper model.")

# Serve HTML frontend with CSS styling
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Audio Transcription</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background: white;
                padding: 2rem;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 500px;
                text-align: center;
            }
            h1 {
                color: #333;
                margin-bottom: 1.5rem;
            }
            input[type="file"] {
                display: none;
            }
            .file-upload {
                background: #007bff;
                color: white;
                padding: 0.75rem 1.5rem;
                border-radius: 4px;
                cursor: pointer;
                margin-bottom: 1rem;
            }
            .file-upload:hover {
                background: #0056b3;
            }
            select {
                width: 100%;
                padding: 0.75rem;
                border-radius: 4px;
                border: 1px solid #ddd;
                margin-bottom: 1rem;
            }
            button {
                background: #28a745;
                color: white;
                padding: 0.75rem 1.5rem;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                width: 100%;
            }
            button:hover {
                background: #218838;
            }
            pre {
                background: #f8f9fa;
                padding: 1rem;
                border-radius: 4px;
                border: 1px solid #ddd;
                white-space: pre-wrap;
                word-wrap: break-word;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Audio Transcription</h1>
            <form id="uploadForm">
                <label for="fileInput" class="file-upload">Choose Audio File</label>
                <input type="file" name="file" id="fileInput" accept="audio/*" required>
                <br><br>
                <label for="language">Select Language:</label>
                <select name="language" id="language">
                    <option value="auto">Auto Detect</option>
                    <option value="en">English</option>
                    <option value="es">Spanish</option>
                    <option value="fr">French</option>
                    <option value="de">German</option>
                    <option value="bn">Bangla</option>
                    <option value="hi">Hindi</option>
                    <option value="ja">Japanese</option>
                    <option value="zh">Chinese</option>
                    <!-- Add more languages as needed -->
                </select>
                <br><br>
                <button type="submit">Transcribe</button>
            </form>
            <h2>Transcript:</h2>
            <pre id="transcript">Your transcription will appear here...</pre>
        </div>

        <script>
            document.getElementById("uploadForm").addEventListener("submit", async (event) => {
                event.preventDefault();

                const fileInput = document.getElementById("fileInput");
                const languageSelect = document.getElementById("language");
                const formData = new FormData();
                formData.append("file", fileInput.files[0]);
                formData.append("language", languageSelect.value);

                try {
                    const response = await fetch("/transcribe/", {
                        method: "POST",
                        body: formData,
                    });
                    const data = await response.json();
                    document.getElementById("transcript").textContent = data.text || data.error;
                } catch (error) {
                    console.error("Error:", error);
                    document.getElementById("transcript").textContent = "An error occurred.";
                }
            });
        </script>
    </body>
    </html>
    """

    
# Transcribe audio file
@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...), language: str = Form("auto")):
    try:
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        with open(filepath, "wb") as buffer:
            buffer.write(file.file.read())

        print(f"Saved file at: {filepath}")
        print(f"File size: {os.path.getsize(filepath)} bytes")

        # Check if the file was saved successfully
        if not os.path.exists(filepath):
            raise HTTPException(status_code=500, detail="File upload failed.")

        # Transcribe the audio
        options = {"language": None if language == "auto" else language}
        result = model.transcribe(filepath, **options)
        print(f"Transcription result: {result}")

        # Clean up: Delete the uploaded file after processing
        os.remove(filepath)

        return JSONResponse(content={"text": result.get("text", "No transcription found.")})

    except Exception as e:
        error_message = f"Transcription error: {str(e)}\n{traceback.format_exc()}"
        print(error_message)  # Log the full error
        raise HTTPException(status_code=500, detail=error_message)

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)