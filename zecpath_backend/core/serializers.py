from rest_framework import serializers

from .models import User, Employer, Candidate, Job, Application


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = [
            'id',
            'user',
            'company_name',
            'company_description',
            'website',
            'industry',
            'location',
            'created_at'
        ]


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            'id',
            'user',
            'phone',
            'bio',
            'skills',
            'resume',
            'location',
            'created_at'
        ]


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id',
            'employer',
            'title',
            'company',
            'description',
            'location',
            'job_type',
            'salary_range',
            'is_active',
            'posted_at',
            'updated_at'
        ]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id',
            'candidate',
            'job',
            'cover_letter',
            'resume',
            'status',
            'applied_at',
            'updated_at'
        ]

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        return user