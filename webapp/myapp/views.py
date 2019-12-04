from django.shortcuts import render
import numpy as np
def convert_to_ndarray(x):
    #y = np.random.random((6,5))
    x =x.replace('[','')
    x =x.replace(']','')
    y = []
    for line in x.split('\n'):
        y.append(list(map(float, line.split())))
    return np.array(y)

# Create your views here.
def matmul(req):
    a = convert_to_ndarray('1 2 3\n6 7 8\n1 5 3')
    b = convert_to_ndarray('1 2 3 4 5\n6 7 8 9 1\n2 6 5 5 5')
    if req.method == 'POST':
        a = convert_to_ndarray(req.POST['A'])
        b = convert_to_ndarray(req.POST['B'])
        
    else:
        print('GET เด้อ')
    return render(req, 'myapp/matmul.html' , {
        'A': a,
        'B': b,
        'C': np.dot(a,b)
    })
