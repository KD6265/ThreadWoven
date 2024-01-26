from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def custom_404_view(request, exception):
    return render(request, '404.html')