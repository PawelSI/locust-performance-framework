from locust import HttpUser, task, between

class ApiUser(HttpUser):
    # Każdy wirtualny użytkownik odczeka od 1 do 5 sekund między zapytaniami
    wait_time = between(1, 5)

    # Adres bazowy naszego API
    host = "https://jsonplaceholder.typicode.com"

    @task(3)
    def get_users(self):
        """Symuluje przeglądanie listy użytkowników"""
        self.client.get("/users")

    @task(1)
    def create_post(self):
        """Symuluje tworzenie nowego posta przez użytkownika."""
        payload = {
            "title": "Test Performance",
            "body": "Sprawdzamy obciążenie serwera",
            "userID": 1
        }
        self.client.post("/post", json=payload)