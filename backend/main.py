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

@klu.get("/student")
def student():
    return {"id": 1, "name": "Ram", "gender": "Male", "course": "DSA"}

@klu.get("/students")
def getstudents():
    return [
        {"id": 1, "name": "Ram", "gender": "Male", "course": "DSA"},
        {"id": 2, "name": "Shyam", "gender": "Male", "course": "ML"},
        {"id": 3, "name": "Sita", "gender": "Female", "course": "AI"},
        {"id": 4, "name": "Gita", "gender": "Female", "course": "DSA"}
    ]
