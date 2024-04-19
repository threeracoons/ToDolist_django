# TODO/views.py
from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'TODO/todo_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        TodoItem.objects.create(text=text)
    return redirect('todo_list')

def remove_item(request, item_id):
    item = TodoItem.objects.get(id=item_id)
    item.delete()
    return redirect('todo_list')
