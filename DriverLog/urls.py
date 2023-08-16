from django.urls import path
from .views import WorkingTimeView

urlpatterns = [
    path('driver_log_working_time/<int:driver_id>/<start_date>/<end_date>/', WorkingTimeView.as_view(),
         name='driver_log_working_time'),
]
