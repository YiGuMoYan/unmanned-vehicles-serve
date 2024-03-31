from django.urls import path

from .views import *

urlpatterns = [
    path("create/", create),
    path("classify/", get_classify_list),
    path("delete/", delete),
    path("list/", get_list),
]