# AI Backend

FastAPI backend service for the AI Full Stack App with OpenAI integration.

## Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

4. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## API Endpoints

- `POST /ask-ai` - Generate AI text response
  - Request: `{ "text": "prompt" }`
  - Response: `{ "response": "generated text" }`

## Configuration

See `.env.example` for required environment variables.
