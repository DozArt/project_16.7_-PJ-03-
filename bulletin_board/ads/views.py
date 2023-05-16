from django.views.generic import ListView, DetailView, CreateView

from .forms import AdForm
from .models import Ads, Response


class AdsList(ListView):
    model = Ads
    ordering = 'date_create'
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 2


class AdDetail(DetailView):
    model = Ads
    template_name = 'ad.html'
    context_object_name = 'ad'


class AdCreate(CreateView):
    form_class = AdForm
    model = Ads
    template_name = 'ad_create.html'


class ResponseList(ListView):
    model = Response
    ordering = 'id'
    template_name = 'Response.html'
    context_object_name = 'response'
    paginate_by = 2
