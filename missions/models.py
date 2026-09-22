from django.db import models
from django.core.exceptions import ValidationError

HOSTEL_CHOICES = [
    ("Ashok Bhawan", "Ashok Bhawan"),
    ("Bhagirath Bhawan", "Bhagirath Bhawan"),
    ("Budh Bhawan", "Budh Bhawan"),
    ("C.V. Raman Bhawan", "C.V. Raman Bhawan"),
    ("Gandhi Bhawan", "Gandhi Bhawan"),
    ("Krishna Bhawan", "Krishna Bhawan"),
    ("Malaviya Bhawan-A", "Malaviya Bhawan-A"),
    ("Malaviya Bhawan-B", "Malaviya Bhawan-B"),
    ("Malaviya Bhawan-C", "Malaviya Bhawan-C"),
    ("Malaviya Apartments", "Malaviya Apartments"),
    ("Rana Pratap Bhawan", "Rana Pratap Bhawan"),
    ("Ram Bhawan", "Ram Bhawan"),
    ("Shankar Bhawan", "Shankar Bhawan"),
    ("Srinivasa Ramanujan (SR) Bhawan", "Srinivasa Ramanujan (SR) Bhawan"),
    ("Vishwakarma Bhawan", "Vishwakarma Bhawan"),
    ("Vyas Bhawan", "Vyas Bhawan"),
    ("Meera Bhawan", "Meera Bhawan"),
]

DIFFICULTY_CHOICES = [
    ("warmup", "Warmup"),
    ("core", "Core"),
    ("boss_level", "Boss Level"),
]

STATUS_CHOICES = [
    ("unclaimed", "Unclaimed"),
    ("in_progress", "In Progress"),
    ("cracked", "Cracked"),
    ("expired", "Expired"),
]

class Mission(models.Model):
    codename = models.CharField(max_length=150)
    brief = models.TextField()
    points = models.IntegerField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="unclaimed")
    hostel = models.CharField(max_length=50, choices=HOSTEL_CHOICES)
    solver_handle = models.CharField(max_length=100, null=True, blank=True)
    deadline = models.DateTimeField()

    def clean(self):
        if self.points <= 0:
            raise ValidationError({"points": "Points must be greater than zero."})
        if self.status == "cracked" and not self.solver_handle:
            raise ValidationError({"solver_handle": "Solver handle is required when status is 'cracked'."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codename} - {self.hostel}"