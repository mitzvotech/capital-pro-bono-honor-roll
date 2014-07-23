from django.db import models
from datetime import date

# Model List
# Organization
# Honoree

class Organization(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Honoree(models.Model):
	affiliation = models.ForeignKey(Organization)
	first_name = models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100)
	email = models.EmailField()

	def __str__(self):
		return self.last_name + ', ' + self.first_name

	def get_absolute_url(self):
		return reverse('author-detail', kwargs={'pk': self.pk})

AWARD_CHOICES = (
	('Honor', 'More than 50 Hours'),
    ('High', 'More than 100 Hours'),
)

RULE49_CHOICES = (
	('Active','Licensed to Practice Law in the District'),
	('Other State', 'Licensed to Practice Law in another Jurisdiction')
)

curr_year = date.today().year

class Honor(models.Model):
	year = models.CharField(max_length=5, default=curr_year)
	award_level = models.CharField(max_length=50, choices=AWARD_CHOICES)
	bar_status = models.CharField(max_length=200, choices=RULE49_CHOICES)
	honoree = models.ForeignKey(Honoree)

	def __str__(self):
		return self.id