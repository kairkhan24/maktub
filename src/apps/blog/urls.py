from django.urls import path

from apps.blog.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
