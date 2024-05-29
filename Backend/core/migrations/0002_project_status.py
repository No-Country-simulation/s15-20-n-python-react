# Generated by Django 5.0.6 on 2024-05-29 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('Planning', 'Planning'), ('In progress', 'In progress'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Planning', max_length=20),
        ),
    ]
