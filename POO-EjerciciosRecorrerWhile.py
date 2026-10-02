Lista=[5,20,15,30,45,0,1,8,15,23]
i=0
M:int = Lista[0]
while i < len(Lista):
         if M < Lista[i]:
            M:int = Lista[i]
         i = i + 1
print("El número mayor es:", M)

i=0
m:int = Lista[0]
while i < len(Lista):
         if m > Lista[i]:
            m:int = Lista[i]
         i = i + 1
print("El número menor es:", m)

print( "El promedio es:", sum(Lista)/len(Lista))
