from django.shortcuts import render

# Create your views here.
# Home view
def home(request):
    return render(request, "stock_project/home.html", {})


def admin(request):
    return render(request, "stock_project/stockadmin.html", {})
