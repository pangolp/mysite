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
    path(
    	route='',
    	view=IndexView.as_view(),
    	name='index'
    ),
    path(
    	route='detalle/<int:pk>',
    	view=PreguntaDetail.as_view(),
    	name='detalle'
    ),
    path(
    	route='pregunta/create/',
    	view=PreguntaCreate.as_view(),
    	name='pregunta_create'
    ),
    path(
    	route='pregunta/update/<int:pk>',
    	view=PreguntaUpdate.as_view(),
    	name='pregunta_update'
    ),
    path(
    	route='pregunta/delete/<int:pk>',
    	view=PreguntaDelete.as_view(),
    	name='pregunta_delete'
    ),
]
