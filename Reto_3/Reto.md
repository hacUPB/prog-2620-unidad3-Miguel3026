## Datos de entrada


| nombre | tipo | descripción |
|------|------|-------------|
| CI | float | Cantidad de combustible inicial ingresada por el usuario en kilogramos |
| H | int | Número de tramos de vuelo que se van a simular |
| D | float | Distancia del tramo de vuelo ingresada por el usuario en kilómetros |
| V | float | Velocidad del viento ingresada por el usuario en km/h, positiva si es a favor y negativa si es en contra |

## Datos Constantes

| nombre | tipo | descripción |
|------|------|-------------|
| CP | int | Consumo por hora del avión en kilogramos por hora |
| VC | int | Velocidad de crucero del avión en kilómetros por hora |
| DC | float | Densidad del combustible Jet A-1 en kilogramos por litro |
| RL | int | Cantidad mínima de combustible que debe mantenerse como reserva legal |
| VMS | int | Velocidad mínima segura del avión para evitar entrar en pérdida (stall) |
| FHW | float | Factor de incremento del consumo cuando hay viento en contra |
| FTW | float | Factor de reducción del consumo cuando hay viento a favor |


## Variables o datos de control

| nombre | tipo | descripción |
|------|------|-------------|
| CA | float | Combustible actual disponible durante cada tramo del vuelo |
| i | int | Contador que representa el número de tramo de vuelo |
| VT | float | Velocidad total del avión |
| TT | float | Tiempo necesario para recorrer el tramo |
| CF | float | Factor de corrección aplicado al consumo según el tipo de viento |
| TW | str | Tipo de viento detectado en el tramo (FAVOR, CONTRA o NULO) |
| EST | str | Estado del sistema según el combustible disponible (OK, CRITICO, STALL o INSUFICIENTE) |


## Datos de salida

| nombre | tipo | descripción |
|------|------|-------------|
| CKG | float | Combustible consumido durante el tramo en kilogramos |
| CPF | float | Combustible final proyectado después del tramo |
| VT | float | Velocidad total resultante usada para el cálculo |
| TT | float | Tiempo calculado para recorrer la distancia |
| TV | str | Resultado que indica el tipo de viento presente |
| EST | str | Estado final del sistema según seguridad de velocidad y combustible |
| CA | float | Combustible restante después de cada tramo mostrado en la tabla del programa |

## Pseudocodigo 
````
inicio

CP = 5400
VC = 900
DC = 0.785
RL = 1200
VMS = 185
FHW = 1.25
FTW = 0.85

mostrar "Sistema de gestion de combustible"

leer CI
leer H

si CI < RL entonces
    mostrar "error: combustible insuficiente"
sino

    CA = CI

    para i desde 1 hasta H+1

        mostrar "tramo ", i

        leer D
        leer V

        VT = VC + V

        si VT <= VMS entonces
            mostrar "alerta: entrando en stall"
            mostrar "abortando vuelo"
            terminar ciclo
        fin si

        TT = D / VT

        si V > 5 entonces
            CF = FTW
            TV = "favor"
        sino
            si V < -5 entonces
                CF = FHW
                TV = "contra"
            sino
                CF = 1
                TV = "nulo"
            fin si
        fin si

        CKG = CP * TT * CF
        CPF = CA - CKG

        si CPF < RL entonces
            mostrar "alerta: combustible insuficiente"
            mostrar "abortando vuelo"
            terminar ciclo
        fin si

        CA = CA - CKG

        mostrar "consumo:" CKG
        mostrar "combustible restante:", CA

    fin para

    mostrar "fin del vuelo"
    mostrar "combustible final:", CA

fin si

fin

````

## Uso de IA
Se uso IA para la parte de los print, dando un resultado mas estetico dinamico y corrección de errores de logica en el codigo, como la funcion, que relaciona el viento,  la distancia y el tiempo. haciendonos cambiar de contador, segmentando los tramos en algo dado por el usuario