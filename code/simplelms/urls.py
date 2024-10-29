"""
URL configuration for simplelms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert-user/', views.insert_user, name='insert_user'),
    path('insert-course/', views.insert_course, name='insert_course'),
    path('select-all-users/', views.select_all_users, name='select_all_users'),
    path('select-user/<int:user_id>/', views.select_user_by_id, name='select_user_by_id'),
    path('select-user-email/<str:email>/', views.select_user_by_email, name='select_user_by_email'),
    path('update-user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete-all-courses/', views.delete_all_courses, name='delete_all_courses'),
    path('delete-all-users-except/', views.delete_all_users_except, name='delete_all_users_except'),
    path('testing/', views.testing, name='testing'),
    path('all-course/', views.allCourse, name='allCourse'),
    path('user-courses/', views.userCourses, name='userCourses'),
    path('course-stat/', views.courseStat, name='courseStat'),
    path('course-member-stat/', views.courseMemberStat, name='courseMemberStat'),
    path('silk/', include('silk.urls', namespace='silk'))
]
