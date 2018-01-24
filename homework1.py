import math
import cmath

def vietas_solution(b,c): #решение с помощью теоремы виета
    d = b**2 - 4*c
    if d >= 0:
        sqd = math.sqrt(d)
        if b>= 0:
            x1 = (-b - sqd) / 2.0
        else:
            x1 = (-b + sqd) / 2.0
        x2 = c/x1
    else:
        sqd = cmath.sqrt(d)
        x1 = (-b + sqd) / 2.0
        x2 = (-b + sqd) / 2.0
    return x1, x2
def machineEpsilon(e): #ищет машинный эпсилон (понадобится для функции taylor_solution)
    e = 1.0
    while (1.0 + e/2.0) > 1.0:
        e = e/2.0
    return e
def taylor_solution(b,c): #решение с помощью разложения в ряд
    if b**2 - 4*c < 0:
        x1,x2 = vietas_solution(b,c)
    else:
        if 4*c/b**2 < machineEpsilon(1.0)**2:
            x1 = - b
            x2 = - c / b - (4 * c / b) ** 2 / 16
        else:
            D = b ** 2 - 4 * c
            x1 = (- b + D ** 0.5) / 2
            x2 = (- b - D ** 0.5) / 2
    return x1, x2
  
  #вывод
print("b=4, c=3 \n vieta's formulas: ", vietas_solution(4.0,3.0)," \n Discriminant/taylor series: ",taylor_solution(4.0,3.0 ),"\n")
print("b=2, c=1 \n  vieta's formulas: ",vietas_solution(2.0,1.0), " \n Discriminant/taylor series: ",taylor_solution(2.0,1.0), "\n")
print("b=0.5, c=4 \n vieta's formulas: ",vietas_solution(0.5,4.0), " \n Discriminant/taylor series: ",taylor_solution(0.5,4.0), "\n")
print("b=10^20, c=3 \n vieta's formulas: ",vietas_solution(1e20,3.0)," \n Discriminant/taylor series: ",taylor_solution(1e20,3.0),"\n")
print("b=-10^20, c=4 \n vieta's formulas: ",vietas_solution(-1e20,4.0)," \n Discriminant/taylor series: ",taylor_solution(-1e20,4.0))
