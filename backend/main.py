from fastapi import FastAPI

klu = FastAPI(title="AI Tutor",
              description="AI Tutor PBL Project",
              version = "1.0.0")

@klu.get("/")
def home():
    return {"message": "Welcome to AI Tutor!"}

@klu.get("/demo")
def demo():
    return {"message": "KL Univerity"}

@klu.get("/askquestion")
def ask():
    return {"message": "What is LLM?", "answer": "Large Language Model"}


