from django.shortcuts import render, HttpResponse
from .models import Urls
import secrets
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request,"index.html")

# Function to generate short url for the actual url using python's 'secrets' module.
def shorturl(request):
    if request.method=='POST':
        original_url = request.POST['original_url']
        shortened_url = secrets.token_urlsafe(4)
        print(shortened_url)
        obj = Urls.objects.create(original_url=original_url, shortened_url=shortened_url)
        shortened_url = "http://localhost:8000/"+shortened_url
    # return HttpResponse("The shortened URL for {} is {}".format(original_url, shortened_url))
    return render(request,"urlcreation.html",{"shortened_url":shortened_url, "original_url":original_url})

def redirectionurl(request,shortened_url):
    print("the short url is",shortened_url)

    try:
        obje = Urls.objects.get(shortened_url=shortened_url)

    except Urls.DoesNotExist:
        obje = None

    if obje is not None:
        return redirect(obje.original_url)
    else:
        return render(request,"notfound.html")

