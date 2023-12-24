from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView

from main.form import CustomerForm, NewsletterForm
from main.models import Newsletter, Customer
from main.services import time_task


class ChecksUser:
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Mailing Management'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Newsletter.objects.all()

        return context_data


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'main/customer_form.html'
    extra_context = {'title': 'Create Customer'}

    success_url = reverse_lazy('main:customer_list')

    def form_valid(self, form):
        if form.is_valid:
            new_client = form.save()
            new_client.owner = self.request.user
            new_client.save()

        return super().form_valid(form)


class CustomerListView(ListView):
    model = Customer
    extra_context = {'title': 'Customer List'}
    template_name = 'main/customer_list.html'

    def get_queryset(self):
        client = super().get_queryset()
        return client.filter(owner=self.request.user)


class CustomerDetailView(DetailView):
    model = Customer
    extra_context = {'title': 'Customer Details'}
    template_name = 'main/customer_detail.html'

    def test_func(self):
        objects = self.get_object()
        return self.request.user == objects.owner or self.request.user.is_superuser


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    extra_context = {'title': 'Update Customer'}

    def get_success_url(self):
        return reverse('main:customer_view', args=[self.kwargs.get('pk')])


class CustomerDeleteView(DeleteView):
    model = Customer
    extra_context = {'title': 'Delete Customer'}
    success_url = reverse_lazy('main:customer_list')


class NewsletterListView(ListView):
    model = Newsletter
    extra_context = {'title': 'Newsletter List'}
    template_name = 'main/newsletter_list.html'

    def get_queryset(self):
        if self.request.user.has_perm('mailing.deactivate_mailing') or self.request.user.is_superuser:
            mailing = super().get_queryset()
            return mailing
        else:
            mailing = super().get_queryset()
            return mailing.filter(owner=self.request.user)


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterForm
    extra_context = {'title': 'Create Newsletter'}
    success_url = reverse_lazy('main:newsletter_list')

    def form_valid(self, form):
        if form.is_valid():
            new_client = form.save()
            new_client.owner = self.request.user
            new_client.save()
        return super().form_valid(form)

    def get_queryset(self):
        return time_task()

    def get_form_kwargs(self):
        user_request = super().get_form_kwargs()
        user_request['user'] = self.request.user
        return user_request


class NewsletterDetailView(DetailView):
    model = Newsletter
    extra_context = {'title': 'Newsletter Details'}
    template_name = 'main/newsletter_detail.html'


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm

    extra_context = {'title': 'Update Newsletter'}

    def get_form_kwargs(self):
        user_request = super().get_form_kwargs()
        user_request['user'] = self.request.user
        return user_request
    def get_success_url(self):
        return reverse('main:newsletter_view', args=[self.kwargs.get('pk')])


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    extra_context = {'title': 'Delete Newsletter'}
    success_url = reverse_lazy('main:newsletter_list')





