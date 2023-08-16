from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from datetime import datetime, timedelta
from DriverLog.models import DriverLog


class WorkingTimeViewTest(TestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.driver_log_1 = DriverLog.objects.create(
            company_id=1,
            create_date=datetime(2023, 8, 1, 8, 0),
            driver_id=123,
            status='работает'
        )
        self.driver_log_2 = DriverLog.objects.create(
            company_id=1,
            create_date=datetime(2023, 8, 1, 12, 0),
            driver_id=123,
            status='OFF'
        )
        # Добавьте больше тестовых данных по необходимости

    def test_working_time_view(self):
        start_date = '2023-08-01'
        end_date = '2023-08-07'
        url = reverse('working-time', args=[self.driver_log_1.driver_id, start_date, end_date])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['working_time'], '4 days, 4:00:00')
        self.assertEqual(response.data['off_time'], '4 days, 0:00:00')
