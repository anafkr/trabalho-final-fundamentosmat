from flask import Flask, render_template, request

app = Flask(__name__)

# --- Torres de Hanói ---
def hanoi(n, origem, destino, auxiliar, passos_lista):
    if n == 1:
        passos_lista.append(f"Mover disco 1 de {origem} para {destino}")
        return
    hanoi(n - 1, origem, auxiliar, destino, passos_lista)
    passos_lista.append(f"Mover disco {n} de {origem} para {destino}")
    hanoi(n - 1, auxiliar, destino, origin=origem, passos_lista=passos_lista)

# Correção na assinatura interna para evitar confusão de parâmetros nomeados
def hanoi_runner(n, origem, destino, auxiliar, lista):
    if n == 1:
        lista.append(f"Mover disco 1 da Torre {origem} para a Torre {destino}")
        return
    hanoi_runner(n - 1, origem, auxiliar, destino, lista)
    lista.append(f"Mover disco {n} da Torre {origem} para a Torre {destino}")
    hanoi_runner(n - 1, auxiliar, destino, origem, lista)


# --- Inversão de String (Rastreando os Passos de retorno) ---
def inverter_string_visual(s, historico):
    if len(s) <= 1:
        historico.append(f"Caso base atingido! String menor ou igual a 1: '{s}'")
        return s
    char_atual = s[-1]
    resto = s[:-1]
    historico.append(f"Pegando o último caractere '{char_atual}' e chamando recursão para o resto: '{resto}'")
    resultado = char_atual + inverter_string_visual(resto, historico)
    historico.append(f"Retornando da chamada com resultado parcial acumulado: {resultado}")
    return resultado


# --- Decimal para Binário (Visualizando divisões e restos) ---
def decimal_para_binario_visual(n, historico):
    if n <= 1:
        historico.append(f"Caso base atingido! Número é {n}. Retorna o próprio '{n}' em string.")
        return str(n)
    
    quociente = n // 2
    resto = n % 2
    historico.append(f"Dividindo {n} por 2 -> Quociente: {quociente}, Resto: {resto} (Guarda o resto {resto})")
    
    resultado_recursivo = decimal_para_binario_visual(quociente, historico)
    resultado_final = resultado_recursivo + str(resto)
    
    historico.append(f"Combinando resultado anterior com o resto: {resultado_recursivo} + '{resto}' = {resultado_final}")
    return resultado_final


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/TorresDeHanoi', methods=['GET', 'POST'])
def torres_de_hanoi():
    passos = None
    discos = 3
    if request.method == 'POST':
        discos = int(request.form.get('discos', 3))
        passos = []
        hanoi_runner(discos, "A", "C", "B", passos)
    return render_template('TorresDeHanoi.html', passos=passos, discos=discos)


@app.route('/InversaoDeString', methods=['GET', 'POST'])
def inversao_de_string():
    resultado = None
    historico = []
    texto = ""
    if request.method == 'POST':
        texto = request.form.get('texto', '')
        resultado = inverter_string_visual(texto, historico)
    return render_template('InversaoDeString.html', resultado=resultado, historico=historico, texto=texto)


@app.route('/DecimalParaBinario', methods=['GET', 'POST'])
def decimal_para_binario():
    resultado = None
    historico = []
    decimal = ""
    if request.method == 'POST':
        decimal = int(request.form.get('decimal', 0))
        resultado = decimal_para_binario_visual(decimal, historico)
    return render_template('DecimalParaBinario.html', resultado=resultado, historico=historico, decimal=decimal)


if __name__ == '__main__':
    print("Iniciando o servidor Flask local...")
    print("Abra o navegador em: http://127.0.0.1:5000")
    app.run(debug=True)
