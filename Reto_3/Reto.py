CP = 5400  # Consumo por hora en kg/hora
VC = 900   # Velocidad crucero en km/h
DC = 0.785 # Densidad del combustible Jet A-1 en kg/litro
RL = 1200  # Reserva legal minima
VMS = 185  # Velocidad minima en km/h (stall)
FHW = 1.25 # Factor headwind (+25% consumo con viento en contra)
FTW = 0.85 # Factor tailwind (-15% consumo con viento a favor)

def Cons_C(D, V, H, CA):
    VT = VC + V
    
    # Validar velocidad minima segura
    if VT <= VMS:
        print(f"\nALERTA CRITICA - ENTRANDO EN STALL")
        print(f"Velocidad total: {VT:.2f} km/h (minima segura: {VMS} km/h)")
        print(f"Abortando ruta en tramo {H}")
        print(f"Buscando aeropuerto mas cercano...\n")
        return None, VT, None, None, "STALL"
    
    TT = D / VT
    
    # Aplicar factor de viento
    if V > 5:
        CF = FTW
        TV = "FAVOR"
    elif V < -5:
        CF = FHW
        TV = "CONTRA"
    else:
        CF = 1.0
        TV = "NULO"
    
    CKG = CP * TT * CF
    CPF = CA - CKG
    
    # Verificar reserva legal
    if CPF < RL:
        print(f"\nALERTA CRITICA - COMBUSTIBLE INSUFICIENTE")
        print(f"Combustible actual: {CA:.2f} kg")
        print(f"Consumo proyectado: {CKG:.2f} kg")
        print(f"Combustible final: {CPF:.2f} kg")
        print(f"Reserva legal requerida: {RL} kg")
        print(f"Abortando ruta en tramo {H}")
        print(f"Buscando aeropuerto mas cercano...\n")
        return CKG, VT, TT, TV, "INSUFICIENTE"
    
    EST = "OK" if CPF > RL + 500 else "CRITICO" #IA
    
    return CKG, VT, TT, TV, EST


print("="*80)
print("SISTEMA DE GESTION DE COMBUSTIBLE del 787 (SMCS) - BIMOTOR COMERCIAL")
print("="*80)

CI = float(input("\nIngrese cantidad de combustible inicial (kg): "))
H = int(input("Ingrese cantidad de tramos a volar: "))

if CI < RL:
    print(f"ERROR: Combustible insuficiente. Minimo requerido: {RL} kg")
else:
    CA = CI
    print(f"\n{'TRAMO':<8} {'DIST(km)':<12} {'VIENTO':<10} {'VEL_TOT(km/h)':<15} {'TIEMPO(h)':<12} {'CONSUMO(kg)':<12} {'COMB_ACTUAL(kg)':<15} {'ESTADO':<12}")
    print("-"*110)
    
    for i in range(1, H + 1):
        print(f"\n--- TRAMO {i} ---")
        D = float(input("Ingrese distancia (km): "))
        V = float(input("Ingrese velocidad del viento (+ favor / - contra): "))
        
        CKG, VT, TT, TV, EST = Cons_C(D, V, i, CA)
        
        if EST == "STALL" or EST == "INSUFICIENTE":
            break
        
        print(f"El consumo de Jet A-1 fue de: {CKG:.2f} kg")
        
        CA = CA - CKG
        
        print(f"{i:<8} {D:<12.1f} {TV:<10} {VT:<15.1f} {TT:<12.2f} {CKG:<12.2f} {CA:<15.2f} {EST:<12}")
    
    print("\n" + "="*80)
    print(f"FIN DEL VUELO - Combustible final: {CA:.2f} kg")
    print("="*80)