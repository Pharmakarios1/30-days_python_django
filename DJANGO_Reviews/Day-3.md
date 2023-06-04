## DAY 3
1. Creating views
2.mapping urls to views

To create views in Django, you need to follow these steps:

1. Create a new Python file in your Django project directory (or open an existing one) and import the necessary dependencies:

python
from django.shortcuts import render
from django.http import HttpResponse


2. Define your view function. A view function receives an HTTP request as its first argument and returns an HTTP response. You can define any additional arguments you need.

python
def my_view(request):
    # View logic goes here
    return HttpResponse("Hello, World!")


3. Map the URL to your view function in the `urls.py` file of your Django app. If the `urls.py` file does not exist, create it in your app's directory. Import your view function and add a URL pattern that maps to it.

python
from django.urls import path
from .views import my_view

urlpatterns = [
    path('my-view/', my_view, name='my-view'),
]


In this example, any requests with the URL pattern `my-view/` will be handled by the `my_view` function.

4. Finally, include the URLs of your app in the main `urls.py` file of your project. This file is usually located in the project's directory. Import the `include` function from `django.urls` and add a path that includes the URLs of your app.

python
from django.urls import include, path

urlpatterns = [
    # Other URL patterns
    path('my-app/', include('myapp.urls')),
]


In this example, all URLs starting with `my-app/` will be handled by the URLs defined in `myapp.urls`.

That's it! You've successfully created a view in Django. When you visit the corresponding URL, Django will invoke your view function and return the HTTP response defined in the function.