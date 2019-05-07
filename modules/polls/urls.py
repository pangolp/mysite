from django.urls import path
from .views import (
	IndexView,
	PreguntaDetail,
	PreguntaCreate,
)


app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detalle/<int:pk>', PreguntaDetail.as_view(), name='detalle'),
    path('pregunta/create/', PreguntaCreate.as_view(), name='pregunta_create'),
]
