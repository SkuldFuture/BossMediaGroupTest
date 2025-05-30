import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from boss_test.apps.tasks.models import Task

User = get_user_model()

@pytest.fixture
def user(db):
    return User.objects.create_user(username="Test", email="test@example.com", password="password")

@pytest.fixture
def client(user):
    client = APIClient()
    response = client.post("/api/authentification/login/", {"email": user.email, "password": "password"})
    token = response.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client

@pytest.mark.django_db
def test_create_task(client):
    response = client.post("/api/tasks/", {"title": "Test task", "description": "desc"})
    assert response.status_code == 201
    assert Task.objects.count() == 1
    assert Task.objects.first().title == "Test task"

@pytest.mark.django_db
def test_list_tasks(client):
    Task.objects.create(user=User.objects.first(), title="T1")
    Task.objects.create(user=User.objects.first(), title="T2")
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    assert len(response.data["results"]) == 2

@pytest.mark.django_db
def test_retrieve_task(client):
    task = Task.objects.create(user=User.objects.first(), title="Retrieve")
    response = client.get(f"/api/tasks/{task.id}/")
    assert response.status_code == 200
    assert response.data["title"] == "Retrieve"

@pytest.mark.django_db
def test_update_task(client):
    task = Task.objects.create(user=User.objects.first(), title="Old Title")
    response = client.put(f"/api/tasks/{task.id}/", {"title": "New Title", "description": "", "completed": False})
    assert response.status_code == 200
    task.refresh_from_db()
    assert task.title == "New Title"

@pytest.mark.django_db
def test_delete_task(client):
    task = Task.objects.create(user=User.objects.first(), title="To delete")
    response = client.delete(f"/api/tasks/{task.id}/")
    assert response.status_code == 204
    assert Task.objects.count() == 0
