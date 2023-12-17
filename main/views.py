from django.views.generic import TemplateView, ListView, DetailView

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


class CustomerListView(ListView):
    model = Customer
    extra_context = {'title': 'Customer'}


class CustomerDetailView(DetailView):
    model = Customer


class MessageListView(ListView):
    model = Message
    extra_context = {'title': 'Message'}


class MessageDetailView(DetailView):
    model = Message


class NewsletterListView(ListView):
    model = Newsletter
    extra_context = {'title': 'Newsletter'}


class NewsletterDetailView(DetailView):
    model = Newsletter





