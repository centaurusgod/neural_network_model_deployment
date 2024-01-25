from django.urls import path, include
from mlapi import views

urlpatterns = [
    path('', views.BirdStatusAPIView.as_view()),
    path('birds_detail', views.BirdsDetailAPIView.as_view()),
    path('node_device', views.NodeDeviceAPIView.as_view())
    # path('post_bird_image/', views.post_bird_image, name='post_bird_image'),
    # path('update_bird_image/<id>', views.update_bird_image, name='update_bird_image'),
    # path('delete_bird_image/<id>', views.delete_bird_image, name='delete_bird_image')

]
