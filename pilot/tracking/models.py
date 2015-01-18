from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class SongTrackingMilestone(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False, unique=True)
	mark = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=2, 
		validators= [MinValueValidator(0), MaxValueValidator(1)], 
		help_text = "Enter a value between 0 and 1. For example, 0.50 for a mark at 50%. ")

class SongTrackingRecord(models.Model):
	created = models.DateTimeField(auto_now_add=True, null=False)
	updated = models.DateTimeField(auto_now_add=True, auto_now=True, null=False)
	milestone = models.ForeignKey(SongTrackingMilestone, help_text="The most recent or final milestone that was hit by the user.")