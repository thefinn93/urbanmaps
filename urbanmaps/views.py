from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader
from django.shortcuts import render
from django.conf import settings
from django.core import serializers
import json

from urbanmaps.models import MapPoint

def index(request):
    points = MapPoint.objects.all().order_by('-pub_date')[:5]
    context = {
        'points': points,
        'cloudmade_key': settings.CLOUDMADE_KEY,
        'cloudmade_style': settings.CLOUDMADE_STYLE
        }
    return render(request, 'urbanmaps/index.html', context)

def info(request):
    if not "id" in request.GET:
        return HttpResponse("Please specify a marker id", status=400)
    else:
        try:
            data = serializers.serialize('json', MapPoint.objects.filter(pk=request.GET['id']))
            return HttpResponse(data)
        except MapPoint.DoesNotExist:
            return HttpResponse("Please specify a *valid*  marker id", status=400)
