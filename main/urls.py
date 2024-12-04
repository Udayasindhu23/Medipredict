# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('', views.splash, name='splash'),
# #     path('home/', views.home, name='home'),
# #     path('signup/', views.signup, name='signup'),
# #     path('forgot_password/', views.forgot_password, name='forgot_password'),
# #     path('select_role/', views.select_role, name='select_role'),
# # ]
# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #     path('', views.splash, name='splash'),                       # Splash screen
# #     path('home/', views.home, name='home'),                       # Home page
# #     path('signup/', views.signup, name='signup'),                 # Signup page
# #     path('forgot-password/', views.forgot_password, name='forgot_password'),  # Forgot password page
# #     path('role-selection/', views.role_selection, name='role_selection'),      # Role selection page
# #      path('patient/', views.patient, name='patient'),  # Patient role
# #     path('doctor/', views.doctor, name='doctor'),    # Doctor role
# #     path('pharmacy/', views.pharmacy, name='pharmacy'), # Pharmacy role
# # ]

# # main/urls.py

# from django.urls import path
# from . import views
# from .views import user_details
# from django.urls import path
# from .views import register, user_details

# urlpatterns = [
#     path('', views.splash, name='splash'),  # Splash screen (landing page)
#     path('home/', views.home, name='home'),  # Home page after splash
#     path('signup/', views.signup, name='signup'),  # User signup page
#     path('forgot-password/', views.forgot_password, name='forgot_password'),  # Forgot password page
#     path('role-selection/', views.role_selection, name='role_selection'),  # Role selection page
#     path('patient/', views.patient, name='patient'),  # Patient dashboard/page
#     path('doctor/', views.doctor, name='doctor'),  # Doctor dashboard/page
#     path('pharmacy/', views.pharmacy, name='pharmacy'),  # Pharmacy dashboard/page
#     path('register/', register, name='register'),
#     path('user-details/', user_details, name='user_details'),
#     # Uncomment below to add login/logout views if necessary
#     path('login/', views.login_view, name='login'),  # User login page
#     path('logout/', views.logout_view, name='logout'),  # User logout page
# ]

from django.urls import path
from . import views  # Import all views
from .views import register, user_details  # Import specific views

urlpatterns = [
    path('', views.splash, name='splash'),  # Splash screen (landing page)
    path('home/', views.home, name='home'),  # Home page after splash
    path('signup/', views.signup, name='signup'),  # User signup page
    path('forgot-password/', views.forgot_password, name='forgot_password'),  # Forgot password page
    path('role-selection/', views.role_selection, name='role_selection'),  # Role selection page
    path('patient/', views.patient, name='patient'),  # Patient dashboard/page
    path('doctor/', views.doctor, name='doctor'),  # Doctor dashboard/page
    path('pharmacy/', views.pharmacy, name='pharmacy'),  # Pharmacy dashboard/page
    path('register/', register, name='register'),  # User registration page
    path('user-details/', user_details, name='user_details'),  # User details page
    path('login/', views.login_view, name='login'),  # User login page
    path('logout/', views.logout_view, name='logout'),  # User logout page
]
