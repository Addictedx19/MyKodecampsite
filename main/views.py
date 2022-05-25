from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, template_name='main/homepage.html')

def contactpage(request):
    return render(request, template_name='main/contactpage.html')

def aboutpage(request):
    return render(request, template_name='main/aboutpage.html') 