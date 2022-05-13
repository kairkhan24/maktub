from django.shortcuts import render
from django.views import View

from apps.blog.selectors import list_posts, list_categories


class IndexView(View):
    def get(self, request):
        posts = list_posts()
        categories = list_categories()
        context = {
            'categories': categories,
            'posts': posts
        }
        return render(request, 'index.html', context)
