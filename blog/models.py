from django.db import models


class BlogManager(models.Manager):
    pass


class BlogPostManager(models.Manager):

    def homepage_posts(self):
        # REVISIT: add pagination here
        return self.all().order_by('-id')

    def get_by_slug(self, slug):
        return self.filter(id=int(slug))[0]


class Blog(models.Model):

    title = models.CharField(max_length=255)
    objects = BlogManager()

    def __unicode__(self):
        return self.title


class BlogPost(models.Model):

    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255)
    content = models.TextField()
    objects = BlogPostManager()

    def __unicode__(self):
        return self.title

    @property
    def slug(self):
        return self.id
