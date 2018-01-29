def fib(x1,x2): #считает отношение кубов к квадратам четных чисел Фибоначчи
    lst=[x1,x2]
    f=0
    while f<4000000:  #добавляет в список сумму двух предыдущих элементов
	      f=lst[-1]+lst[-2] 
	      lst.append(f)  
    #отбираем только четные числа
    M=[x for x in lst if x%2==0]
    #создаем списки с квадратами и кубами четных чисел и ищем их сумму
    squares=[x**2 for x in M]
    sum_sq=sum(squares)
    cubes=[x**3 for x in M]
    sum_cub=sum(cubes)
    result=sum_cub/sum_sq
    return result

print ('result =', fib(1.0,2.0))
