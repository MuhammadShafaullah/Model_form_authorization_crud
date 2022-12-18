
from django.contrib import admin
from django.urls import path,include
from Crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home' ),
    path('delete/<int:id>/',views.delete_data,name='deletedata' ),
    path('update/<int:id>/',views.update_data,name='updatedata' ),
]
