import os
os.system('clear')



class A:
    var_da_classe = 123  # var de classe
    
    def __init__(self) -> None:
        pass
    
a1 = A()
a2 = A()

A.var_da_classe = 321

print(a1.var_da_classe)
print(a2.var_da_classe)
print(A.var_da_classe)
  