# core django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import TemplateView

# Project guia imports
from home.models import Post
from collection.models import Collection
from exhibition.models import Exhibition
from publication.models import Publication
from event.models import Event
from person.models import Person


def login(request):
    return render(request, 'login.html')


class PostList(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['collection_total'] = Collection.objects.all().count()
        if (Post.objects.order_by('id_auto_series').exists()):
            post = Post.objects.latest('capture')
            context['first_image_id'] = post.capture.first().id_auto_series
            image_list = [str(index) for index in range(post.capture.count())]
            context['image_list'] = image_list
        else:
            context['first_active_image'] = ''

        return context

    def collection_total(self):
        collection_total = Collection.objects.all().count()
        return collection_total

    def exhibition_total(self):
        exhibition_total = Exhibition.objects.all().count()
        return exhibition_total

    def publication_total(self):
        publication_total = Publication.objects.all().count()
        return publication_total

    def event_total(self):
        event_total = Event.objects.all().count()
        return event_total

    def person_total(self):
        person_total = Person.objects.all().count()
        return person_total
