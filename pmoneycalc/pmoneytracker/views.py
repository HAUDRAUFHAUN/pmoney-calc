from django.shortcuts import render, HttpResponseRedirect
from .models import Payment

# Create your views here.


def index(request):
    return render(request, 'index.html')


def newpayment(request):
    if request.method == "POST":
        print(request.POST)
        p = Payment(child=request.user,
                    payment=request.POST.get('amount'), parent=request.POST.get('parent'))

        p.save()
    return render(request, 'pmoneytracker/newpayment.html')


def dashboard(request):
    return render(request, 'pmoneytracker/dashboard.html')
