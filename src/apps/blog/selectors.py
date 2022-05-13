from typing import List

from django.shortcuts import get_object_or_404

from apps.blog.models import Post, Category


def list_posts() -> List[Post]:
    qs = Post.objects.all()
    return qs


def get_post_by_slug(*,
                     post_slug: str,
                     raise_exception: bool = True,
                     ) -> Post:
    if raise_exception:
        post = get_object_or_404(Post, slug=post_slug)
    else:
        post = Post.objects.filter(slug=post_slug).first()
    return post


def list_categories() -> List[Category]:
    qs = Category.objects.all()
    return qs
