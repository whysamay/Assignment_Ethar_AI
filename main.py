from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import models
from database import engine
from routers import auth, users, dashboard, projects, tasks

models.Base.metadata.create_all(bind=engine)
#all the tables written in models.py with base as the parent class
#they all will be created if these do not exist in the database


app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router)
app.include_router(dashboard.router)
app.include_router(projects.router)
app.include_router(tasks.router)

# Serve the frontend
@app.get("/")
async def root():
    return FileResponse("static/index.html")
