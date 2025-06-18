from django.http import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import FileResponse
from django.conf import settings
import os

from app.models import CV
from portofolio.settings import EMAIL_HOST_USER

# Create your views here.

def index(request, *args, **kwargs):

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
            
        # Envoi de l'email à vous-même

        send_mail(
            subject=f'Nouveau message depuis votre portfolio qui concerne {subject}',
            message=f"De: {name} <{email}>\n\nMessage:\n \n{message}",
            from_email=email,  # Expéditeur
            recipient_list=[EMAIL_HOST_USER],  # Votre email comme destinataire
            fail_silently=False  # Un seul paramètre fail_silently
        )

        messages.success(request, "Votre mail a été envoyé avec succès !")
        return redirect('index')

    return render(request, "app/index.html")

def download_cv(request):
    try:
        cv = CV.objects.latest('date_ajout')  # récupère le plus récent
        file_path = cv.fichier.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
    except CV.DoesNotExist:
        raise Http404("Aucun CV disponible.")
    except FileNotFoundError:
        raise Http404("Fichier introuvable.")
    

def robots_txt(request):
    content = "User-agent: *\nDisallow:\nSitemap: https://sympa-kalambay.onrender.com/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")
