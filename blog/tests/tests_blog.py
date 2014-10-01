from django.test import TestCase
from blog.models import Blog, BlogPost


class PracticeTestCase(TestCase):

    def test_blog(self):
        blog = Blog(title="test blog")
        blog.save()
        self.assertIsInstance(blog, Blog)

        blog_post = BlogPost(blog=blog, title="test post",
                content="this is content")
        blog_post.save()
        self.assertIsInstance(blog_post, BlogPost)

        get_by_slug = BlogPost.objects.get_by_slug(blog_post.slug)
        self.assertIsInstance(get_by_slug, BlogPost)

        homepage = BlogPost.objects.homepage_posts()
        self.assertEquals(len(homepage), 1)
