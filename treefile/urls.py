from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('Lifetree-Healthcare-And-Diagnostics', views.index, name="index-page"),
    path('About-Lifetree-Healthcare-And-Diagnostics', views.about, name="about-page"),
    path('Meet-the-team-of-Lifetree-Healthcare-And-Diagnostics', views.team, name="team-page"),
    path('View-gallery-of-Lifetree-Healthcare-And-Diagnostics', views.galleryPage, name="gallery-page"),
    path('blog-Lifetree-Healthcare-And-Diagnostics', views.blogi, name="blog-page"),
    path('Contact-Lifetree-Healthcare-And-Diagnostics', views.contact, name="contact-page"),
    path('Team-Detail/<int:id>/<str:name>/', views.teamDetail),
    path('Service-Detail/<int:id>/<str:name>/', views.servicedetail),
    path('Blog-Detail/<int:id>/<str:name>/', views.blogdetail),
]