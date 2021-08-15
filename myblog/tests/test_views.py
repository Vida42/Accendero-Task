from django.test import TestCase
from myblog.models import Tag, Post
from django.contrib.auth.models import User
from django.urls import reverse


class DummyTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='tester',
            email='admin@tester.com',
            password='tester')

        self.tag1 = Tag.objects.create(name='tag1_for_test')
        self.tag2 = Tag.objects.create(name='tag2_for_test')

        self.post1 = Post.objects.create(
            title='Test Title1',
            author=self.user,
            body='Test Body1',
        )
        self.post1.tags.add(self.tag1)
        self.post1.save()

        self.post2 = Post.objects.create(
            title='Test Title2',
            author=self.user,
            body='# H1\n\n## H2\n\n**Bold**\n\n*Italic*',
        )


class HomeViewTestCase(DummyTestCase):
    def setUp(self):
        super().setUp()
        self.url1 = reverse("myblog:home")

    def test_post(self):
        resp = self.client.get(self.url1)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("post_list", resp.context)
        self.assertIn("date_list", resp.context)
        self.assertIn("tag_list", resp.context)
        self.assertIn("page_obj", resp.context)
        self.assertEqual(resp.context["post_list"].count(), 2)

    def test_no_post(self):
        Post.objects.all().delete()
        resp = self.client.get(self.url1)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'No post for now!')


class DetailViewTestCase(DummyTestCase):
    def setUp(self):
        super().setUp()
        self.url1 = reverse('myblog:detail', kwargs={'pk': self.post1.pk})
        self.url2 = reverse('myblog:detail', kwargs={'pk': self.post2.pk})

    def test_post(self):
        resp = self.client.get(self.url1)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("post", resp.context)
        self.assertContains(resp, 'Test Title1')

    def test_no_post(self):
        Post.objects.all().delete()
        resp = self.client.get(self.url1)
        self.assertEqual(resp.status_code, 404)

    def test_markdown(self):
        resp = self.client.get(self.url2)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("post", resp.context)
        self.assertContains(resp, 'Test Title2')
        element = resp.context["post"].body
        expected = """<h1>H1</h1>
        <h2>H2</h2>
        <p><strong>Bold</strong></p>
        <p><em>Italic</em></p>"""
        self.assertHTMLEqual(element, expected)

    def test_blog_views(self):
        self.client.get(self.url1)
        self.assertEqual(self.post1.blog_views, 0)
        self.post1.refresh_from_db()
        self.assertEqual(self.post1.blog_views, 1)
        self.client.get(self.url1)
        self.post1.refresh_from_db()
        self.assertEqual(self.post1.blog_views, 2)


class AboutViewTestCase(DummyTestCase):
    def setUp(self):
        super().setUp()
        self.url1 = reverse("myblog:about")

    def test_about(self):
        resp = self.client.get(self.url1)
        self.assertEqual(resp.status_code, 200)
        expected = "This is a blog application building with Django."
        self.assertContains(resp, expected)


class ArchiveViewTestCase(DummyTestCase):
    def setUp(self):
        super().setUp()
        self.url1 = reverse("myblog:archive", kwargs={
            'year': self.post1.created_time.year,
            'month': self.post1.created_time.month
        })
        self.url2 = reverse("myblog:archive", kwargs={
            'year': 2030,
            'month': 8
        })

    def test_archive_with_no_post(self):
        resp = self.client.get(self.url2)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'No post for now!')

    def test_archive_with_post(self):
        resp = self.client.get(self.url1)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("post_list", resp.context)
        self.assertIn("date_list", resp.context)
        self.assertIn("tag_list", resp.context)
        self.assertIn("page_obj", resp.context)
        self.assertEqual(resp.context["post_list"].count(), 2)


class TagViewTestCase(DummyTestCase):
    def setUp(self):
        super().setUp()
        self.url1 = reverse("myblog:tag", kwargs={'tag_pk': self.tag1.pk})
        self.url2 = reverse("myblog:tag", kwargs={'tag_pk': self.tag2.pk})

    def test_tag_with_no_post(self):
        resp = self.client.get(self.url2)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'No post for now!')

    def test_tag_with_post(self):
        resp = self.client.get(self.url1)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("post_list", resp.context)
        self.assertIn("date_list", resp.context)
        self.assertIn("tag_list", resp.context)
        self.assertIn("page_obj", resp.context)
        self.assertEqual(resp.context["post_list"].count(), 1)
