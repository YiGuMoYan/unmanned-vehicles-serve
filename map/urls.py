from django.urls import path

from .views import *

urlpatterns = [
    path("create/", create),
    path("get_list/", get_list),
    path("delete/", delete),
    path("only/", only),
    path("algorithm/", get_algorithm_list),
    path("detail/", detail),
    path("video/", video),
    path("globalDef/", globalDef),
    path("localDef/", localDef),
]
