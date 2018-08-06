from pymongo import MongoClient
from flask import *
import mlab

mlab.connect()

all_river = river.find({continent: "Africa"})

print(river[0])
