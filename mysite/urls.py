from typing import ValuesView
from django.contrib import admin
from django.urls import path, include

from A_test_assignment_for_WelbeX.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('A_test_assignment_for_WelbeX.urls')),
]
