from django.contrib import admin
from .models import Profile
from .models import PowershotApplicationForLiveSeries
from .models import BonVoyageApplicationForLiveSeries
from .models import Application

# Register your models here.
admin.site.register(Profile)
admin.site.register(PowershotApplicationForLiveSeries)
admin.site.register(BonVoyageApplicationForLiveSeries)
admin.site.register(Application)
