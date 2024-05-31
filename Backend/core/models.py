from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

# Model for role types


class RoleType(models.Model):
    EDITOR = 'editor'
    COMMENTATOR = 'commentator'
    READER = 'reader'

    ROLE_CHOICES = [
        (EDITOR, 'Editor'),
        (COMMENTATOR, 'Comentarista'),
        (READER, 'Lector'),
    ]

    role_type = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=READER,
    )

# Model for labels of tasks


class LabelTask(models.Model):
    label_text = models.CharField(max_length=100)


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)


class Collaborator(models.Model):
    collab_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(RoleType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)
    propietary = models.ForeignKey(User, on_delete=models.CASCADE)
    collabs = models.ManyToManyField(Collaborator)


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    membership_project = models.ForeignKey(Project, on_delete=models.CASCADE)


class TasksList(models.Model):
    list_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    membership_board = models.ForeignKey(Board, on_delete=models.CASCADE)


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    create_at = models.DateField(default=date.today)
    expiration_at = models.DateField(blank=True, null=True)
    labels = models.ManyToManyField(LabelTask)
    assigned_users = models.ManyToManyField(User)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField(max_length=500)
    commented_task = models.ForeignKey(Task, on_delete=models.CASCADE)


class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=300)
    associate_task = models.ForeignKey(Task, on_delete=models.CASCADE)
