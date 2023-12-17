from django.urls import path

from main.views import IndexView, CustomerListView, NewsletterListView, NewsletterDetailView, CustomerDetailView, \
    MessageListView, MessageDetailView

from main.apps import MainConfig

app_name = MainConfig.name


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('customer/', CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_view'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_view'),
    path('newsletter/', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_view'),


]
