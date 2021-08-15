from django.test import TestCase
from myblog.models import Tag, Post
from django.contrib.auth.models import User
from django.urls import reverse


# Create your tests here.
class TagTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='tag_for_test')

    def test_creation(self):
        tag = Tag.objects.create(name='tag_for_test')
        self.assertTrue(isinstance(tag, Tag))
        self.assertEqual(tag.name, 'tag_for_test')

    def test_str(self):
        self.assertEqual(self.tag.name, self.tag.__str__())


class PostTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username='tester',
            email='admin@tester.com',
            password='tester')
        self.post = Post.objects.create(
            title='Test Title',
            author=user,
            body='Test Body',
        )

    def test_creation(self):
        user = User.objects.create_superuser(
            username='tester2',
            email='admin2@tester.com',
            password='tester2')
        post = Post.objects.create(
            title='Creation Test Title',
            author=user,
            body='Creation Test Body',
        )
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.title, 'Creation Test Title')
        self.assertEqual(post.author, user)
        self.assertEqual(post.body, 'Creation Test Body')

    def test_str(self):
        self.assertEqual(self.post.title, self.post.__str__())

    def test_save(self):
        self.assertIsNotNone(self.post.modified_time)
        old_modified_time = self.post.modified_time
        self.post.body = 'New Body'
        self.post.save()
        # self.post.refresh_from_db()
        self.assertTrue(self.post.modified_time > old_modified_time)

    def test_get_absolute_url(self):
        expected = reverse('myblog:detail', kwargs={'pk': self.post.pk})
        self.assertEqual(self.post.get_absolute_url(), expected)
