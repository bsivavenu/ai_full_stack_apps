# AI Full Stack Apps

A monorepo containing multiple full-stack applications built with modern technologies.

## Projects

### 1. [fastapi-openai-react-stack](./fastapi-openai-react-stack/)

A full-stack application combining:
- **Backend:** FastAPI with OpenAI integration
- **Frontend:** React 19
- **Features:** AI text generation, CORS-enabled API, interactive UI

**Quick Start:**
```bash
# Backend
cd fastapi-openai-react-stack/ai-test
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env  # Add your OPENAI_API_KEY
uvicorn app.main:app --reload

# Frontend (in new terminal)
cd fastapi-openai-react-stack/ai-frontend
npm install
npm start
```

Visit `http://localhost:3000`

---

## Repository Structure

```
ai_full_stack_apps/
├── fastapi-openai-react-stack/    # First full-stack app
│   ├── ai-frontend/               # React frontend
│   ├── ai-test/                   # FastAPI backend
│   └── README.md
├── README.md                       # This file
└── .gitignore
```

## Future Projects

Add more full-stack applications here:
- `nextjs-express-fullstack/`
- `svelte-django-app/`
- etc.

## Prerequisites

- **Node.js 16+** and npm
- **Python 3.12+**
- OpenAI API key

## Contributing

Each project is independent. Refer to individual project READMEs for specific setup and contribution guidelines.

## License

MIT
