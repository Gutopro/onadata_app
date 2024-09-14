import requests
from django.http import JsonResponse, HttpResponse
# Create your views here.


def fetch_form_data(request, form_id):
    """ fetches form data from onadata api """
    api_url = f"https://api.ona.io/api/v1/forms/{form_id}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data, safe=False)
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return JsonResponse({'error': f"Form ID {form_id} does not exist."}, status=404)
        return JsonResponse({'error': f"HTTP error occurred: {http_err}"}, response.status_code)
    except requests.exceptions.RequestException as req_err:
        return JsonResponse({'error': f"Network error occurred: {req_err}"}, status=500)
