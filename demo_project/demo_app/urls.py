from django.urls import path
from.views import display_table


urlpatterns = [
    path('', display_table, name = "display_table")
    ]