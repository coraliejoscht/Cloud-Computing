#Question 3
#Coralie JOSCHT et Solène CORRE

import requests
import json
from pprint import pprint
from pymongo import MongoClient
import time
import dateutil.parser

atlas = MongoClient('mongodb+srv://admin:admin123@cluster0.ut8s6.gcp.mongodb.net/bicycle?retryWrites=true&w=majority')

db = atlas.bicycle
def main():
    pass


def nearStation(lat,lon):
    db.stations2.find({'geometry':{
        $near:{
            $geometry:{
                type: "Point",
                coordinates: [lon,lat]
            },
            $maxDistance:1000,
            $minDistance:0
            }
        }})

    #return(list(near_station))
