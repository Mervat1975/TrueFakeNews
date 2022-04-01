
from django.shortcuts import render
import pandas as pd
import os
import pickle

# Create your views here.


def predict(text):

    filename = 'finalized_model2.sav'

    # load the model from disk
    loaded_model = pickle.load(open(os.path.join(filename), 'rb'))
    text_arr = []
    text_arr.append(text)
    prediction = loaded_model.predict(text_arr)
    return prediction


def classifier(request):
    if request.method == 'GET':
        result = "none"
        return render(request, 'index.html', {'result': result})
    elif request.method == 'POST':
        post_data = request.POST
        textnews = str(post_data.get('textnews'))
        result = predict(textnews)
        result = str(result).replace("'", "").replace("[", "").replace("]", "")
        return render(request, 'index.html', {'result': result, 'textnews': textnews})
