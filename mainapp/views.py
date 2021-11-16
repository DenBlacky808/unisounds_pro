from django.shortcuts import render

from mainapp.models import Track


def blog(request):
    tracks = Track.objects.all()
    content = {
        'tracks': tracks
    }
    return render(request, 'mainapp/blog.html', content)
