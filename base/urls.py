from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('new_complaint/', new_complaint, name='new_complaint'),
    path('complaints/', get_all_complaints, name='get_complaints'),
    path('complaints_admin/', get_all_complaints_category_admin, name='admin_complaints'),
    path('new_event/', create_event, name='create_event'),
    path('events/', get_all_event, name='get_all_events'),
    path('update/', update_user, name='update_user'),
    path('user/', get_user, name='get_user'),
    path('complaint/<int:complaint_id>/resolve/', resolve_complaint, name='resolve_complaint'),
]
