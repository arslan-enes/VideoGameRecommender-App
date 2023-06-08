from django.shortcuts import render
import requests
from .pyscripts.pymongo_query import get_documents

def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        url = "https://video-game-recommender.herokuapp.com/predict"  # Replace with your API URL
        payload = {
            "query": f"{description}"
        }
        response = requests.post(url, json=payload)
        print("Response code:".upper(), response.status_code)
        data = response.json()
        documents = get_documents(data['recommendations'][0])
        

        documents_list = []
        for document in documents:
            documents_list.append(document)


        return render(request, 'main\\home.html', {'documents': documents_list})
    


    return render(request, 'main\\home.html')


