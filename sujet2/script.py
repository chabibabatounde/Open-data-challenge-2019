# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys;
import process as ps

args = sys.argv

#Récupération de la liste des pays disponible
#[BASE] pays
if args[1] == "pays":
    ps.listePays()

#Dépense par mois pour tous les pays
#[BASE] barLess [AAAA-MM]
if args[1] =="barLess":
    ps.barLessData(args[2])

#Dépense par mois pour tous les pays
#[BASE] barLess [AAAA-MM]
if args[1] =="pieGraph":
    ps.pieGraph(args[2])

#Evolution des dépenses par pays
#[BASE] evolution [Pays]
if args[1] =="evolution":
    ps.evolution(args[2])
