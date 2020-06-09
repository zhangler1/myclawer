import pandas as pd
data5 = {   "id1": {'a':4, 'b':{5:"a"}, 'c':5, 'd':7, 'e':8},
   "id2":{'a':1, 'b':2,'c':3 ,'d':4,  'e':5}
            }



print('(5)由字典组成的字典')
print(pd.DataFrame(data5))