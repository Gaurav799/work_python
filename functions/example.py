def si_calc():
    p=float(input('enter theprinciple: '))
    r=float(input('enter the rate of intrest: '))
    t=float(input('enter the time: '))
    si=p*(r*t)/100
    print(f'Simple Intrest is {si}')
si_calc()

def ci_calc():
    p=float(input('enter theprinciple: '))
    r=float(input('enter the rate of intrest: '))
    t=float(input('enter the time: '))
    ci=p*(1+r/100)**t
    print(f'compound Intrest is {ci}')
ci_calc()