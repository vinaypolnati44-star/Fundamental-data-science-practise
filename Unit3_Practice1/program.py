import pandas as pd
from pandas import json_normalize

data = {
 "students":[
  {"name":"Ram","details":{"age":20,"marks":85}},
  {"name":"Sita","details":{"age":19,"marks":90}},
  {"name":"Ravi","details":{"age":21,"marks":78}}
 ]
}

df = json_normalize(data["students"])
print(df)
