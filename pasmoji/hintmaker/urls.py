from django.urls import path,include
from . import views

app_name='hintmaker'
urlpatterns=[

    path('hint_maker/',views.HintMakerView.as_view(),name='hintmaker'),
    path('',views.HomeView.as_view(),name='home'),
    path('edit/<int:id>',views.EditView.as_view(),name='edit'),



]