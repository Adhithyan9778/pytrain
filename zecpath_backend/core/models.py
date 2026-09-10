from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        EMPLOYER = "EMPLOYER", "Employer"
        CANDIDATE = "CANDIDATE", "Candidate"

    username = None

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CANDIDATE
    )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Employer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employer"
    )
    company_name = models.CharField(max_length=100)
    company_description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


class Candidate(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="candidate"
    )
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    resume = models.FileField(upload_to="resumes/", blank=True)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name


class Job(models.Model):
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name="jobs"
    )
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    job_type = models.CharField(max_length=50, blank=True)
    salary_range = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(upload_to="application_resumes/", blank=True)
    status = models.CharField(max_length=50, default="Applied")
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["candidate", "job"],
                name="unique_candidate_job_application"
            )
        ]

    def __str__(self):
        return f"{self.candidate} - {self.job}"