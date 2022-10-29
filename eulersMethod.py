def main():
    x0 = 2
    y0 = 3
    dx = 0.1
    runs = 5
    eulersMethod(x0,y0,dx,runs)
    
def f(x: float,y: float) -> float:
    return x + 2 * y
    
def eulersMethod(x: float, y: float, width: float, num: int):
    print(f"x0 = {x}\t\ty0 = {y}")
    for i in range(1,num+1):
        y = y + f(x,y) * width
        x = x + width
        print(f"x{i} = {x}\t\ty{i} = {y}")
    
main()