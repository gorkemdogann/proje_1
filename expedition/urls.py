from django.contrib import admin
from django.urls import path
from . import views

app_name = "expedition"

urlpatterns = [
    path('dashboard/',views.Dashboard, name='dashboard'),
    path('addexpedition/',views.addExpedition, name='addexpedition'),
    path('expedition/<int:id>',views.Detail, name='detail'),
    path('update/<int:id>',views.UpdateExpedition, name='update'),
    path('delete/<int:id>',views.DeleteExpedition, name='delete'),
    path('firma_list/<str:firma>',views.firma_list, name='firma_list'),
    path('chart/',views.chart, name="chart"),


]
