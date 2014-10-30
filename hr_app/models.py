from django.db import models
from django.core.urlresolvers import reverse
from datetime import date
from mptt.models import MPTTModel, TreeForeignKey
import watson

class Organization(MPTTModel):
	organization_name = models.CharField(max_length=200)
	parent = TreeForeignKey('self', related_name='children', blank=True, null=True)

	def __str__(self):
		return self.organization_name

	def __unicode__(self):
		return u'%s' % self.organization_name

	def get_absolute_url(self):
		return reverse('organization-detail', kwargs={'org_id': self.pk})

	class MPTTMeta:
		order_insertion_by = ['organization_name']

class Honoree(MPTTModel):
	first_name = models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100,blank=True, null=True)
	last_name = models.CharField(max_length=100)
	email = models.EmailField()
	parent = TreeForeignKey(Organization, related_name='lawyers')

	def __str__(self):
		return self.last_name + ', ' + self.first_name

	def __unicode__(self):
		return u'%s, %s' % (self.last_name, self.first_name)

	def get_absolute_url(self):
		return reverse('honoree-detail', kwargs={'pk': self.pk})

	class MPTTMeta:
		order_insertion_by = ['last_name']

AWARD_CHOICES = (
	('Honor', 'More than 50 Hours'),
    ('High', 'More than 100 Hours'),
)

RULE49_CHOICES = (
	('Active','Licensed to Practice Law in the District'),
	('Other State', 'Licensed to Practice Law in another Jurisdiction')
)

curr_year = date.today().year

class Honor(MPTTModel):
	year = models.CharField(max_length=5, default=curr_year)
	award_level = models.CharField(max_length=50, choices=AWARD_CHOICES)
	bar_status = models.CharField(max_length=200, choices=RULE49_CHOICES)
	parent = TreeForeignKey(Honoree, related_name='honors')

	class MPTTMeta:
		order_insertion_by = ['year']

	def __unicode__(self):
		return u'%s : %s' % (str(self.parent), self.year)

	def __str__(self):
		return str(self.parent) + ":" + self.year

watson.register(Honoree)
