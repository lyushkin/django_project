from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from blog.models import Category, Post, Author, User, Comments


def index(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    users = User.objects.all()
    commentss = User.objects.all()
    users_list = []
    for i in commentss:
        comment = Comments.objects.filter(user_id=i.id)
        if comment:
            users_list.append(i.id)
    kom = commentss.filter(id__in=users_list)

    try:
        category_fan = Category.objects.get(title='Фантастика')
    except ObjectDoesNotExist:
        raise ValueError('Такой категори не существует!')

    params = {'categories': categories,
            'fan': category_fan, 'authors': authors, 'users': kom}
    return render(request, 'index.html', params)


def category(request, pk):
    posts = Post.objects.filter(category_id=pk)
    return render(request, 'category.html', locals())


def author(request, pk):
    posts = Post.objects.filter(author_id=pk)
    params = {'posts': posts}
    return render(request, 'author_posts.html', params)


def comments(request, pk):
    _comments = Comments.objects.filter(user_id=pk)
    return (render(request, 'comments.html', {'comments':_comments}))

