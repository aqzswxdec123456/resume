from django.shortcuts import render
from .models import PersonalInfo, JobExperience, Education, Skill

def resume_view(request):
    personal_info = PersonalInfo.objects.first()
    skills = Skill.objects.filter(parent__isnull=True)
    job_experiences = JobExperience.objects.all()
    education = Education.objects.all()

    return render(request, 'dev_resume/resume.html', {
        'personal_info': personal_info,
        'skills': skills,
        'education': education,
        'job_experiences': job_experiences
    })

