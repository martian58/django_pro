from django.shortcuts import render
from .models import Customer

def home(request):

    return render(request, 'index.html', {})


def about(request):

    return render(request, 'about.html', {})

def customer_view(request):
    customers = Customer.objects.all()

    return render(request, 'customers.html', {
        'customers': customers
    })