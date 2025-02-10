# 🎙️ Audio Transcription API with Whisper and FastAPI
This project provides an API for transcribing audio files using OpenAI's Whisper model and FastAPI. It includes a simple web interface for uploading audio files and selecting the transcription language.
## 🛠️ Technologies Used
FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.

Whisper: OpenAI's automatic speech recognition (ASR) model for transcribing audio.

HTML/CSS/JavaScript: For the frontend interface.

Uvicorn: ASGI server to run the FastAPI application.
## 🚀 Features
Upload audio files for transcription.

Select the language for transcription (or auto-detect).

Clean and responsive web interface.

Supports multiple languages (e.g., English, Spanish, French, etc.).

Automatic cleanup of uploaded files after processing.

## 📂 Project Structure
├── main.py                ### FastAPI application and Whisper integration
├── uploads/               ### Directory to temporarily store uploaded files
├── README.md              ### Project documentation
## 🧩 Step-by-Step Explanation
### 1. Setup and Dependencies
Install required libraries:
pip install fastapi uvicorn whisper werkzeug
### 2. FastAPI Application Setup
The FastAPI app is initialized with CORS middleware to allow cross-origin requests.

A directory (uploads/) is created to store uploaded audio files temporarily.

python : 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
### 3. Loading the Whisper Model
The Whisper model is loaded using whisper.load_model(). The base model is used by default, but you can switch to tiny or small for lower resource usage.
try:
    model = whisper.load_model("base")
except Exception as e:
    print(f"Error loading Whisper model: {e}")
    raise RuntimeError("Failed to load Whisper model.")

### 4. Frontend Interface
A simple HTML form is served at the root (/) endpoint for uploading audio files and selecting the language.

The form uses JavaScript to send the file and language selection to the /transcribe/ endpoint.
### 5. Transcription Endpoint
The /transcribe/ endpoint accepts an audio file and a language parameter.

The file is saved to the uploads/ directory, transcribed using the Whisper model, and then deleted to save space.

The transcription result is returned as JSON.
### 6. Running the Application
The application is run using Uvicorn:
🎨 Frontend Styling
The frontend is styled using CSS for a clean and modern look.

Key features:

Responsive design.

Custom file upload button.

Dropdown for language selection.
## 🚨 Error Handling
Errors during transcription are logged and returned to the user with a 500 Internal Server Error status.

Example:
{
  "error": "Transcription error: [error details]"
}
## 🌐 API Endpoints
/	GET	Serve the HTML frontend.
/transcribe/	POST	Transcribe an uploaded audio file.
## 🛑 Limitations
The Whisper model can be resource-intensive, especially for larger files or higher-quality models.

The application is designed for development use. For production, consider adding:

Rate limiting.

Authentication.

Better error handling.
## 📜 License
This project is open-source and available under the MIT License.
## 🙏 Credits
OpenAI for the Whisper model.

FastAPI and Uvicorn for the backend framework.

HTML/CSS/JavaScript for the frontend.



