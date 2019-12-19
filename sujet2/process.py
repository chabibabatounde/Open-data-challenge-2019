
import datastore as store

def listePays():
    data = store.getAll()
    liste = []
    for ligne in data['records']:
        if not (ligne['fields']['cou_text_fr'] in liste):
            print(ligne['fields']['cou_text_fr'])
            liste.append(ligne['fields']['cou_text_fr'])
    return liste