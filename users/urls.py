from django.urls import path

from users.views import SignUpView, UserUpdateView

urlpatterns=[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
]