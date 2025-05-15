DEEPINFRA=51GFc4Nzy5almW9uahWBMetKTpLcXd3Y

def search_food(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({'error': 'No query provided'}, status=400)

    url = "https://api.edamam.com/api/recipes/v2"
    params = {
        'type': 'public',
        'q': query,
        'app_id': '53938627',
        'app_key': '0e18bd84353f5704d35a0079a2eb3fc4'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data, safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)