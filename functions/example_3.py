def area_of_triangle():
    a=int(input('enter the length of side a: '))
    b=int(input('enter the length of side b: '))
    c=int(input('enter the length of side c: '))
    s=(a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print('The area of the triangle is: ',area)