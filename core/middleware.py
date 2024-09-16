from django.http import JsonResponse

class RoleBasedRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Handle based on user role
            if request.user.is_admin():
                return JsonResponse({'detail': 'Redirect to admin homepage', 'role': 'admin'}, status=200)
            elif request.user.is_teacher():
                return JsonResponse({'detail': 'Redirect to teacher homepage', 'role': 'teacher'}, status=200)
            elif request.user.is_student():
                return JsonResponse({'detail': 'Redirect to student homepage', 'role': 'student'}, status=200)
        
        # If user is not authenticated, proceed with the request normally
        return self.get_response(request)
