from django.conf.urls import url
from django.contrib.auth.decorators import user_passes_test

from .views import show_admin_custom_page

urlpatterns = [
    url(r'^admin-custom-page/$', user_passes_test(lambda u: u.is_superuser)(show_admin_custom_page), name='show_admin_custom_page'),
]
