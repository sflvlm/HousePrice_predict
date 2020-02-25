from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy as np
from predict import price_predict
# Create your views here.
def index(request):
    return render(request,'predict/index.html')

def count(request):
    area = request.POST.get('area')
    room_num = request.POST.get('room_num')
    hall_num = request.POST.get('hall_num')
    floor = request.POST.get('floor')
    dire = request.POST.get('dire')
    site = request.POST.get('site')


    if not all([area, room_num, hall_num,floor,dire,site]):
        # 数据不完整
        return render(request, 'index.html', {'errmsg': '数据不完整'})

    data = pd.DataFrame(np.array([[area, 2005, room_num,hall_num,floor,dire,0,1,1,1500,site]]),
                        columns=['area', 'buildtime', 'room_num','hall_num','floor','dire','exemption of business tax',
                                 'exemption of double tax','quality education','distance','loc'])
    data.astype('float32')
    print(data)
    price = price_predict.Knn_predict(data)
    price = int(price)
    return render(request,'predict/index.html',{'price':price})
    # return JsonResponse({'price':price})