from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request, *args, **kwargs):
    return render(request, "app/index.html")

def robots_txt(request):
    content = "User-agent: *\nDisallow:\nSitemap: https://sympa-kalambay.onrender.com/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")
