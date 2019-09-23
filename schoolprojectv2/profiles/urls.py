from .views import ( StudentList,
                     TeacherList
                    )
from django.urls import path, include

urlpatterns = [
    path('students/', StudentList.as_view, name="students"),
    path('teachers/', TeacherList.as_view, name="teachers")
]
