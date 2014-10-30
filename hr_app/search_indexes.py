# import datetime
# from haystack import indexes
# from hr_app.models import Honoree

# class HonoreeIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     last_name = indexes.CharField(model_attr='last_name')
#     first_name = indexes.CharField(model_attr='first_name')
#     parent = indexes.CharField(model_attr='parent')

#     def get_model(self):
#         return Honoree

#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.all()