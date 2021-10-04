from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Urls
from .forms import UrlForm
from django.contrib.sites.models import Site

def url_create(request):
    current_site = Site.objects.get_current()
    domain = 'http://127.0.0.1:8000'
    shorten_url = ''

    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save()
            shorten_url = f"{domain}/{url.short_code}"
    else:
        form = UrlForm()

    context = {
        "form": form,
        'shorten_url': shorten_url
    }

    return render(request, 'urlApi/create.html', context)


def url_redirect(request, short_code):
    url = get_object_or_404(Urls, short_code=short_code)

    return HttpResponseRedirect(url.url)
