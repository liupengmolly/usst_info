from django.shortcuts import render
from jwc.models import Jwcinfo
from django.http import HttpResponse
# import json
# Create your views here.

# GITHUB_AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
# CLIENT_ID = "ba6eac5880e1603ae793"
# CLIENT_SECRET = "9846b066492f86c6dad0191864932f4aa3fe6213"

# GITHUB_CALLBACK = "https://localhost:8000/jwc/github"


def index(request):
    """
    show some important notice under the search bar.
    not implemented now, just get the first 5 notices from the database.
    """
    attentions = Jwcinfo.objects.order_by("pubtime")[:4]
    aboutuser = Jwcinfo.objects.order_by("crawltime")[50:54]
    return render(request, 'index.html', {"attentions": attentions,"aboutuser":aboutuser})


def info(request, info_id):
    """render detail page of a certain article
    """
    result = Jwcinfo.objects.get(id=info_id)
    return render(request, 'info.html', {'result': result})

# def githubCallBack():
# 	session_code = request.GET.get('code')

def glances_add(request):
    """glances +1 per click.
    """
    notice_id = request.GET.get('id')
    notice = Jwcinfo.objects.get(id = notice_id)
    notice.glances += 1
    notice.save()
    return HttpResponse("sucessfully added glances")


def page_not_found(request):
    return render(request,"404.html")

def internal_server_error(request):
    return render(request,"500.html")
