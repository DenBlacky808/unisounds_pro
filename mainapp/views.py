from django.shortcuts import render

from mainapp.models import Track


def main(request):
    tracks = Track.objects.all()
    content = {
        'tracks': tracks
    }
    return render(request, 'mainapp/index.html', content)


def blog(request):
    tracks = Track.objects.all()
    content = {
        'tracks': tracks
    }
    return render(request, 'mainapp/blog.html', content)
