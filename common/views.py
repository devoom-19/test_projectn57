from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'pages/about.html')

def author_page(request):
    return render(request, 'pages/author.html')