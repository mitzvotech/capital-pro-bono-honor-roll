from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer
from hr_app.models import Honor, Honoree

class HonoreeResource(ModelResource):
	class Meta:
		queryset = Honoree.objects.all()
		resource_name = 'honoree'
		excludes = ['id', 'level', 'lft', 'rght', 'tree_id']
		filtering = {
			'email': ALL,
		}


class HonorResource(ModelResource):
	honoree = fields.ForeignKey(HonoreeResource, 'parent')

	class Meta:
		queryset = Honor.objects.all()
		resource_name = 'honor'
        authorization = Authorization()
        filtering = {
            'email': ALL_WITH_RELATIONS,

        }
        serializer = Serializer(formats=['json'])