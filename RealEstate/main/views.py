from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def main_view(request:HttpRequest):

    return render(request, "main/home.html")



def propertie_view(request):

    properties = [
        {"title": "Villa Modern in Malqa", "image": "villa1.jpg"},
        {"title": "Great home for you in Rimal", "image": "villa2.jpg"},
        {"title": "Villa with 8 bedrooms in Swedey", "image": "villa3.jpg"},
        {"title": "Amazing Villa in Hitten", "image": "villa4.jpg"},
    ]
    return render(request, 'main/properties.html', {'properties': properties})



def contact_view(request:HttpRequest):

    return render(request, "main/contact.html")


def mode_view(request:HttpRequest, mode):
    
    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
        
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response

