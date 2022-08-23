from django.db import models

from common.utils import TimeStampModel

class Company(TimeStampModel):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'companies'

class JobNotice(TimeStampModel):
    title       = models.CharField(max_length=45)
    reward      = models.IntegerField()
    description = models.TextField()
    company     = models.ForeignKey('Company', on_delete=models.CASCADE)

    class Meta:
        db_table = 'job_notices'

class User(TimeStampModel):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'

class RecruitmentStatus(models.Model):
    job_notice = models.ForeignKey('JobNotice', on_delete=models.CASCADE)
    user       = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'recruitment_status'

class District(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'districts'

class NoticeDistrict(models.Model):
    job_notice = models.ForeignKey('JobNotice', on_delete=models.CASCADE)
    district   = models.ForeignKey('District', on_delete=models.CASCADE)

    class Meta:
        db_table = 'notice_districts'

class Position(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'positions'

class NoticePosition(models.Model):
    job_notice = models.ForeignKey('JobNotice', on_delete=models.CASCADE)
    position   = models.ForeignKey('Position', on_delete=models.CASCADE)

    class Meta:
        db_table = 'notice_positions'

class Skill(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'skills'

class NoticeSkill(models.Model):
    job_notice = models.ForeignKey('JobNotice', on_delete=models.CASCADE)
    skill      = models.ForeignKey('Skill', on_delete=models.CASCADE)

    class Meta:
        db_table = 'notice_skills'