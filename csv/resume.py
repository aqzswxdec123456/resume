import sys
import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_resume.settings')
django.setup()

from resume.models import PersonalInfo, JobExperience, Education, Skill

def import_personal_info(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            personal_info = PersonalInfo(**row)
            personal_info.save()

def import_work_experience(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = JobExperience(**row)
            job.save()

def import_education(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            education = Education(**row)
            education.save()

def import_skills(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            parent_name = row['parent_name'].strip()
            if parent_name:
                parent = Skill.objects.get(name=parent_name)
            else:
                parent = None

            skill, created = Skill.objects.get_or_create(
                name=row['name'].strip(),
                defaults={'parent': parent}
            )


def main(mode, csv_file_path):
    if mode == '1':  # 模式1: 私人訊息
        import_personal_info(csv_file_path)
    elif mode == '2':  # 模式2: 工作經驗
        import_work_experience(csv_file_path)
    elif mode == '3':  # 模式3: 教育程度
        import_education(csv_file_path)
    elif mode == '4':  # 模式4: 技能數
        import_skills(csv_file_path)
    else:
        print("Unsupported mode")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 script.py [mode] [csv_file_path]")
    else:
        mode = sys.argv[1]
        csv_file_path = sys.argv[2]
        main(mode, csv_file_path)


