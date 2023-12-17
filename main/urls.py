from django.urls import path

from main.views import IndexView, CustomerListView, NewsletterListView, NewsletterDetailView, CustomerDetailView, \
    MessageListView, MessageDetailView, CustomerUpdateView, CustomerDeleteView, MessageUpdateView, MessageDeleteView, \
    NewsletterUpdateView, NewsletterDeleteView, CustomerCreateView, MessageCreateView, NewsletterCreateView

from main.apps import MainConfig

app_name = MainConfig.name


urlpatterns = [

    path('', IndexView.as_view(), name='index'),

    path('customer/create/', CustomerCreateView.as_view(), name='create_customer'),
    path('customer/', CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_view'),
    path('customer/edit/<int:pk>/', CustomerUpdateView.as_view(), name='edit_customer'),
    path('customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='delete_customer'),

    path('message/create/', MessageCreateView.as_view(), name='create_message'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_view'),
    path('message/edit/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    path('newsletter/create/', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('newsletter/', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_view'),
    path('newsletter/edit/<int:pk>/', NewsletterUpdateView.as_view(), name='edit_newsletter'),
    path('newsletter/delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),


]
