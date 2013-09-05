from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader
from django.shortcuts import render
from django.conf import settings

from urbanmaps.models import MapPoint

def index(request):
    points = MapPoint.objects.all().order_by('-pub_date')[:5]
    context = {
        'points': points,
        'cloudmade_key': settings.CLOUDMADE_KEY,
        'cloudmade_style': settings.CLOUDMADE_STYLE
        }
    return render(request, 'urbanmaps/index.html', context)
