from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.delete, name='delete'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('task-completed/<int:id>', views.taskCompleted, name='task-completed'),

]