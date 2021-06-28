import pytest
from model_bakery import baker

from core.models import TodoListModel


@pytest.mark.django_db
class TestTodoListEndpoints:
    @pytest.fixture(autouse=True)
    def setup_method_fixture(self, api_client, admin_user, data, strong_pass):
        self.endpoint = "/api/todo/"
        self.client = api_client()
        self.data = data
        self.client.login(username=admin_user.username, password=strong_pass)
        self.model = TodoListModel

    def test_unsuccessful__unauthorized(self):
        self.client.logout()
        response = self.client.get(self.endpoint)

        assert response.status_code == 403
        assert response.json() == {
            "detail": "Authentication credentials were not provided."
        }

    def test_successful__list(self):
        baker.make(self.model, _quantity=3)
        response = self.client.get(self.endpoint)

        assert response.status_code == 200
        assert len(response.json()) == 3

    def test_successful__create(self):
        response = self.client.post(self.endpoint, data=self.data, format="json")

        assert response.status_code == 201
        assert response.json()["title"] == "It is a task!"
        assert response.json()["done"] is False

    def test_unsuccessful__create_bad_data(self):
        data = {}
        response = self.client.post(self.endpoint, data=data, format="json")
        assert response.status_code == 400

    def test_unsuccessful__create_when_more_there_are_five_items(self):
        baker.make(self.model, _quantity=5)
        response = self.client.post(self.endpoint, data=self.data, format="json")
        assert response.status_code == 400
        assert response.json() == {"error": "No more than five tasks are allowed."}

    def test_successful__update(self):
        model = baker.make(self.model, title="More a test", done=True)
        data = {"title": "More a test new Title", "done": False}
        response = self.client.patch(
            f"{self.endpoint}{model.id}/", data=data, format="json"
        )
        assert response.status_code == 200
        assert response.json()["title"] == "More a test new Title"
        assert response.json()["done"] is False

    def test_delete(self, mocker):
        model = baker.make(self.model)
        response = self.client.delete(f"{self.endpoint}{model.id}/")
        todo_list = self.model.objects.filter(id=model.id).first()
        assert response.status_code == 204
        assert todo_list is None
