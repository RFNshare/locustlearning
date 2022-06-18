from locust import TaskSet, task, User, between, SequentialTaskSet


class SearchProduct(TaskSet):
    @task(4)
    def search_men_product(self):
        print("Searching Men Products")

    @task(6)
    def search_kids_products(self):
        print("Search Kid Products")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]
