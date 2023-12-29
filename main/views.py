from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView

from blog.models import Blog
from main.form import CustomerForm, NewsletterForm
from main.models import Customer, Newsletter, NewsletterLog
from main.services import time_task


class ChecksUser:
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'main/customer_form.html'
    success_url = reverse_lazy('main:customer_list')

    def form_valid(self, form):
        if form.is_valid:
            new_customer = form.save()
            new_customer.owner = self.request.user
            new_customer.save()

        return super().form_valid(form)


class CustomerListView(ChecksUser, ListView):
    model = Customer
    template_name = 'main/customer_list.html'

    def get_queryset(self):
        customer = super().get_queryset()
        return customer.filter(owner=self.request.user)


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'newsletter/customer_detail.html'

    def test_func(self):
        objects = self.get_object()
        return self.request.user == objects.owner or self.request.user.is_superuser


class CustomerDeleteView(LoginRequiredMixin, ChecksUser, DeleteView):
    model = Customer
    template_name = 'main/customer_confirm_delete.html'
    success_url = reverse_lazy('main:customer_list')


class CustomerUpdateView(LoginRequiredMixin, ChecksUser, UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('main:customer_list')


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = Customer
    template_name = 'main/newsletter_form.html'
    success_url = reverse_lazy('main:newsletter_list')

    def form_valid(self, form):
        if form.is_valid():
            new_customer= form.save()
            new_customer.owner = self.request.user
            new_customer.save()
        return super().form_valid(form)

    def get_queryset(self):
        return time_task()

    def get_form_kwargs(self):
        user_request = super().get_form_kwargs()
        user_request['user'] = self.request.user
        return user_request


class NewsletterListView(ListView):
    model = Newsletter
    template_name = 'main/news_list.html'

    def get_queryset(self):
        if self.request.user.has_perm('main.deactivate_newsletter') or self.request.user.is_superuser:
            newsletter = super().get_queryset()
            return newsletter
        else:
            newsletter = super().get_queryset()
            return newsletter.filter(owner=self.request.user)


class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = 'main/newsletter_detail.html'


class NewsletterDeleteView(LoginRequiredMixin, ChecksUser, DeleteView):
    model = Newsletter
    template_name = 'main/newsletter_confirm_delete.html'
    success_url = reverse_lazy('main:newsletter_list')


class NewsletterUpdateView(LoginRequiredMixin, ChecksUser, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('main:newsletter_list')

    def get_form_kwargs(self):
        user_request = super().get_form_kwargs()
        user_request['user'] = self.request.user
        return user_request


class NewsletterLogListView(ListView):
    model = NewsletterLog
    template_name = 'main/newsletter_report.html'


def contacts(request):
    return render(request, 'main/contacts.html')


class HomePageView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        blog = Blog.objects.all()[:3]  # выборка из базы данных 3 случайных записи Blog
        customers_count = len(Customer.objects.all())  # подсчёт кол-во клиентов
        newsletter_count = len(Newsletter.objects.all())  # подсчёт кол-во рассылок
        newsletter_active = len(Newsletter.objects.filter(status='started'))  # подсчёт кол-во активных рассылок
        context = super().get_context_data()
        context['newsletter_count'] = newsletter_count
        context['newsletter_active'] = newsletter_active
        context['customers_count'] = customers_count
        context['blogs'] = blog

        return context


@permission_required('newsletter.deactivate_newsletter')
def off(request, pk):
    """Контролер для отключения рассылок"""

    obj = Newsletter.objects.get(pk=pk)

    if obj.status == 'created' or 'started':
        obj.status = 'done'
        obj.save()

    return redirect(reverse('main:newsletter_list'))