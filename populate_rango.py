import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page
def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         "views": 132,
         'url': 'http://docs.python.org/3/tutorial/'},
        {'title': 'How to Think like a Computer Scientist',
         "views": 72,
         'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title': 'Learn Python in 10 Minutes',
         "views": 30,
         'url': 'http://www.korokithakis.net/tutorials/python/'}]
    django_pages = [
        {'title': 'Official Django Tutorial',
         "views": 70,
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title': 'Django Rocks',
         "views": 64,
         'url': 'http://www.djangorocks.com/'},
        {'title': 'How to Tango with Django',
         "views": 14,
         'url': 'http://www.tangowithdjango.com/'}]
    other_pages = [
        {'title': 'Bottle',
         "views": 10,
         'url': 'http://bottlepy.org/docs/dev/'},
        {'title': 'Flask',
         "views": 18,
         'url': 'http://flask.pocoo.org'}]
    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}}
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data['pages']:
            add_page(c, p["title"], p["url"], p["views"])
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p
def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()