from django.shortcuts import render
from django.shortcuts import redirect
from .models import Item
from .forms import ItemForm


def index(request):
    items = Item.objects.all() 
    return render(request, 'index.html', {'items': items})

def about(request):
    return render(request, 'about.html')
def about_me(request):
    return render(request, 'about_me.html')

def add_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = ItemForm()
    return render(request, 'form.html', {'form': form})