# Generated by Django 4.0.3 on 2022-03-05 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='HearAboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='RaceEthnicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('discord_name', models.CharField(blank=True, max_length=100, null=True)),
                ('twitch_name', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('sd_job', models.BooleanField(default=False)),
                ('sd_start_salary', models.TextField(blank=True, null=True)),
                ('why_interested', models.TextField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('need_accomodations', models.BooleanField(default=False)),
                ('accomodations_desc', models.TextField(blank=True, null=True)),
                ('desc_from_student', models.TextField(blank=True, null=True)),
                ('cohort', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.cohort')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.gender')),
                ('hear_about', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.hearaboutus')),
                ('race_ethnicity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.raceethnicity')),
            ],
        ),
    ]
