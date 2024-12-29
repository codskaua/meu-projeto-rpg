from flask import Flask, render_template, request

app = Flask(__name__)

# Definindo variáveis globais
vida = 20
max_vida = 20
nome = "Jogador"
idade = "25"

@app.route('/')
def home():
    global vida, nome, idade
    return render_template('index.html', vida=vida, nome=nome, idade=idade, max_vida=max_vida)

@app.route('/alterar', methods=['POST'])
def alterar():
    global vida, nome, idade
    if request.form.get('botao_vida') == 'menos':
        vida -= 1
    elif request.form.get('botao_vida') == 'mais':
        vida += 1
    
    if vida > max_vida:
        vida = max_vida  # Não limita vida no frontend

    if 'nome' in request.form:
        nome = request.form['nome']
    if 'idade' in request.form:
        idade = request.form['idade']
    
    return render_template('index.html', vida=vida, nome=nome, idade=idade, max_vida=max_vida)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
