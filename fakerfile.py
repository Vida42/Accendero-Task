from faker import Faker
from django.utils import timezone
import os
import django


def createTags():
    try:
        User.objects.get(username='faker')
    except User.DoesNotExist:
        User.objects.create_superuser('faker', 'faker@test.com', 'faker')
        possible_tags = ['Django', 'Python', 'Faker', 'Numpy', 'SQL', 'JS', 'Markdown', 'CSS', 'HTML', 'OS']
        for tag in possible_tags:
            Tag.objects.create(name=tag)


def createFakePost():
    fake = Faker()
    Faker.seed(42)
    author = User.objects.get(username='faker')
    for _ in range(10):
        tags = Tag.objects.order_by('?')
        tag1, tag2, tag3 = tags[0], tags[2], tags[5]
        created_time = fake.date_time_between(start_date='-1y', end_date="now",
                                              tzinfo=timezone.get_current_timezone())
        new_post = Post.objects.create(
            title=fake.sentence(),
            author=author,
            body='\n\n'.join(fake.paragraphs(nb=5)),
            created_time=created_time,
        )
        new_post.tags.add(tag1, tag2, tag3)
        new_post.save()


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproj.settings")
    django.setup()
    from myblog.models import Tag, Post
    from django.contrib.auth.models import User
    createTags()
    print('Created tags.')
    createFakePost()
    print('Created some faked posts.')
