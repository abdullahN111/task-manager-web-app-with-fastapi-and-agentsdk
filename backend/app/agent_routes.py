from fastapi import APIRouter, HTTPException
from agents import Agent, Runner
from app.tools import add_task, view_all_tasks, delete_task
from utils.agent_config import model, session

router = APIRouter()

@router.post("/agent")
async def run_agent(payload: dict):
    user_input = payload.get("input")
    if not user_input:
        raise HTTPException(status_code=400, detail="Missing 'input'")
    
    agent = Agent(
        name="Task Manager Agent",
        instructions="""
        You are a Precise Task Manager Agent who can ADD and DELETE Tasks based on user query, you will be using tools to perform your actions.
    
    Here is what you can do:
    
    - If user wants to add a task you will call add_task
    - If user wants to delete a task by providing ID you will call delete_task using that ID

        """,
        model=model,
        tools=[add_task, view_all_tasks, delete_task]
    )

    try:
        response = await Runner.run(starting_agent=agent, input=user_input, session=session)
        return {"output": response.final_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
