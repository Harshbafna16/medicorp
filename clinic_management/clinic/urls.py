from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('prescription/', views.prescription, name='prescription'),
    path('doctor-info/', views.doctor_info, name='doctor_info'),
    path('video-call/', views.video_call, name='video_call'),  # New URL
    path("video_call/<str:room_name>/", views.video_call, name="video_call"),
]
