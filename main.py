import os
from fastapi import FastAPI

# Debugging: Print working directory and files to verify correct deployment
print("✅ Current Working Directory:", os.getcwd())
print("📂 Files in directory:", os.listdir(os.getcwd()))

# Load environment variables safely
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ .env file loaded successfully")
except ModuleNotFoundError:
    print("⚠️ Warning: python-dotenv module not found. Skipping environment loading")

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Horse Trainer AI is live!"}

# Ensure the app runs on port 7860 (your preferred port)
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 7860))  # Default to 7860
    print(f"🚀 Starting server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)

