from django.shortcuts import render

# Create your views here.

def admin_birds_status(request):
    return render(request, 'admin_birds_status.html')

def admin_add_birds_status(request):
    return render(request, 'admin_add_birds_status.html')
    
def admin_birds_detail(request):
    return render (request, 'admin_birds_detail.html')

def admin_add_birds_detail(request):
    return render (request, 'admin_add_birds_detail.html')