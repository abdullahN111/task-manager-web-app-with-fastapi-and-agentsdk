from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agent_routes import router as agent_router


from app.routes import router as task_router



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://aibased-taskmanager.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)
app.include_router(agent_router)



