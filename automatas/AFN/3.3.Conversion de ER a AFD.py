def mostrar_ejercicio_corregido():
    #árbol contruido
    hojas = {
        1: '1', 2: '1', 3: '0', 
        4: '0', 5: '0', 6: '1', 
        7: '#'
    }

    print("REPRESENTACIÓN DEL ÁRBOL")
    print(""" 
                             {1,3,4,6,7}  raíz  {7}      
                               ____________ . ____________   
                             /                             \\
               {1,3,4,6}    /   {2,3,5,6}                   \\
                 _________ . _________                      #
                /                     \\                     0  
               /       1               \\                    7
        {1,3} * {2,3}             {4,6} * {5,6}          {7}  {7}            
              | 1                       | 1
              |                         |
       {1,3}  +  {2,3}           {4,6}  +  {5,6}
            / 0\\                      / 0\\
           /    \\                    /    \\
          /      \\                  /      \\
    {1}  .  {2}   0           {4}  .  {5}    1 
       / 0\\      0               / 0\\        6
      /    \\     3 0            /    \\    {6} {6} 
     /      \\ {3} {3}          /      \\      
     1        1                0        0
     0        0                0        0
    (1)      (2)              (4)      (5)
  {1} {1}  {2} {2}          {4} {4}  {5} {5}          
    """)

    # Resultado de siguientes
    siguiente = {
        1: {2},
        2: {1, 3, 4, 6, 7},
        3: {1, 3, 4, 6, 7},
        4: {5},
        5: {4, 6, 7},
        6: {4, 6, 7},
        7: set()
    }

    print("RESULTADO DE SIGUIENTE(1)-SIGUIENTE(7):")
    for i in range(1, 8):
        valor = sorted(list(siguiente[i])) if siguiente[i] else "φ"
        print(f"siguiente({i}) = {valor}")

    # Construcción del AFD 
    # Estado inicial q0 
    q0 = frozenset({1, 3, 4, 6, 7})
    estados_revisar = [q0]
    nombres_estados = {q0: "A"}
    transiciones = {}
    
    alfabeto = ['0', '1']

    while estados_revisar:
        actual = estados_revisar.pop(0)
        nombre_actual = nombres_estados[actual]
        transiciones[nombre_actual] = {}

        for simbolo in alfabeto:
            proximo_set = set()
            for pos in actual:
                if hojas.get(pos) == simbolo:
                    proximo_set.update(siguiente[pos])
            
            estado_res = frozenset(proximo_set)
            
            if estado_res not in nombres_estados:
                nombres_estados[estado_res] = str(len(nombres_estados))
                estados_revisar.append(estado_res)
            
            transiciones[nombre_actual][simbolo] = estado_res

    # Tabla de transición de estados del AFD 
    print("\n3. TABLA DE TRANSICIÓN DE ESTADOS:")
    header = f"{'Estado (q)':<25} | {'0':<20} | {'1':<20}"
    print(header)
    print("-" * len(header))
    
    orden = [
        frozenset({1, 3, 4, 6, 7}),
        frozenset({1, 3, 4, 5, 6, 7}),
        frozenset({2, 4, 6, 7}),
        frozenset({5}),
        frozenset({4, 6, 7}),
        frozenset()
    ]

    for est in orden:
        q_str = str(sorted(list(est))) if est else "φ"
        
        # Calcular destinos
        t0_set = set()
        t1_set = set()
        for p in est:
            if hojas.get(p) == '0': t0_set.update(siguiente[p])
            if hojas.get(p) == '1': t1_set.update(siguiente[p])
        
        dest0 = str(sorted(list(t0_set))) if t0_set else "φ"
        dest1 = str(sorted(list(t1_set))) if t1_set else "φ"
        
        print(f"{q_str:<25} | {dest0:<20} | {dest1:<20}")

if __name__ == "__main__":
    mostrar_ejercicio_corregido()