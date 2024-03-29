# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys;
import json;
import requests

def getAll():
    data =  "[]"
    url =  "https://www.data.corsica/api/records/1.0/search/?dataset=indice-tourisme-destination-regions&facet=cou_text_fr&facet=nom_reg&facet=mois_annee"
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
    return data

def getBarLessData(periode):
    data =  "[]"
    url =  "https://www.data.corsica/api/records/1.0/search/?dataset=indice-tourisme-destination-regions&facet=cou_text_fr&facet=nom_reg&facet="+periode
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
    return data

def getEvolutionData(pays):
    data =  "[]"
    url =  "https://www.data.corsica/api/records/1.0/search/?dataset=indice-tourisme-destination-regions&lang=fr&rows=3070&refine.cou_text_fr="+pays
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
    return data
