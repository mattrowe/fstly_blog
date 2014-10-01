from blog.forms import BlogPostForm
from blog.models import BlogPost
from django.core.urlresolvers import reverse
from django.http import HttpResponse, QueryDict
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from django.views.generic.base import TemplateView
import json


class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['blog_posts'] = BlogPost.objects.homepage_posts()

        return context


class DetailView(TemplateView):

    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['post'] = BlogPost.objects.get_by_slug(kwargs.get('slug'))
        return context


class EditView(View):


    def get(self, request, **kwargs):
        template_data = {}

        if 'post_id' in kwargs:
            template_data['post'] = BlogPost.objects.get(
                id=int(kwargs.get('post_id')))
        else:
            template_data['post'] = None
        template_data['form'] = BlogPostForm(instance=template_data['post'])
        return render_to_response(
            'edit.html', template_data,
            context_instance=RequestContext(request))

    def _process_post(self, form):
        if form.is_valid():
            post = form.save()
            response_data = {
                'redirect_to': reverse('DetailView', None, [str(post.id)])
            }
            status = 201
        else:
            response_data = form.errors
            status = 400

        return HttpResponse(json.dumps(response_data),
                content_type="application/json", status=status)


    def post(self, request, **kwargs):
        # this is an edit
        post = BlogPost.objects.get(id=int(kwargs.get('post_id')))
        form = BlogPostForm(request.POST, instance=post)
        return self._process_post(form)


    def put(self, request, **kwargs):
        # this is a new post
        form = BlogPostForm(QueryDict(request.body))
        return self._process_post(form)


    def delete(self, request, **kwargs):
        # remove the post
        post = BlogPost.objects.get(id=int(kwargs.get('post_id')))
        post.delete()
        response_data = {
            'redirect_to': reverse('HomeView', None)
        }
        return HttpResponse(json.dumps(response_data),
                content_type="application/json", status=201)
