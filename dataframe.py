PData={'Country':['China','India','United States','Indonesia','Brazil','Pakistan'],'Population':[1379750000,1330780000,324882000,260581000,2606918000,194754000],'BirthRate':[12.00,21.76,13.21,18.84,18.43,27.62],'UpdateDate':['2016-08-11','2016-08-11','2016-07-01','2016-08-11','2016-08-11','2017-02-22']}
import pandas as pd
df=pd.DataFrame(PData,columns=['Country','Population','BirthRate','UpdateDate'])
print(df)
