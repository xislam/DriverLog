from django.db import models


class DriverLog(models.Model):
    STATUS_CHOICES = [
        ('OFF', 'OFF'),
        ('работает', 'работает'),
    ]

    company_id = models.IntegerField()
    create_date = models.DateTimeField()
    driver_id = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __int__(self):
        return self.driver_id
