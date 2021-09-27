from django.urls  import path
from . import views


app_name = "free_answer"



urlpatterns = [
    path("<uuid:pk>/start_aggregate/", views.StartAggregate.as_view(), name="start_aggregate"),
    path("<uuid:pk>/end_aggregate/", views.EndAggregate.as_view(), name="end_aggregate")

]
