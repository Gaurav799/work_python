def simple_intrest(p:int, r:int, t:int):
    return (p * r * t) / 100

def compound_intrest(p,r,t):
    return p*(1+r/100) ** t

if __name__ == '__main__':
    p=10000
    r=5
    t=3
    si=simple_intrest(p,r,t)
    ci=compound_intrest(p,r,t)
    print(f'Simple intrest is {si}')
    print(f'Compound intrest is {ci}')

    p=float(input('enter the principle: '))
    r=float(input('enter the rate of intrest: '))
    t=float(input('enter the time: '))
    si= simple_intrest(p,r,t)
    ci=compound_intrest(p,r,t)
    print(f'Simple intrest is {si}')
    print(f'Compound intrest is {ci}')