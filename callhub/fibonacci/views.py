from django.shortcuts import render
import math
from .models import Store
from datetime import datetime
# Create your views here.

def resp(request):
    if request.method == 'GET':
        return render(request, 'fibonacci/resp.html', {'res':''})

    if request.method == 'POST':
        start_time = datetime.now()
        num = request.POST.get('num')
        ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])
        try:
            q_set = Store.objects.get(num=num)
        except (KeyError, Store.DoesNotExist):
            f = fib(int(num))
            record = Store(num=num, values=f)
            record.save()
            end_time = datetime.now()
            elapsed = end_time - start_time
            return render(request, 'fibonacci/resp.html', {
                'res': f,
                'num': ordinal(int(num)),
                'time': elapsed
            })
        res = q_set.values
        end = datetime.now()
        elap = end - start_time
        return render(request, 'fibonacci/resp.html', {
            'res': res,
            'num': ordinal(int(num)),
            'time': elap 
        })

def fib(n):
    if n == 0:
        return 0
    
    a, b = 0, 1
    res = []
    
    for i in range(n):
        a, b = b, a+b
        res.append(a)
    return res[n-1]