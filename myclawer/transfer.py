import pandas as pd
import  jsonlines
import  json







with open("test3", mode='r') as f:

     rows =f.readlines()
     for row in  rows :
      print(row)
      json.loads(row)
