# Generated by Django 4.2.13 on 2024-07-27 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('salary_min', models.IntegerField(blank=True, null=True)),
                ('salary_max', models.IntegerField(blank=True, null=True)),
                ('employment_type', models.CharField(choices=[('full_time', 'Повна зайнятість'), ('part_time', 'Не повна зайнятість'), ('contract', 'Підробіток'), ('internship', 'Стажування')], default='full_time', max_length=20)),
                ('relocation_ready', models.CharField(choices=[('relocate_yes', 'Можу виїхати за потреби'), ('relocate_no', 'НЕ готовий до переїзду')], default='relocate_no', max_length=20)),
                ('desired_positions', models.ManyToManyField(blank=True, related_name='resumes', to='company.jobposition')),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Strength',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_current', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('recommendation', models.FileField(blank=True, null=True, upload_to='recommendations/')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='resume.resume')),
            ],
            options={
                'verbose_name': 'Work Experience',
                'verbose_name_plural': 'Work Experiences',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='UserLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency_level', models.CharField(choices=[('beginner', 'Початківець'), ('basic', 'Базовий рівень'), ('intermediate', 'Впевнений користувач'), ('advanced', 'Вільно володію'), ('native', 'Рідна')], max_length=20)),
                ('certificate_link', models.URLField(blank=True, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_languages', to='resume.language')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_languages', to='resume.resume')),
            ],
            options={
                'verbose_name': 'User Language',
                'verbose_name_plural': 'User Languages',
            },
        ),
        migrations.AddField(
            model_name='resume',
            name='strengths',
            field=models.ManyToManyField(blank=True, related_name='resumes', to='resume.strength'),
        ),
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_level', models.CharField(choices=[('high_school', 'Середня'), ('vocational_school', 'Середня спеціальна'), ('incomplete_higher', 'Незакінчена вища'), ('higher_education', 'Вища')], max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_student', models.BooleanField(default=False)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='resume.resume')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('certificate_link', models.URLField(blank=True, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='resume.resume')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ['start_date'],
            },
        ),
    ]
