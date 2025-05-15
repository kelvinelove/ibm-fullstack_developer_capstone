from django.http import JsonResponse
from .restapis import get_request
from django.conf import settings

def get_dealerships(request, state=None):
    if state:
        endpoint = f"/api/dealership?state={state}"
    else:
        endpoint = "/api/dealership"
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships}) 