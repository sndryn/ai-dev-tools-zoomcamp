from django.test import TestCase
from django.urls import reverse
from .models import Todo


class TodoViewsTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title="Test TODO", due_date="2025-01-01")

    # HOME VIEW
    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test TODO")

    # CREATE VIEW
    def test_create_view(self):
        response = self.client.post(
            reverse("create"), {"title": "New TODO", "due_date": "2025-12-31"}
        )
        self.assertEqual(response.status_code, 302)  # redirect

        self.assertTrue(Todo.objects.filter(title="New TODO").exists())

    # EDIT VIEW
    def test_edit_view(self):
        response = self.client.post(
            reverse("edit", args=[self.todo.pk]),
            {"title": "Updated Title", "due_date": "2025-03-01"},
        )
        self.assertEqual(response.status_code, 302)

        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, "Updated Title")

    # DELETE VIEW
    def test_delete_view(self):
        response = self.client.post(reverse("delete", args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)

        self.assertFalse(Todo.objects.filter(pk=self.todo.pk).exists())

    # RESOLVE TOGGLE
    def test_resolve_view(self):
        # Initially unresolved
        self.assertFalse(self.todo.resolved)

        response = self.client.get(reverse("resolve", args=[self.todo.pk]))
        self.assertEqual(response.status_code, 302)

        self.todo.refresh_from_db()
        self.assertTrue(self.todo.resolved)

        # Toggle back
        response = self.client.get(reverse("resolve", args=[self.todo.pk]))
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.resolved)
