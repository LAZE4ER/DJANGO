from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def about_me(request):
    return render(request, 'about_me.html')