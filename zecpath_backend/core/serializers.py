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
            'domain',
            'industry',
            'company_size',
            'location',
            'is_verified',
            'is_deleted',
            'created_at'
        ]
        read_only_fields = [
            'id',
            'user',
            'is_verified',
            'is_deleted',
            'created_at'
        ]

    def validate_company_size(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError(
                "Company size must be greater than 0."
            )

        return value

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
            'id',
            'user',
            'phone',
            'bio',
            'skills',
            'education',
            'experience',
            'expected_salary',
            'resume',
            'location',
            'is_deleted',
            'created_at'
        ]
        read_only_fields = [
            'id',
            'user',
            'is_deleted',
            'created_at'
        ]

    def validate_expected_salary(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError(
                "Expected salary cannot be negative."
            )

        return value
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
        read_only_fields = [
            'id',
            'employer',
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
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password',
            'phone'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create_user(
            password=password,
            role=User.Role.CANDIDATE,
            **validated_data
        )

        return user