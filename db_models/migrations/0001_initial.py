# Generated by Django 3.2.5 on 2022-08-23 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'districts',
            },
        ),
        migrations.CreateModel(
            name='JobNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=45)),
                ('reward', models.IntegerField()),
                ('description', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_models.company')),
            ],
            options={
                'db_table': 'job_notices',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'positions',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'skills',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='RecruitmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job_notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_models.jobnotice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_models.user')),
            ],
            options={
                'db_table': 'recruitment_status',
            },
        ),
        migrations.CreateModel(
            name='NoticeSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_models.jobnotice')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_models.skill')),
            ],
            options={
                'db_table': 'notice_skills',
            },
        ),
        migrations.CreateModel(
            name='NoticePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_models.jobnotice')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_models.position')),
            ],
            options={
                'db_table': 'notice_positions',
            },
        ),
        migrations.CreateModel(
            name='NoticeDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_models.district')),
                ('job_notice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_models.jobnotice')),
            ],
            options={
                'db_table': 'notice_districts',
            },
        ),
    ]
