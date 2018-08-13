import pandas as pd
import excel
var1=pd.read_excel("C:\\Users\\DELL\\Desktop\\dataset.xlsx",0)
var2=pd.read_excel("C:\\Users\\DELL\\Desktop\\dataset.xlsx",0)

CE_ME=0 #Number of civil and mechanical students
l1=var1.describe()
l2=var2.describe()
req=0

#var1 is the original sheet and var2 is the final sheet after applying all constraint
for i in range(l2.Name[0]):
  if(var2["Year"][i]>=str("3rd")):
#Accessing name and email in separate variables
    name=var2["Name"][i]
    mail=var2["Email"][i]
    firstName=name.split(' ')[0] 
    lastName=name.split(' ')[1]
 #Now removing all the 3rd and 4th year students whose first or last name matches with email id.   
    if firstName.lower() in mail:
      var2.drop([i],axis= 0, inplace=True)

    elif lastName.lower() in mail:
      var2.drop([i],axis= 0, inplace=True)
      

#rearranging the sheet after the deletion of row, (reindexing)
var2=var2.reset_index(drop=True)
l2=var2.describe()

for i in range(l2.Department[0]):
  if(var2["Department"][i]=='CE'):
    CE_ME=CE_ME+1
    continue
  if(var2["Department"][i]=='ME'):
    CE_ME=CE_ME+1
    continue
   
# 10% of the attending student(req)
req=l2.Name[0]*(0.1)
#applying the constraints
if(l2.Name[0]>30): 
  if(CE_ME>=req):
    print("DrAiveX will  EXIST")
  else:
    print("DrAiveX will not EXIST")
    
  
else:
  print("DrAiveX will not EXIST")



