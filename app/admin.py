from django.contrib import admin
from .models import PersonalInfo, JobExperience, Education, Skill

admin.site.register(PersonalInfo)
admin.site.register(JobExperience)
admin.site.register(Education)
admin.site.register(Skill)
