from ..models import Job


def get_all_jobs():
    return Job.objects.all()


def create_job(data):
    from ..serializers import JobSerializer

    serializer = JobSerializer(data=data)

    if serializer.is_valid():
        return serializer.save(), None

    return None, serializer.errors