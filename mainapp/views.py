from django.shortcuts import render, get_object_or_404

from mainapp.models import Track, TrackCategory


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








