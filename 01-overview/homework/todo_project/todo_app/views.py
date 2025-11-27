from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


def home(request):
    todos = Todo.objects.order_by("resolved", "due_date")
    return render(request, "home.html", {"todos": todos})


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


def edit(request, pk):
    """Edit an existing TODO (no forms)"""
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.due_date = request.POST.get("due_date") or None
        todo.save()
        return redirect("home")

    return render(request, "edit.html", {"todo": todo})


def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        todo.delete()
        return redirect("home")

    return render(request, "delete.html", {"todo": todo})


def resolve(request, pk):
    """Toggle resolved/unresolved"""
    todo = get_object_or_404(Todo, pk=pk)
    todo.resolved = not todo.resolved
    todo.save()
    return redirect("home")
