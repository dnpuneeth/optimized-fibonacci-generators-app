from django.shortcuts import render
import math
from .models import Store
from datetime import datetime
# Create your views here.

def resp(request):
    return render(request, 'fibonacci/resp.html', {'pre':''})


def timeit(fn):
    def timed(*args):
        global elapsed
        start_time = datetime.now()
        result = fn(*args)
        end_time = datetime.now()
        elapsed = "Duration: {}".format(end_time - start_time)
        return result
    return timed 

def fib(n):
    if n < 0:
        return "Enter positive number"

    if n == 0:
        return 1
    
    a, b = 0, 1
    res = []
    
    for i in range(n):
        a, b = b, a+b
        res.append(a)
    return res[n-1]

@timeit
def find(request):
    strt = datetime.now()
    if request.method == 'POST':
        num = request.POST.get('num')
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])
        try:
            pre = Store.objects.get(num=num)
        except (KeyError, Store.DoesNotExist):
            f = fib(int(num))
            record = Store(num=num, values=f)
            record.save()
            return render(request, 'fibonacci/resp.html', {
                'pre': f,
                'num': ordinal(int(num)),
                'time': elapsed
            })
        res = pre.values
        end = datetime.now()
        elap = "Duration {} ".format(end - strt)
        return render(request, 'fibonacci/resp.html', {
            'pre': res,
            'num': ordinal(int(num)),
            'time': elap 
        })