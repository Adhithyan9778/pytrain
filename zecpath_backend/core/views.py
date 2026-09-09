from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import JobSerializer
from .services.job_service import get_all_jobs, create_job


class JobListAPIView(APIView):

    def get(self, request):
        jobs = get_all_jobs()
        serializer = JobSerializer(jobs, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        job, errors = create_job(request.data)

        if errors:
            return Response(
                errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = JobSerializer(job)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class UserTestAPIView(APIView):

    def get(self, request):
        return Response(
            {
                "message": "User API is working",
                "status": "success"
            },
            status=status.HTTP_200_OK
        )