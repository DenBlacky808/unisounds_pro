from django.shortcuts import render

from mainapp.models import Track


def show_admin_custom_page(request):
    # some code
    tracks = Track.objects.all()[:8]
    content = {
        'tracks': tracks
    }
    return render(request, 'statapp/admin_custom_page.html', content)
