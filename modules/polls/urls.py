from django.urls import path
from .views import (
	IndexView,
	PreguntaDetail,
	PreguntaCreate,
	PreguntaUpdate,
	PreguntaDelete,
)


app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detalle/<int:pk>', PreguntaDetail.as_view(), name='detalle'),
    path('pregunta/create/', PreguntaCreate.as_view(), name='pregunta_create'),
    path('pregunta/update/<int:pk>', PreguntaUpdate.as_view(), name='pregunta_update'),
    path('pregunta/delete/<int:pk>', PreguntaDelete.as_view(), name='pregunta_delete'),
]
