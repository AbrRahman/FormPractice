from django.urls import path
from .import views
urlpatterns = [
    path('api_form/',views.api_forms,name="api_forms"),
    path("model_form/",views.model_forms,name="model_form")
]
