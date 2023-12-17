from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView

from main.models import Newsletter, Customer, Message


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
    extra_context = {'title': 'Create Customer'}
    fields = ('fio', 'email', 'comment', )
    success_url = reverse_lazy('main:customer_list')


class CustomerListView(ListView):
    model = Customer
    extra_context = {'title': 'Customer List'}


class CustomerDetailView(DetailView):
    model = Customer
    extra_context = {'title': 'Customer Details'}


class CustomerUpdateView(UpdateView):
    model = Customer
    extra_context = {'title': 'Update Customer'}
    fields = ('fio', 'email', 'comment', )

    def get_success_url(self):
        return reverse('main:customer_view', args=[self.kwargs.get('pk')])


class CustomerDeleteView(DeleteView):
    model = Customer
    extra_context = {'title': 'Delete Customer'}
    success_url = reverse_lazy('main:customer_list')


class MessageCreateView(CreateView):
    model = Message
    extra_context = {'title': 'Create Message'}
    fields = ('message_subject', 'message_body',)
    success_url = reverse_lazy('main:message_list')


class MessageListView(ListView):
    model = Message
    extra_context = {'title': 'Message List'}


class MessageDetailView(DetailView):
    model = Message
    extra_context = {'title': 'Message Details'}


class MessageUpdateView(UpdateView):
    model = Message
    extra_context = {'title': 'Update Message'}
    fields = ('message_subject', 'message_body',)

    def get_success_url(self):
        return reverse('main:message_view', args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    model = Message
    extra_context = {'title': 'Delete Message'}
    success_url = reverse_lazy('main:message_list')


class NewsletterListView(ListView):
    model = Newsletter
    extra_context = {'title': 'Newsletter List'}


class NewsletterCreateView(CreateView):
    model = Newsletter
    extra_context = {'title': 'Create Newsletter'}
    fields = ('customer', 'message', 'interval', 'status', )
    success_url = reverse_lazy('main:newsletter_list')


class NewsletterDetailView(DetailView):
    model = Newsletter
    extra_context = {'title': 'Newsletter Details'}


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    extra_context = {'title': 'Update Newsletter'}
    fields = ('customer', 'message', 'interval', 'status', )

    def get_success_url(self):
        return reverse('main:newsletter_view', args=[self.kwargs.get('pk')])


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    extra_context = {'title': 'Delete Newsletter'}
    success_url = reverse_lazy('main:newsletter_list')





