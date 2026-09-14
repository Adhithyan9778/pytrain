
from ..models import Job, Employer


def get_all_jobs():
    return Job.objects.all()


def create_job(data, user):
    from ..serializers import JobSerializer

    try:
        employer = Employer.objects.get(user=user)
    except Employer.DoesNotExist:
        return None, {
            "error": "Employer profile not found."
        }

    serializer = JobSerializer(data=data)

    if serializer.is_valid():
        return serializer.save(employer=employer), None

    return None, serializer.errors