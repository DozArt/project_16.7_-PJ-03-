from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import ResponseFilter
from .forms import AdForm, ResponseForm
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

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        return super().form_valid(form)


class AdUpdate(UpdateView):
    form_class = AdForm
    model = Ads
    template_name = 'ad_update.html'


class AdDelete(DeleteView):
    model = Ads
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ads_list')


class ResponseList(ListView):
    model = Response
    ordering = 'id'
    template_name = 'response.html'
    context_object_name = 'responses'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ResponseCreate(CreateView):
    form_class = ResponseForm
    model = Response
    template_name = 'response_create.html'

    def responses_create(self, ad):
        self.group = Ads.objects.get(id=ad)

    def form_valid(self, form):
        response = form.save(commit=False)
        response.author = self.request.user
        response.ads = self.group  # все еще не работает
        return super().form_valid(form)
