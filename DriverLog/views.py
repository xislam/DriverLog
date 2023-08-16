from rest_framework import generics, status
from rest_framework.response import Response
from datetime import timedelta
from .models import DriverLog
from .serializers import DriverLogSerializer

class WorkingTimeView(generics.RetrieveAPIView):
    serializer_class = DriverLogSerializer

    def get_queryset(self):
        driver_id = self.kwargs['driver_id']
        start_date = self.kwargs['start_date']
        end_date = self.kwargs['end_date']
        return DriverLog.objects.filter(driver_id=driver_id, create_date__range=(start_date, end_date))

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        total_working_time = timedelta()
        total_rest_time = timedelta()
        total_off_time = timedelta()

        last_log = None

        for log in queryset:
            if last_log:
                time_difference = log.create_date - last_log.create_date
                if last_log.status == 'работает':
                    total_working_time += time_difference
                elif last_log.status == 'OFF':
                    total_off_time += time_difference
                elif last_log.status == 'отдыхал':
                    total_rest_time += time_difference

            last_log = log

        result = {
            'working_time': str(total_working_time),
            'rest_time': str(total_rest_time),
            'off_time': str(total_off_time)
        }

        return Response(result, status=status.HTTP_200_OK)
