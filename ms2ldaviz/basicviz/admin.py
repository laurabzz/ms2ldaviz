from django.contrib import admin
from basicviz.models import Experiment,Document,Mass2Motif,Feature,FeatureMass2MotifInstance


admin.site.register(Experiment)
admin.site.register(Document)
admin.site.register(Mass2Motif)
admin.site.register(Feature)
admin.site.register(FeatureMass2MotifInstance)