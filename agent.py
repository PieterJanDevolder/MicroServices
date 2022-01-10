from typing import Optional
from fastapi import BackgroundTasks,FastAPI
from pydantic import BaseModel
import time
from celery_worker import create_order
from model import Order
from celery.result import AsyncResult

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


def write_notification(email: str, message=""):
    time.sleep(15)
    with open(f"{email}_log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}

@app.post("/order")
async def add_order(order: Order):
    task = create_order.delay(order.customer_name, order.order_quantity)
    return {f"Order{task.task_id} rcved"}

@app.get("/orderresult")
async def add_order(taskid):
    res = AsyncResult(taskid)
    res.ready()
    print(res.result)
    return "ok"