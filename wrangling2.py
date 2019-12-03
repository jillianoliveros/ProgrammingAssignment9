import pandas as pd
a1={'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]}
a=pd.DataFrame(a1,columns=['Box','Dimension','Value'])
b=a.pivot_table(index='Box',columns=['Dimension'],values='Value').reset_index()
Volume=b.assign(Volume=lambda b: b.Length*b.Width*b.Height)
