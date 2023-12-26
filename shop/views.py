from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import Post, Category, Publisher, Author


class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        authors = Author.objects.all()
        return render(request, 'posts.html', {'posts': posts, 'authors': authors})


class AddPostView(View):
    def get(self, request):
        categories = Category.objects.all()
        authors = Author.objects.all()
        publishers = Publisher.objects.all()
        return render(request, 'add_post.html',
                      {'categories': categories, 'authors': authors, 'publishers': publishers})

    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        publisher_id = request.POST.get('publisher')
        authors_ids = request.POST.getlist('authors')

        category = Category.objects.get(id=category_id)
        publisher = Publisher.objects.get(id=publisher_id)
        post = Post(title=title, content=content, category=category, publisher=publisher)
        post.save()

        for author_id in authors_ids:
            author = Author.objects.get(id=author_id)
            post.authors.add(author)

        return redirect('posts')


class EditPostView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        categories = Category.objects.all()
        authors = Author.objects.all()
        publishers = Publisher.objects.all()
        return render(request, 'edit_post.html',
                      {'post': post, 'categories': categories, 'authors': authors, 'publishers': publishers})

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        publisher_id = request.POST.get('publisher')
        authors_ids = request.POST.getlist('authors')

        category = Category.objects.get(id=category_id)
        publisher = Publisher.objects.get(id=publisher_id)

        post.title = title
        post.content = content
        post.category = category
        post.publisher = publisher
        post.authors.clear()

        for author_id in authors_ids:
            author = Author.objects.get(id=author_id)
            post.authors.add(author)

        post.save()
        return redirect('posts')


def posts(request):
    posts = Post.objects.all()
    authors = Author.objects.all()

    return render(request, 'posts.html', {'posts': posts, 'authors': authors})


def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        publisher_id = request.POST.get('publisher')

        authors_ids = request.POST.getlist('authors')

        category = Category.objects.get(id=category_id)
        publisher = Publisher.objects.get(id=publisher_id)
        post = Post(title=title, content=content, category=category, publisher=publisher)
        post.save()

        for author_id in authors_ids:
            author = Author.objects.get(id=author_id)
            post.authors.add(author)

        return redirect('posts')

    categories = Category.objects.all()
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'add_post.html', {'categories': categories, 'authors': authors, 'publishers': publishers})


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        publisher_id = request.POST.get('publisher')
        authors_ids = request.POST.getlist('authors')

        category = Category.objects.get(id=category_id)
        publisher = Publisher.objects.get(id=publisher_id)

        post.title = title
        post.content = content
        post.category = category
        post.publisher = publisher
        post.authors.clear()

        for author_id in authors_ids:
            author = Author.objects.get(id=author_id)
            post.authors.add(author)

        post.save()
        return redirect('posts')

    categories = Category.objects.all()
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'edit_post.html',
                  {'post': post, 'categories': categories, 'authors': authors, 'publishers': publishers})


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts')


def popular_posts(request):
    return HttpResponse("Популярные посты")


def latest_posts(request):
    return HttpResponse("Последние опубликованные посты")


def post_details(request, post_id):
    return HttpResponse(f"Детали поста {post_id}")


def post_comments(request, post_id):
    return HttpResponse(f"Комментарии поста {post_id}")


def post_likes(request, post_id):
    return HttpResponse(f"Лайки поста {post_id}")


def home(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        return HttpResponse(f"Логин: {username}, Пароль: {password}")
    return HttpResponse("Добро пожаловать на главную страницу")


def about(request):
    return HttpResponseRedirect('/about/')


def contacts(request):
    return HttpResponseRedirect('/contacts/')


def page_not_found(request, exception):
    return HttpResponse("Загрузка страницы была завершена ошибкой", status=404)


def access(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    if username == 'admin' and password == 'admin':
        return HttpResponse("Все норм")
    return HttpResponse("Доступ запрещен")


def json_page(request):
    data = {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }
    return JsonResponse(data)


def set_cookie(request):
    response = HttpResponse("Cookie установлен")
    response.set_cookie('mycookie', 'Hello, world!')
    return response


def get_cookie(request):
    mycookie = request.COOKIES.get('mycookie')
    return HttpResponse(f"Значение cookie: {mycookie}")
