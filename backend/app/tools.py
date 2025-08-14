from agents import function_tool
from utils.database import SessionLocal
from utils import models



@function_tool
def add_task(task_name: str, task_description: str, task_deadline: str):
    """Add a task by using task_name: str (print task name Capitalize i.e Task), task_description: str (print task description Capitalize i.e This is my Task, do not add task description like 'The task is to do that' etc) and task_deadline: str (print deadline date in dd-mm-yyyy format no matter what the user provides)
    If user didnt give you data in required format, arrange it by using only 2/3 words for title and minimum 8 words description, return the successfull message in consistent format like Task task_name is added.
    """
    db = SessionLocal()
    try:
        new_task = models.Task(
            title=task_name,
            description=task_description,
            deadline=task_deadline
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return f"✅ Added: #{new_task.id} {new_task.title} | {new_task.deadline}"
    except Exception as e:
        db.rollback()
        return f"❌ Failed to add task: {e}"
    finally:
        db.close()
        
        
@function_tool
def view_all_tasks():
    """Fetch and view all tasks from database"""
    db = SessionLocal()
    try:
        tasks = db.query(models.Task).all()
        if not tasks:
            return {"message": "📂 No tasks found."}
        task_list = [f"- #{task.id} {task.title} | {task.deadline}" for task in tasks]
       
        for task in tasks:
            print(f"- #{task.id} {task.title} | {task.deadline}")
       
        return {"message": "Here is the list of all your tasks:", "tasks": task_list}
    except Exception as e:
        return {"error": f"❌ Failed to fetch tasks: {e}"}
    finally:
        db.close()


@function_tool
def delete_task(id: int):
    """Delete a task by using id: int"""
    db = SessionLocal()
    try:
        task = db.query(models.Task).filter(models.Task.id == id).first()
        if not task:
           
            return f"⚠️ Task {id} not found."
        db.delete(task)
        db.commit()
        return f"🗑️ Deleted task #{id}"
    except Exception as e:
        db.rollback()
        return f"❌ Failed to delete task: {e}"
    finally:
        db.close()
