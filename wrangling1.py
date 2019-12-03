import pandas as pd
a1={'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
b1={'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
c1={'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
d1={'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
a=pd.DataFrame(a1,columns=['Student','Math'])
b=pd.DataFrame(b1,columns=['Student','Electronics'])
c=pd.DataFrame(c1,columns=['Student','GEAS'])
d=pd.DataFrame(d1,columns=['Student','ESAT'])
A=pd.merge(a,b,on='Student')
B=pd.merge(c,d,on='Student')
C=pd.merge(A,B,on='Student')
D=pd.melt(C,id_vars='Student',value_vars=['Math','Electronics','GEAS','ESAT'])
E=D.sort_values('Student')
We_Bear_Bears=E.rename(columns={'variable':'Subject','value':'Grades'})
