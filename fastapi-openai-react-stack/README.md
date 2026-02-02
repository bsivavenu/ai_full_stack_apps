# AI Full Stack App

A full-stack application combining a FastAPI backend with OpenAI integration and a React frontend.

## Project Structure

```
ai_full_stack_app/
├── ai-frontend/          # React frontend application
├── ai-backend/           # FastAPI backend service
└── README.md
```

## Prerequisites

- **Frontend:** Node.js 16+ and npm
- **Backend:** Python 3.12+
- **API Keys:** OpenAI API key

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd ai-backend
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Create `.env` file with your OpenAI API key:
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

5. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ai-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The app will open at `http://localhost:3000`

## API Endpoints

- `POST /ask-ai` - Send a prompt and get AI-generated response
  - Request body: `{ "text": "Your prompt here" }`
  - Response: `{ "response": "AI generated text" }`

## Environment Variables

Backend requires the following in `.env`:
- `OPENAI_API_KEY` - Your OpenAI API key

## Development

- Frontend runs on port 3000
- Backend API runs on port 8000
- CORS is configured to allow frontend requests

## License

MIT
