fiebre = True
tos = True
fatiga = True

if fiebre and tos and fatiga:
    print("Alta probabilidad de influenza") 
elif fiebre and tos: 
    print("Posible infección respiratoria") 
else: 
    print("Sin diagnóstico")