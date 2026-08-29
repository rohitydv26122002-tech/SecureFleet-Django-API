from django.shortcuts import render

# Create your views here.
def all_website(request):
    return render(request, 'website/all_website.html')
