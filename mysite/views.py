from django.shortcuts import render,redirect
import requests
import pandas as pd
import numpy as np
import csv
from django.http  import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Inventory,Raw_material
from .forms import InventoryForm
context={}
def upload(request):
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url']=fs.url(name)
    return render(request,'upload.html',context)
def file_list(request):
    inventories=Inventory.objects.all()
    raw=Raw_material.objects.all()
    for i in range(len(inventories)):
     url=inventories[i].csv_file.url
     url='http://127.0.0.1:8000'+url
     data=pd.read_csv(url)
     df=pd.DataFrame(data)
     df['Date']=inventories[i].date
     df['volume (m3)']=df['WIDTH']*df['LENGTH']*df['SIZE']*10**-9
     df['cost (USD)'].fillna(1000//(df['volume (m3)']*8),inplace=True)
     df['price_per_volume (USD/m3)']=df['cost (USD)']//df['volume (m3)']
     df['weight (in kg)']=df['volume (m3)']*8000
     df['price_per_weight (USD/kg)']=df['cost (USD)']/df['weight (in kg)']
     url1=raw[0].csv_file.url
     url1='http://127.0.0.1:8000'+url1
     print(url1)
     file1=pd.read_csv(url1)
     df1=pd.DataFrame(file1)
     raw=[]
     for j,r in df.iterrows():
       c=np.random.choice(range(1188))
       raw.append(df1.loc[c]['M1'])
     df['raw_price']=raw
     df['indexing_ratio']=df['cost (USD)']/df['raw_price']
     df.to_csv('media/inventory/inventory'+str(i)+'.csv')
     inventories[i].csv_file='inventory/inventory'+str(i)+'.csv'
     inventories[i].save()

    
    return render(request,'files_list.html',{'inventories':inventories})
def upload_csv(request):
    
        if request.method=='POST':
          form=InventoryForm(request.POST,request.FILES)
          r=Raw_material()
          r.csv_file='stock_closing.csv'
          r.save()
          if form.is_valid():
            form.save()
            return redirect('files_list')
        else:
            form=InventoryForm()
        return render(request,'upload_csv.html',{'form':form})
# Create your views here.
