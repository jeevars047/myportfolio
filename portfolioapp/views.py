from django.shortcuts import render,redirect
from django.http import HttpResponse
from portfolioapp.models import Portfolio
from portfolioapp.forms import PortfolioForm

def index(request):
    return render(request,'appfile/index.html')
def skill(request):
    return render(request,'appfile/skills.html')
def projects(request):
    return render(request,'appfile/projects.html')
def resume(request):
    return render(request,'appfile/resume.html')
def about(request):
    return render(request,'appfile/about.html')
def contact(request):
    info = PortfolioForm()
    if request.method == "POST":
        info = PortfolioForm(request.POST)
        if info.is_valid():
            info.save()
        return redirect('/thankyou')
    return render(request,'appfile/contact.html',{'info':info})
def thankyou(request):
    return render(request,'appfile/thankyou.html')
    
  