from django.urls import path
from .views import (
	IndexView,
	PreguntaDetail,
)


app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detalle/<int:pk>', PreguntaDetail.as_view(), name='detalle'),
]
