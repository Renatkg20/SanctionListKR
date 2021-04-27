import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import openpyxl

url = 'https://fiu.gov.kg/uploads/607ff83b2fa01.xml'
res = requests.get(url)
Number1 = []
Surname = []
Name = []
Patronomic = []
DataBirth = []
PlaceBirth = []
BasicInclusion = []
CategoryPerson = []
DateInclusion = []

soup = BeautifulSoup(res.content, 'lxml-xml')
soup = soup.find('SanctionList').find_all('KyrgyzPhysicPerson')
for i in soup:
        t = i.find('Number')
        Number1.append(t.get_text())
        Surname.append((i.find('Surname')).get_text())
        Name.append((i.find('Name')).get_text())
        try:
            Patronomic.append((i.find('Patronomic')).get_text())
        except AttributeError:
            Patronomic.append("-")
            
        DataBirth.append((i.find('DataBirth')).get_text())
        try: 
            PlaceBirth.append((i.find('PlaceBirth')).get_text())
        except AttributeError:
            PlaceBirth.append("-")
            
        BasicInclusion.append((i.find('BasicInclusion')).get_text())
        CategoryPerson.append((i.find('CategoryPerson')).get_text())
        try:
            DateInclusion.append((i.find('DateInclusion')).get_text())
        except AttributeError:
            DateInclusion.append("-")
       
        
df = pd.DataFrame({"Supername": Surname,
                   "Name": Name,
                   "Patronomic": Patronomic,
                   "DataBirth": DataBirth,
                   "PlaceBirth": PlaceBirth,
                   "BasicInclusion": BasicInclusion,
                   "CategoryPerson": CategoryPerson,
                   "DateInclusion" : DateInclusion}, index= Number1)

       
df.to_excel("output.xlsx")
 