from django.contrib import admin
from .models import Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'teacher']
    search_fields = ['name', 'description', 'price', 'teacher']
    list_filter = ['name', 'description', 'price', 'teacher']
    list_per_page = 10
    list_max_show_all = 100
    list_display_links = ['name', 'description', 'price', 'teacher']
    list_select_related = ['name', 'description', 'price', 'teacher']
    
    def get_queryset(self, request):
        return super().get_queryset(request).filter(teacher=request.user)
    
        