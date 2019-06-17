from locust import HttpLocust, TaskSet, task


class Behavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task
    def index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = Behavior
    min_wait = 5000
    max_wait = 9000
