# Generated by Django 5.0.6 on 2024-06-09 23:53

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_text', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Etiqueta',
                'verbose_name_plural': 'Etiquetas',
                'ordering': ['label_text'],
            },
        ),
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_type', models.CharField(choices=[('EDITOR', 'Editor'), ('COMMENTATOR', 'Comentarista'), ('READER', 'Lector')], default='READER', max_length=20)),
                ('status', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
                'ordering': ['role_type'],
            },
        ),
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('collab_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.roletype')),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('collabs', models.ManyToManyField(to='core.collaborator')),
                ('propietary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['name', 'propietary'],
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('membership_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.project')),
            ],
            options={
                'verbose_name': 'Tablero',
                'verbose_name_plural': 'Tableros',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('create_at', models.DateField(default=datetime.date.today)),
                ('expiration_at', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('assigned_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('labels', models.ManyToManyField(to='core.labeltask')),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('associate_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
            ],
            options={
                'verbose_name': 'Archivo',
                'verbose_name_plural': 'Archivos',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('text_comment', models.TextField(blank=True, max_length=500, null=True)),
                ('file_link', models.CharField(blank=True, max_length=300, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('commented_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='TasksList',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('status', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('membership_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.board')),
            ],
            options={
                'verbose_name': 'Lista de Tareas',
                'verbose_name_plural': 'Listas de Tareas',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='teams',
            field=models.ManyToManyField(to='core.team'),
        ),
    ]
