from django.db import models

# 個人訊息
class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    introduction = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    def __str__(self):
        return self.name


# 工作經驗
class JobExperience(models.Model):
    company_name = models.CharField(max_length=80)      # 公司名
    title = models.CharField(max_length=20)             # 職稱
    employment_period = models.CharField(max_length=50) # 公司待多久
    description = models.TextField()                    # 工作描述
    reason_for_leaving = models.TextField()             # 離職原因
    salary_range = models.CharField(max_length=50)      # 薪資範圍
    def __str__(self):
        return self.company_name

# 教育程度
class Education(models.Model):
    school_name = models.CharField(max_length=100)
    school_departments = models.CharField(max_length=100)
    graduate_status = models.CharField(max_length=50)
    education_level = models.CharField(max_length=50)
    duration = models.CharField(max_length=100)
    def __str__(self):
        return self.school_name

# 技能數
class Skill(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subskills')
    def __str__(self):
        return self.name

