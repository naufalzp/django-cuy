from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # User-related paths
    path('insert-user/', views.insert_user, name='insert_user'),
    path('select-all-users/', views.select_all_users, name='select_all_users'),
    path('select-user/<int:user_id>/', views.select_user_by_id, name='select_user_by_id'),
    path('select-user-email/<str:email>/', views.select_user_by_email, name='select_user_by_email'),
    path('update-user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete-all-users-except/', views.delete_all_users_except, name='delete_all_users_except'),
    
    # User statistics paths
    path('user-statistics/', views.user_statistics, name='user_statistics'),
    path('user-statistics-html/', views.user_statistics_html, name='user_statistics_html'),
    path('user-detail-statistics/<int:user_id>/', views.user_detail_statistics, name='user_detail_statistics'),

    # Course-related paths
    path('insert-course/', views.insert_course, name='insert_course'),
    path('all-course/', views.all_course, name='all_course'),
    path('user-courses/', views.user_courses, name='user_courses'),
    path('delete-all-courses/', views.delete_all_courses, name='delete_all_courses'),
    path('course-stat/', views.course_stat, name='course_stat'),
    path('course-member-stat/', views.course_member_stat, name='course_member_stat'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

    # Testing and additional data paths
    path('testing/', views.testing, name='testing'),
    path('add-data/', views.add_data, name='add_data'),

    # Silk profiling
    path('silk/', include('silk.urls', namespace='silk')),
]
