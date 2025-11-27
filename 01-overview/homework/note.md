# Homework notes

The Django TODO project is entirely implemented using ChatGPT as the exercise for the Introduction to AI-Assisted Development section the the AI-Dev-Tools course. Below are some instructions used to build the project based on answers from ChatGPT.

## Installing Django
```
pip install django
```

## Creating project
```
django-admin startproject todo_project
```

## Creating app
```
cd todo_project
python manage.py startapp todo_app
```

Add `todo_app` to `INSTALLED_APPS` in `todo_project/settings.py`

## Creating models
Update `todo_app/models.py`

e.g.
```
class Todo(models.model):
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

## Running migrations
```
cd todo_project

python manage.py makemigrations
python manage.py migrate
```

## Implementing logic
Update `todo_app/views.py`

e.g.
```
def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        due_date = request.POST.get("due_date") or None

        Todo.objects.create(
            title=title,
            due_date=due_date,
        )

        return redirect("home")

    return render(request, "create.html")

```

## Create templates
```
cd todo_project
mkdir template
```

Create HTML templates inside the template folder.

## Registering templates
Update `todo_project/settings.py` and register the template directory in `TEMPLATES` section.

e.g.
```
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

Update `todo_project/urls.py`

e.g.
```
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/resolve/", views.resolve, name="resolve"),
]
```

## Testing

Update `todo_app/tests.py`

e.g.
```
class TodoViewsTest(TestCase):

    def setUp(self):
        self.todo = Todo.objects.create(
            title="Test TODO",
            due_date="2025-01-01"
        )
    # CREATE VIEW
    def test_create_view(self):
        response = self.client.post(reverse("create"), {
            "title": "New TODO",
            "due_date": "2025-12-31"
        })
        self.assertEqual(response.status_code, 302)  # redirect

        self.assertTrue(
            Todo.objects.filter(title="New TODO").exists()
        )
```

Run test
```
python manage.py test
```

## Running the app
```
python manage.py runserver
```

Open `localhost:8000`