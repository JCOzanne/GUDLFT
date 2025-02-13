from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task
    def index(self):
        self.client.get('/')

    @task
    def show_summary(self):
        self.client.post('/showSummary', data={"email": "john@simplylift.co"})

    @task
    def book_places (self):
        self.client.post("/purchasePlaces", data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "1"
        })

    @task
    def update_points(self):
        self.client.get("/clubPoints")


