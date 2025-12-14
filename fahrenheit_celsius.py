def f_to_c(f):
    return 5*(f-32)/9
    
f = int(input("enter the temeperature in f:"))
print(f"{round(f_to_c(f),2)}")
