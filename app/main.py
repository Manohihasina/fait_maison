from fastapi import FastAPI
from app.core.database import SessionLocal
from sqlalchemy import text
from app.core.firebase import db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Family Business API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permet à l'application mobile d'accéder à l'API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "Family Business API fonctionne !",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/health/database")
def database_health_check():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception as e:
        return {
            "status": "error",
            "database": "disconnected",
            "message": str(e),
        }

    finally:
        db.close()


@app.get("/health/firebase")
def firebase_health():
    db.collection("test").document("connection").set({
        "status": "connected"
    })

    return {
        "status": "ok",
        "firebase": "connected"
    }