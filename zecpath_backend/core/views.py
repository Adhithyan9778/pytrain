from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsEmployer, IsCandidate

from .models import Candidate, Employer
from .serializers import (
    JobSerializer,
    SignupSerializer,
    CandidateSerializer,
    EmployerSerializer,
)
from .services.job_service import get_all_jobs, create_job




class JobListAPIView(APIView):

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsEmployer()]

        return [IsAuthenticated()]

    def get(self, request):
        jobs = get_all_jobs()
        serializer = JobSerializer(jobs, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        job, errors = create_job(
            request.data,
            request.user
        )

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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {
                "message": "User API is working",
                "status": "success"
            },
            status=status.HTTP_200_OK
        )
class SignupAPIView(APIView):

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "message": "User created successfully",
                    "user": {
                        "id": user.id,
                        "name": user.name,
                        "email": user.email,
                        "role": user.role
                    }
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )  
class LogoutAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {"error": "Refresh token is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Logout successful"},
                status=status.HTTP_200_OK
            )

        except Exception:
            return Response(
                {"error": "Invalid or expired refresh token"},
                status=status.HTTP_400_BAD_REQUEST
            ) 
class CandidateProfileAPIView(APIView):

    permission_classes = [IsCandidate]

    def get(self, request):
        try:
            profile = Candidate.objects.get(
                user=request.user,
                is_deleted=False
            )
        except Candidate.DoesNotExist:
            return Response(
                {"error": "Candidate profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CandidateSerializer(profile)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        if hasattr(request.user, "candidate"):
            return Response(
                {"error": "Candidate profile already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CandidateSerializer(data=request.data)

        if serializer.is_valid():
            profile = serializer.save(user=request.user)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request):
        try:
            profile = Candidate.objects.get(
                user=request.user,
                is_deleted=False
            )
        except Candidate.DoesNotExist:
            return Response(
                {"error": "Candidate profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CandidateSerializer(
            profile,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request):
        try:
            profile = Candidate.objects.get(
                user=request.user,
                is_deleted=False
            )
        except Candidate.DoesNotExist:
            return Response(
                {"error": "Candidate profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        profile.is_deleted = True
        profile.save()

        return Response(
            {"message": "Candidate profile deleted successfully"},
            status=status.HTTP_200_OK
        )

class EmployerProfileAPIView(APIView):

    permission_classes = [IsEmployer]

    def get(self, request):
        try:
            profile = Employer.objects.get(
                user=request.user,
                is_deleted=False
            )
        except Employer.DoesNotExist:
            return Response(
                {"error": "Employer profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EmployerSerializer(profile)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        if hasattr(request.user, "employer"):
            return Response(
                {"error": "Employer profile already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EmployerSerializer(data=request.data)

        if serializer.is_valid():
            profile = serializer.save(user=request.user)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request):
        try:
            profile = Employer.objects.get(
                user=request.user,
                is_deleted=False
            )
        except Employer.DoesNotExist:
            return Response(
                {"error": "Employer profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = EmployerSerializer(
            profile,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request):
        try:
            profile = Employer.objects.get(
                user=request.user,
                is_deleted=False
            )
        except Employer.DoesNotExist:
            return Response(
                {"error": "Employer profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        profile.is_deleted = True
        profile.save()

        return Response(
            {"message": "Employer profile deleted successfully"},
            status=status.HTTP_200_OK
        )