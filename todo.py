from fastapi import FastAPI, Query

app = FastAPI()

tasks = {
    1:{
        "id":1,
        "title": "Learn FastAPI",
        "description": "create a todo app"
    },
    2:{
        "id":2,
        "title": "trading",
        "description": "research stocks"
    },
    3:{
        "id": 3, 
        "title": "game",
        "description": "reach radiant"
    }
}

@app.get("/all-tasks")
def allTasks():
    return tasks

@app.get("/task")
def task(taskId: int = Query(None, title="Task Id", gt=0)):
    if taskId not in tasks:
        return {"ERROR":"Invalid Task Id"}
    
    return tasks[taskId]

@app.post("/create-task")
def create(task: dict):
    if "id" not in task.keys() or "title" not in task.keys() or "description" not in task.keys():
        return {"ERROR":"Incomplete dictionary"}
    

    if task["id"] in tasks:
        return {"ERROR":"Task Id already exists"}
    

    tasks[task["id"]] = task
    return {"SUCCESS":"Task added"} 