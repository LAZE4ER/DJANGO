from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.


def visit_counter_view(request):
    visit_count = request.session.get("visit_count", 0)
    visit_count += 1
    request.session["visit_count"] = visit_count

    return HttpResponse(f"You have visited this page {visit_count} times")


def visit_reset(request):
     request.session.pop("visit_count", None)
    
     return redirect('visit_counter')  
 
 
 
 
 
