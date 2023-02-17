# Generated by Django 4.1.2 on 2023-02-12 14:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher'), ('Parents', 'Parents'), ('School Administrator', 'School Administrator'), ('Super User', 'Super User')], default='Student', max_length=30)),
                ('website', models.URLField(blank=True, max_length=300, null=True)),
                ('facebook', models.URLField(blank=True, max_length=300, null=True)),
                ('twitter', models.URLField(blank=True, max_length=300, null=True)),
                ('linkedin', models.URLField(blank=True, max_length=300, null=True)),
                ('Instagram', models.URLField(blank=True, max_length=300, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClassGrade',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('class_grade', models.IntegerField()),
                ('section', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('unique_name', models.CharField(max_length=255, unique=True)),
                ('subject', models.CharField(choices=[('English', 'ENG'), ('Mathematics', 'MAT'), ('Physics', 'PHY'), ('Chemistry', 'CHE'), ('Biology', 'BIO'), ('SAT', 'SAT'), ('Civics', 'CIV')], default='ENG', max_length=20)),
                ('choose_answer', models.CharField(max_length=3000)),
                ('truefalse_answer', models.CharField(max_length=500)),
                ('fillblank_answer', models.CharField(max_length=1028)),
                ('no_of_questions', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'ordering': ['-start_time'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_city', models.CharField(blank=True, max_length=255, null=True)),
            ],
            bases=('base.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('subject', models.CharField(choices=[('English', 'ENG'), ('Mathematics', 'MAT'), ('Physics', 'PHY'), ('Chemistry', 'CHE'), ('Biology', 'BIO'), ('SAT', 'SAT'), ('Civics', 'CIV')], default='ENG', max_length=100)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('class_grade', models.ManyToManyField(blank=True, to='base.classgrade')),
                ('school_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.school')),
            ],
            bases=('base.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('class_grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.classgrade')),
                ('school_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.school')),
            ],
            bases=('base.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('score', models.IntegerField()),
                ('display', models.BooleanField(default=False)),
                ('finished', models.DateField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.exam')),
                ('student_score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_score', to='base.student')),
            ],
            options={
                'ordering': ['finished'],
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='school_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.school'),
        ),
        migrations.AddField(
            model_name='exam',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='base.teacher'),
        ),
        migrations.AddField(
            model_name='classgrade',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.school'),
        ),
    ]
