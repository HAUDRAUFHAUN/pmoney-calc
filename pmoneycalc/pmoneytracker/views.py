from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def newpayment(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'pmoneytracker/newpayment.html')
