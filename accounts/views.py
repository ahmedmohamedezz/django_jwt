from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken


class MyTokenObtainPairView(TokenObtainPairView):
    """
    POST (username && password) -> { access, refresh }
    """


class MyTokenRefreshView(TokenRefreshView):
    """
    POST { "refresh": "<refresh_token>" } -> { access, refresh }
    """


class LogoutView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response(
                {"detail": "Refresh token required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as _:
            return Response(
                {"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST
            )

        return Response({"detail": "Logged out"}, status=status.HTTP_200_OK)


class ProtectedView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response({"hello": f"hi {request.user.username}, you're authenticated"})
