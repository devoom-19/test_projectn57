from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def phone_number_page(request):
    return render(request, 'phone number.html')

def wife_page(request):
    return render(request, 'my_wife.html')
