from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    """Home page view."""
    try:
        return render(request, 'index.html')
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)
