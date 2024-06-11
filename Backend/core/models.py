from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

# Model for role types


class RoleType(models.Model):
    ROLE_CHOICES = {
        'EDITOR': 'Editor', 'COMMENTATOR': 'Comentarista', 'READER': 'Lector'
    }

    role_type = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='READER',
    )
    status = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.role_type

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['role_type']

# Model for labels of tasks


class LabelTask(models.Model):
    label_text = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.label_text

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['label_text']


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)
    status = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['name']


class Collaborator(models.Model):
    collab_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(RoleType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        ordering = ['user']


class Project(models.Model):
    PLANNING = 'Planning'
    IN_PROGRESS = 'In_progress'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (PLANNING, 'Planning'),
        (IN_PROGRESS, 'In_progress'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled')
    ]

    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)
    propietary = models.ForeignKey(User, on_delete=models.CASCADE)
    collabs = models.ManyToManyField(Collaborator)
    status = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['name', 'propietary']


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    membership_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tablero'
        verbose_name_plural = 'Tableros'
        ordering = ['title']


class TasksList(models.Model):
    list_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    membership_board = models.ForeignKey(Board, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lista de Tareas'
        verbose_name_plural = 'Listas de Tareas'
        ordering = ['title']


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    create_at = models.DateField(default=date.today)
    expiration_at = models.DateField(blank=True, null=True)
    labels = models.ManyToManyField(LabelTask)
    assigned_users = models.ManyToManyField(User)
    status = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['title']


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField(max_length=500, blank=True, null=True)
    file_link = models.CharField(max_length=300, blank=True, null=True)
    commented_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['user']


class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    associate_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'
        ordering = ['title']
