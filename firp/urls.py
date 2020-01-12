from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('fir/',views.FirView.as_view(),name='view-fir'),
    path('add/',views.AddFIRView.as_view(),name='add-fir'),
    path('logout/',views.LogoutView.as_view(),name='logout')
]
