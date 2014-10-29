import csv
from models import Organization, Honoree, Honor

def processCSVfile(f):
	hr_reader = csv.reader(f, delimiter=',', quotechar='"')
	hr_reader.next()
	for data in hr_reader:

		#Year, Organization, First Name, Middle Name, Last Name, Email, Award Level, Bar Status	
		org, created = Organization.objects.get_or_create(organization_name=data[1]);
		honoree, honoree_create = Honoree.objects.get_or_create(
			first_name=data[2],
			middle_name=data[3],
			last_name=data[4],
			email=data[5],
			parent=org
		)
		honor, honor_created = Honor.objects.get_or_create(
			year=data[0], 
			award_level=data[6],
			bar_status=data[7],
			parent=honoree
		)
	return True