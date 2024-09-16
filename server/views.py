from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login
from rest_framework_simplejwt.tokens import RefreshToken
from core.models import LoginSystem
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        access_token = data.get('access_token')

        if access_token:
            if request.session.get('access_token') == access_token:
                next_url = request.GET.get('next', '/')
                return JsonResponse({'next': next_url, 'status': 302}, status=302)
            else:
                return JsonResponse({'detail': 'Invalid access token'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                # Log in the user if the subscription is valid
                auth_login(request, user)
                refresh = RefreshToken.for_user(user)
                access = str(refresh.access_token)

                # Save tokens to LoginSystem model
                create_token(user, refresh, access)
                request.session['access_token'] = access
                request.session['refresh_token'] = str(refresh)
                
                response_data = {
                    'access_token': access,
                    'refresh_token': str(refresh),
                }
                return JsonResponse({'detail': 'Login Successful', 'data': response_data, 'status': 200}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return JsonResponse({'detail': 'Method not allow'})




def create_token(user, refresh, access):
    try:
        token = LoginSystem.objects.get(username=user.username)
        token.access_token = str(access)
        token.refresh_token = str(refresh)
        token.save()
    except LoginSystem.DoesNotExist:
        print('Failed to create token')
    return token


from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class LogoutView(DjangoLogoutView):
    @method_decorator(login_required)  # Ensure the user is logged in
    def dispatch(self, request, *args, **kwargs):
        # Custom logic to set the token fields to null
        user = request.user
        if hasattr(user, 'server'):
            user.serve.access_token = None
            user.serve.refresh_token = None
            user.serve.save()
        request.session.flush()
        # Call the parent dispatch method
        return super().dispatch(request, *args, **kwargs)
