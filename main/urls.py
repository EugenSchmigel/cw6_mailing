from django.urls import path

from main.views import HomePageView, CustomerListView, NewsletterListView, NewsletterDetailView, CustomerDetailView, \
    CustomerUpdateView, CustomerDeleteView, \
    NewsletterUpdateView, NewsletterDeleteView, CustomerCreateView, HomePageView, NewsletterCreateView, NewsletterLogsListView

from main.apps import MainConfig

app_name = MainConfig.name


urlpatterns = [

    path('', HomePageView.as_view(), name='index'),

    path('customer/create/', CustomerCreateView.as_view(), name='create_customer'),
    path('customer/', CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_view'),
    path('customer/edit/<int:pk>/', CustomerUpdateView.as_view(), name='edit_customer'),
    path('customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='delete_customer'),

    path('newsletter/create/', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('newsletter/', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_view'),
    path('newsletter/edit/<int:pk>/', NewsletterUpdateView.as_view(), name='edit_newsletter'),
    path('newsletter/delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),
    path('logs/', NewsletterLogsListView.as_view(), name='logs_list'),
]
