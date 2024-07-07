from django.shortcuts import render, get_object_or_404
from .models import Folder

def folder_list(request):
    folders = Folder.objects.filter(parent=None)
    return render(request, 'folders/folder_list.html', {'folders': folders})

def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    parent = folder.get_parent()
    return render(request, 'folders/folder_detail.html', {'folder': folder, 'parent': parent})

def folder_children(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    children = folder.get_children()
    return render(request, 'folders/folder_children.html', {'folder': folder, 'children': children})
