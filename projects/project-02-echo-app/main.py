import uvicorn
from eco_backend.main import app

def main():
    """Start the FastAPI backend server"""
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
