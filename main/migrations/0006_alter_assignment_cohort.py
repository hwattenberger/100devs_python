# Generated by Django 4.0.3 on 2022-03-14 22:38

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_assignment_cohort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='cohort',
            field=models.ForeignKey(default=main.models.get_current_cohort, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.cohort'),
        ),
    ]