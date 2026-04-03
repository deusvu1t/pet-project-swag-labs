import requests
import allure


class TestApi:
    @allure.title("Get users and verify response")
    def test_get_users(self):
        response = requests.get("https://jsonplaceholder.typicode.com/users")

        assert response.status_code == 200

        data = response.json()
        assert len(data) > 0
        assert "id" in data[0]

    @allure.title("Create a new user and verify response")
    def test_create_user(self):
        payload = {
            "name": "Yuri",
            "job": "QA"
        }

        response = requests.post(
            "https://jsonplaceholder.typicode.com/users",
            json=payload
        )

        assert response.status_code == 201
        assert response.json()["name"] == "Yuri"
