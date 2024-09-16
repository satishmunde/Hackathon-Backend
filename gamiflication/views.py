# In your views.py
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import UserPoints

@login_required
def add_points(request, amount):
    user_points = get_object_or_404(UserPoints, user=request.user)
    user_points.add_points(amount)
    return JsonResponse({'status': 'success', 'points': user_points.points})



# Example of awarding a badge when a user reaches 100 points
from .models import Badge, UserBadge

@login_required
def check_and_award_badge(request):
    user_points = get_object_or_404(UserPoints, user=request.user)
    
    if user_points.points >= 100:  # Example condition
        badge = Badge.objects.get(name='100 Points Club')
        if not UserBadge.objects.filter(user=request.user, badge=badge).exists():
            UserBadge.objects.create(user=request.user, badge=badge)
            return JsonResponse({'status': 'badge_awarded', 'badge': badge.name})
    
    return JsonResponse({'status': 'no_badge_awarded'})



# Example view to get the top users for a leaderboard
from django.db.models import F
from .models import UserPoints

@login_required
def leaderboard(request):
    top_users = UserPoints.objects.order_by('-points')[:10]  # Top 10 users based on points
    leaderboard_data = [{'user': user.user.username, 'points': user.points} for user in top_users]
    return JsonResponse({'leaderboard': leaderboard_data})



# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import UserPoints, Badge, UserBadge, UserLevel
from .serializers import UserPointsSerializer, UserBadgeSerializer, UserLevelSerializer

# View to get user profile with points, levels, and badges
class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Get or create points, levels, and badges data
        points, _ = UserPoints.objects.get_or_create(user=user)
        level, _ = UserLevel.objects.get_or_create(user=user)
        badges = UserBadge.objects.filter(user=user)

        # Serialize the data
        points_serializer = UserPointsSerializer(points)
        level_serializer = UserLevelSerializer(level)
        badges_serializer = UserBadgeSerializer(badges, many=True)

        return Response({
            'points': points_serializer.data,
            'level': level_serializer.data,
            'badges': badges_serializer.data
        })

# View to add points to a user
class AddPointsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        points_to_add = request.data.get('points', 0)

        # Get or create user points
        user_points, _ = UserPoints.objects.get_or_create(user=user)
        user_points.add_points(points_to_add)

        # Serialize updated points
        points_serializer = UserPointsSerializer(user_points)

        return Response(points_serializer.data, status=status.HTTP_200_OK)

# View to fetch a list of all available badges
class BadgeListAPIView(APIView):
    def get(self, request):
        badges = Badge.objects.all()
        serializer = BadgeSerializer(badges, many=True)
        return Response(serializer.data)

# View to award a badge to a user
class AwardBadgeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        badge_id = request.data.get('badge_id')

        try:
            badge = Badge.objects.get(id=badge_id)
            UserBadge.objects.create(user=user, badge=badge)
            return Response({'message': 'Badge awarded successfully!'}, status=status.HTTP_201_CREATED)
        except Badge.DoesNotExist:
            return Response({'error': 'Badge not found'}, status=status.HTTP_404_NOT_FOUND)

# View to fetch user level and experience
class UserLevelAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        level, _ = UserLevel.objects.get_or_create(user=user)
        serializer = UserLevelSerializer(level)
        return Response(serializer.data)

    # Optionally: API to add experience points and automatically level up
    def post(self, request):
        user = request.user
        experience = request.data.get('experience', 0)

        # Get or create user level
        user_level, _ = UserLevel.objects.get_or_create(user=user)
        user_level.add_experience(experience)

        serializer = UserLevelSerializer(user_level)
        return Response(serializer.data, status=status.HTTP_200_OK)
