from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from mainapp.models import Track, TrackCategory
from django.templatetags.static import static
import os
from django.urls import include, path


def blog(request, pk):
    links_menu = TrackCategory.objects.all()

    if pk == 0:
        category = {
            'pk': 0,
            'name': 'all'
        }
        tracks = Track.objects.all()
    else:
        category = get_object_or_404(TrackCategory, pk=pk)
        tracks = Track.objects.filter(category__name=category)
    content = {
        'category': category,
        'tracks': tracks,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/blog.html', content)


def main(request):
    links_menu = TrackCategory.objects.all()
    tracks = Track.objects.all()
    content = {
        'tracks': tracks,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/blog.html', content)


def download_count(request, pk):
    track_inst = get_object_or_404(Track, pk=pk)
    track_inst.download_counter += 1
    track_inst.save()

    file_path = os.path.join(settings.MEDIA_ROOT, str(track_inst.download_link))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404