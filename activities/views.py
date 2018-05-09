# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Activity
import pandas as pd
import os
import requests as rq
from django.conf import settings


def activity_list(request):
    activity_list = Activity.objects.all().order_by('date')
    context = {
                'activity_list':activity_list
    }
    return render(request, 'activities/activities_list.html', context)



def get_drinki(request):
    file_path = os.path.join(settings.STATICFILES_DIRS,"helix_data.csv")
    print(file_path)
    helix_data = pd.read_csv(file_path)
    helix_data.loc[helix_data['User_trait']=='H','trait_value']=15
    helix_data.loc[helix_data['User_trait']=='L','trait_value']=5
    helix_data.loc[helix_data['User_trait']=='M','trait_value']=10
    protein = 0
    micronutrients = 0
    carbs = 0
    for row, ele in helix_data.iterrows():
        protein += int(ele['trait_value'])*int(ele['Protein'])
        micronutrients += ele['trait_value']*ele['Micronutrients']
        carbs += ele['trait_value']*ele['Carb']
    get_drinki={'protein':protein,
                'micronutrients':micronutrients,
                'carbs':carbs}
    sum_drinki = get_drinki['protein']+get_drinki['micronutrients']+get_drinki['carbs']
    get_drinki['carbs'] = round(get_drinki['carbs']/sum_drinki,2)
    get_drinki['protein'] = round(get_drinki['protein']/sum_drinki,2)
    get_drinki['micronutrients'] = round(get_drinki['micronutrients']/sum_drinki,2)
    return render(request, 'activities/get_drinki.html',get_drinki)


def create_drink(request):
    r = rq.get("http://10.248.50.53:5000/make_drink")
    return render(request, 'activities/prepare_drink.html')
# Create your views here.
def goals(request):
    return render(request, 'activities/goals.html')
# Create your views here.
