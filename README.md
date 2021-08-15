# Accendero-Task


## TASK

> Using languages of your choice, build a full-stack web application, demonstrating an application that can have persistent state of some sort and allow a change in data.

Build a personal blog, it allows user to create blog with Markdown. Every post has title, author, summary, body, created_time, modified_time and tags.

See home page showed below.

![Home Page](https://github.com/Vida42/Accendero-Task/tree/main/res/home.png)

## TESTING

> You must demonstrate proper test cases for your code. Please provide examples of both unit and integration testing.

### Unit test

All unit tests are done inside `./myblog/tests`

For example:

```python
# myblog/tests/test_views/AboutViewTestCase

class AboutViewTestCase(DummyTestCase):
    def setUp(self):
        super().setUp()
        self.url1 = reverse("myblog:about")

    def test_about(self):
        resp = self.client.get(self.url1)
        self.assertEqual(resp.status_code, 200)
        expected = "This is a blog application building with Django."
        self.assertContains(resp, expected)
```

### Integration Test

We use [coverage](https://coverage.readthedocs.io/en/coverage-5.0.3/index.html) as the tool to do integration test. To use it, go to the root folder first, then:

- Run `coverage run manage.py test myblog/tests` to do the coverage test.

- Run `coverage html` to generate report

Report looks like:

![coverage](https://github.com/Vida42/Accendero-Task/tree/main/res/coverage.png)


## RUN

- First, users need to install `Python 3.9.1` in their computers.

- Then install required packages. You can simply install these packages saved in `requirements.txt`. Go to project root folder(where manage.py locates), run `pip install -r requirements.txt` in your command prompt.

- Run `python manage.py makemigrations` to create migrations for any change.

- Run `python manage.py migrate` to apply those changes to the database.

- To run this client, run `python manage.py runserver`.

### Fill in Posts

You have two ways to inspect what it looks like with posts filled in:

1. Creating an admin user

> see details [here](https://docs.djangoproject.com/en/3.2/intro/tutorial02/#creating-an-admin-user)

```python
python manage.py createsuperuser
```

2. Go to root folder first, then run:

```python
python fakerfile.py
```

This command will generate 10 posts with author name `faker`.

Now you can run `python manage.py runserver` again to see the blog.

## REFERENCE

https://docs.djangoproject.com/en/3.2/ref/contrib/admin/

https://www.geeksforgeeks.org/overriding-the-save-method-django-models/

https://docs.djangoproject.com/en/3.2/topics/http/urls/

https://stackoverflow.com/questions/2345708/how-can-i-get-the-full-absolute-url-with-domain-in-django

https://stackoverflow.com/questions/42469306/how-to-redirect-404-requests-to-homepage-in-django-single-page-app-using-nginx/42469671

https://riptutorial.com/django/example/32472/use-of----extends---------include----and----blocks---

https://stackoverflow.com/questions/62823120/html-not-rendering-well-when-using-markdown2-converted

https://stackoverflow.com/questions/47718880/syntax-highlight-font-colour-doesnt-change

https://stackoverflow.com/questions/3907628/how-do-you-limit-list-objects-template-side-rather-than-view-side

https://stackoverflow.com/questions/68775869/support-for-password-authentication-was-removed-please-use-a-personal-access-to

https://stackoverflow.com/questions/7737146/how-can-i-change-the-default-django-date-template-format

https://stackoverflow.com/questions/57590142/how-to-format-djangos-timezone-now

https://djangobook.com/mdj2-advanced-models/

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.dates

https://stackoverflow.com/questions/4668619/how-do-i-filter-query-objects-by-date-range-in-django

https://stackoverflow.com/questions/52425711/how-to-add-a-page-view-count-for-django-detail-view

https://docs.djangoproject.com/en/3.2/topics/pagination/

https://www.youtube.com/watch?v=PqXWWu2U_TI

https://stackoverflow.com/questions/3090302/how-do-i-get-the-object-if-it-exists-or-none-if-it-does-not-exist-in-django

https://stackoverflow.com/questions/22816704/django-get-a-random-object

https://docs.djangoproject.com/en/3.2/topics/testing/overview/

https://realpython.com/testing-in-django-part-1-best-practices-and-examples/

https://docs.djangoproject.com/en/3.2/topics/testing/advanced/#integration-with-coverage-py

https://stackoverflow.com/questions/17536916/python-django-how-to-assert-that-unit-test-result-contains-a-certain-string

https://stackoverflow.com/questions/56048573/how-do-i-verify-in-a-django-unit-test-that-my-context-contains-a-form-object

https://stackoverflow.com/questions/4377861/reload-django-object-from-database

