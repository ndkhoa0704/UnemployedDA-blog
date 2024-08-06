import time
from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/")

    @task(3)
    def view_articles(self):
        for item_id in range(10):
            self.client.get(f"/article/{item_id}", name="/item")
            time.sleep(1)

    def on_start(self):
        self.client.post("/token", json={"username":"admin", "password":"admin"})