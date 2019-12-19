
import matplotlib.pyplot as plt
import datastore as store
import uuid 

def listePays():
    data = store.getAll()
    liste = []
    for ligne in data['records']:
        if not (ligne['fields']['cou_text_fr'] in liste):
            print(ligne['fields']['cou_text_fr'])
            liste.append(ligne['fields']['cou_text_fr'])
    return liste

def barLessData(periode):
    filename = str(uuid.uuid1())
    data = store.getBarLessData(periode)
    toPlot = {}
    for ligne in data['records']:
        if(ligne['fields']['cou_text_fr']=="Royaume-Uni de Grande-Bretagne et d'Irlande du Nord"):
            toPlot["Royaume-Uni"] =ligne['fields']['sum_i1']
        else:
            toPlot[ligne['fields']['cou_text_fr']] =ligne['fields']['sum_i1']

    names = list(toPlot.keys())
    values = list(toPlot.values())
    fig, axs = plt.subplots(1, 1,sharey=True)
    fig.suptitle("Transactions par pays d'origine")
    axs.bar(names, values, color=['red', 'orange', 'blue', 'green'])
    plt.xticks(rotation='vertical')
    plt.tight_layout()
    plt.savefig('/Applications/XAMPP/xamppfiles/htdocs/dataviz/img/'+filename+'.png')
    print(filename+'.png')

def pieGraph(periode):
    filename = str(uuid.uuid1())
    data = store.getBarLessData(periode)
    pays = []
    valeurs = []
    for ligne in data['records']:
        if(ligne['fields']['cou_text_fr']=="Royaume-Uni de Grande-Bretagne et d'Irlande du Nord"):
            pays.append("Royaume-Uni")
        else:
            pays.append(ligne['fields']['cou_text_fr'])
        
        valeurs.append(ligne['fields']['sum_i1'])
    fig, ax1 = plt.subplots(1, 1,  sharey=True)
    ax1.pie(valeurs,  labels=pays, autopct='%1.1f%%',startangle=90)
    ax1.axis('equal') 
    fig.suptitle('Répartition des dépenses sur la période de '+periode)
    plt.savefig('/Applications/XAMPP/xamppfiles/htdocs/dataviz/img/'+filename+'.png', dpi=500)
    print(filename+'.png')

    

def evolution(pays):
    filename = str(uuid.uuid1())
    data =  store.getEvolutionData(pays)
    toPlot = {}
    valeurPlot = {}
    for ligne in data['records']:
        toPlot[ligne['fields']['mois_annee']] =ligne['fields']['sum_i1']
        valeurPlot[ligne['fields']['mois_annee']] =ligne['fields']['sum_i2']
    names = list(toPlot.keys())
    values = list(toPlot.values())
    fig, axs = plt.subplots(1, 1,  sharey=True)
    axs.plot(names, values)
    axs.plot(names, list(valeurPlot.values()))
    plt.xticks(rotation='vertical')
    fig.suptitle('Evolution des transaction : Pays = '+pays)
    #plt.ylabel("Valeurs")
    plt.tight_layout()
    plt.savefig('/Applications/XAMPP/xamppfiles/htdocs/dataviz/img/'+filename+'.png', dpi=500)
    print(filename+'.png')