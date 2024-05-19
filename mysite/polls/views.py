from django.shortcuts import render, redirect
import pandas as pd
import pickle
import math

def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['sex'] # select
        bmi = request.POST['bmi']
        child = request.POST['child']
        smoker = request.POST['smoker'] # select
        region = request.POST['region'] # select

        if name != "":
            
            df = pd.DataFrame(columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

            df2 = {
                'age': float(age),
                'sex': int(gender),
                'bmi': float(bmi),
                'children': int(child),
                'smoker': int(smoker),
                'region': int(region)
            }

            # Convert the dictionary to a DataFrame and concatenate it with the original DataFrame
            df = pd.concat([df, pd.DataFrame([df2])], ignore_index=True)
            # load the model from disk
            model = 'polls/Medical.pickle'
            loaded_model = pickle.load(open(model, 'rb'))
            res = loaded_model.predict(df)
            res=math.ceil(res*100)/100

            print(res)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})
