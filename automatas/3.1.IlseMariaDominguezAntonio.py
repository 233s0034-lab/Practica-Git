# Definición del AFD
Q = {"q0", "q1", "q2", "q3"}      
Σ = {"0", "1"}                     
q0 = "q0"                         
F = {"q0"}                         

# Función de transición δ 
δ = {
    "q0": {"0": "q2", "1": "q1"},
    "q1": {"0": "q3", "1": "q0"},
    "q2": {"0": "q0", "1": "q3"},
    "q3": {"0": "q1", "1": "q2"}
}

print("Q:",Q)
print("Σ:",Σ)
print("q0:",q0)
print("F:",F)
print("δ:",δ)

def delta_hat(state, w):
    """Función δ*(q, w) que procesa la cadena w"""
    current_state = state
    recorrido = [current_state]  # Guardar el camino de estados
    for symbol in w:
        current_state = δ[current_state][symbol]
        recorrido.append(current_state)
    return current_state, recorrido

def acepta(w):
    """Verifica si la cadena w es aceptada por el AFD"""
    final_state, recorrido = delta_hat(q0, w)
    aceptada = final_state in F
    # Mostrar procedimiento paso a paso
    print(f"\nCadena: {w}")
    for i in range(1, len(recorrido)):
        prefijo = w[:i]
        print(f"δ*(q0, {prefijo}) = {recorrido[i]}")
    print(f"Estado final alcanzado: {final_state}")
    print("Resultado:", "Aceptada" if aceptada else "No aceptada")

# Evaluar ambas cadenas
cadenas = ["1010", "011"]
for w in cadenas:
    acepta(w)

