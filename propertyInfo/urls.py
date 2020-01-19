# from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.main_screen),
    path('property/new/', views.PropertyCreate.as_view(), name='property_new'),
    path('property/<str:slug>/', views.PropertyDetail.as_view(), name='property_detail'),
    path('property/<str:slug>/edit/', views.PropertyEdit.as_view(), name='property_edit'),
    # path('update_content/', views.update_content, name='update_content'),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
