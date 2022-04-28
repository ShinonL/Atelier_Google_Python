from django.db import models

# Create your models here.
company_types = (
    ('SRL', 'S.R.L'),
    ('SA', 'S.A')
)


class Companies(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    company_type = models.CharField(max_length=10, choices=company_types)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.name} - {self.company_type}"
