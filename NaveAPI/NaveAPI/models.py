from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Administrator(models.Model):

    user = models.CharField(
        max_length = 255,
        null = False,
        blank = False,
        unique = True
    )

    password = models.CharField(
        max_length = 255,
        null = False,
        blank = False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique = True
    )

    objects = models.Manager()

class UserAdministrator(models.Model):

    user = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique = True
    )

    password = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique = True
    )

    createDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=False,
        blank=False
    )

    deleteDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )

    isDeleted = models.BooleanField(
        null = False,
        blank = False
    )

    objects = models.Manager()

class JobVacancy(models.Model):

    userADMID = models.ForeignKey(
        UserAdministrator,
        on_delete=models.CASCADE,
        null = False,
        blank = False
    )

    company = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    description = models.CharField(
        max_length=4000,
        null=False,
        blank=False
    )

    salary = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    createDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=False,
        blank=False
    )

    deleteDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )

    isDeleted = models.BooleanField(
        null=False,
        blank=False
    )

    objects = models.Manager()

def user_file_directory_path(instance, filename):
    return 'website/files/user_{0}/{1}'.format(instance.user.id, filename)

class User(models.Model):

    user = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique = True
    )

    password = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique = True
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    telephone = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    curriculum = models.FileField(
        upload_to=user_file_directory_path,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        null = True,
        blank = True
    )

    createDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=False,
        blank=False
    )

    deleteDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )

    isDeleted = models.BooleanField(
        null=False,
        blank=False
    )

    objects = models.Manager()

class JobApplication(models.Model):

    jobVacancyID = models.ForeignKey(
        JobVacancy,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    userID = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    createDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=False,
        blank=False
    )

    deleteDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )

    isDeleted = models.BooleanField(
        null=False,
        blank=False
    )

    objects = models.Manager()

class Comment(models.Model):

    userADMID = models.ForeignKey(
        UserAdministrator,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    userID = models.ForeignKey(
        JobApplication,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    createDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=False,
        blank=False
    )

    deleteDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )

    isDeleted = models.BooleanField(
        null=False,
        blank=False
    )

    objects = models.Manager()

class Log(models.Model):

    commentID = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    log = models.CharField(
        max_length=6000,
        null=False,
        blank=False
    )

    createDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=False,
        blank=False
    )

    deleteDate = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )

    isDeleted = models.BooleanField(
        null=False,
        blank=False
    )

    objects = models.Manager()





