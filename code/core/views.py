from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.db.models import Max, Min, Avg, Count
from .models import Course

# Insert User
def insert_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({"message": "User created", "user_id": user.id})
    return JsonResponse({"error": "Invalid request method"}, status=400)

# Insert Course
def insert_course(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        teacher_id = request.POST.get("teacher_id")
        teacher = get_object_or_404(User, pk=teacher_id)
        course = Course.objects.create(name=name, description=description, price=price, teacher=teacher)
        return JsonResponse({"message": "Course created", "course_id": course.id})
    return JsonResponse({"error": "Invalid request method"}, status=400)

# Select All Users
def select_all_users(request):
    users = User.objects.all()
    
    if request.method == "GET" and 'html' in request.GET:
        return render(request, 'users.html', {'users': users})

    user_data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return JsonResponse({"users": user_data})

# Select Get by ID
def select_user_by_id(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    if request.method == "GET" and 'html' in request.GET:
        return render(request, 'user.html', {'user': user})
    
    return JsonResponse({"id": user.id, "username": user.username, "email": user.email})

# Select with Condition
def select_user_by_email(request, email):
    users = User.objects.filter(email=email)
    user_data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return JsonResponse({"users": user_data})

# Update User
def update_user(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(User, pk=user_id)
        user.username = request.POST.get("username", user.username)
        user.email = request.POST.get("email", user.email)
        user.save()
        return JsonResponse({"message": "User updated"})
    return JsonResponse({"error": "Invalid request method"}, status=400)

# Delete User
def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return JsonResponse({"message": "User deleted"})

# Delete All Courses
def delete_all_courses(request):
    Course.objects.all().delete()
    return JsonResponse({"message": "All courses deleted"})

# Delete All Users Except Specific IDs
def delete_all_users_except(request):
    if request.method == "POST":
        user_ids = request.POST.getlist("user_ids")
        User.objects.exclude(id__in=user_ids).delete()
        return JsonResponse({"message": "All users except specified deleted"})
    return JsonResponse({"error": "Invalid request method"}, status=400)

def testing(request):
    user_test = User.objects.filter(username="usertesting")
    if not user_test.exists():
        user_test = User.objects.create_user(
                            username="usertesting", 
                            email="usertest@email.com", 
                            password="sanditesting")
    all_users = serializers.serialize('python', User.objects.all())

    admin = User.objects.get(pk=1)
    user_test.delete()

    after_delete = serializers.serialize('python', User.objects.all())

    response = {
            "admin_user": serializers.serialize('python', [admin])[0],
            "all_users" : all_users,
            "after_del" : after_delete,
        }
    return JsonResponse(response)

def allCourse(request):
    allCourse = Course.objects.all()
    result = []
    for course in allCourse:
        record = {'id': course.id, 'name': course.name, 
                  'description': course.description, 
                  'price': course.price,
                  'teacher': {
                      'id': course.teacher.id,
                      'username': course.teacher.username,
                      'email': course.teacher.email,
                      'fullname': f"{course.teacher.first_name} {course.teacher.last_name}"
                  }}
        result.append(record)
    return JsonResponse(result, safe=False)

def userCourses(request):
    user = User.objects.get(pk=3)
    courses = Course.objects.filter(teacher=user.id)
    course_data = []
    for course in courses:
        record = {'id': course.id, 'name': course.name, 
                  'description': course.description, 'price': course.price}
        course_data.append(record)
    result = {'id': user.id, 'username': user.username, 'email': user.email, 
              'fullname': f"{user.first_name} {user.last_name}", 
              'courses': course_data}
    return JsonResponse(result, safe=False)

def courseStat(request):
    courses = Course.objects.all()
    stats = courses.aggregate(max_price=Max('price'),
                                min_price=Min('price'),
                                avg_price=Avg('price'))
    result = {'course_count': len(courses), 'courses': stats}
    return JsonResponse(result, safe=False)

def courseMemberStat(request):
    courses = Course.objects.filter(description__contains='python') \
                            .annotate(member_num=Count('coursemember'))
    course_data = []
    for course in courses:
        record = {'id': course.id, 'name': course.name, 'price': course.price, 
                  'member_count': course.member_num}
        course_data.append(record)
    result = {'data_count': len(course_data), 'data':course_data}
    return JsonResponse(result)