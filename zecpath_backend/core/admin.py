from django.contrib import admin
from .models import User, Employer, Candidate, Job, Application


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "name",
        "role",
        "is_active",
        "is_verified",
        "created_at",
    )
    list_filter = (
        "role",
        "is_active",
        "is_verified",
    )
    search_fields = (
        "email",
        "name",
        "phone",
    )


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "user",
        "industry",
        "location",
        "created_at",
    )
    search_fields = (
        "company_name",
        "user__email",
    )


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone",
        "location",
        "created_at",
    )
    search_fields = (
        "user__email",
        "user__name",
        "phone",
    )


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "employer",
        "location",
        "job_type",
        "is_active",
        "posted_at",
    )
    list_filter = (
        "is_active",
        "job_type",
    )
    search_fields = (
        "title",
        "company",
        "location",
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "candidate",
        "job",
        "status",
        "applied_at",
        "updated_at",
    )
    list_filter = (
        "status",
    )
    search_fields = (
        "candidate__user__email",
        "job__title",
    )