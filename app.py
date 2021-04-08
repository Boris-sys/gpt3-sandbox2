import os
from flask import Flask, request, render_template
from gpt import set_openai_key, GPT, Example
KEY_NAME = "OPENAI_KEY"

app = Flask(__name__)
set_openai_key(os.environ[KEY_NAME])

@app.route('/')
def index():
    return render_template('index.html',title=title,context=context)

@app.route('/query', methods=['POST'])
def request_query():
    query = request.form['query']
    response = gpt.submit_request(query)
    return {'text': response['choices'][0]['text'][7:]}             



title = '¿Que le respondo al profe?'
context = 'El objetivo de esta simulación es encontrar la respuesta perfecta para darle al profe en una situación complicada.'

examples={
'Profesor: que pensás hacer respecto a tus trabajos prácticos?':'Yo: Trataré de hacer todos los trabajos prácticos antes de que terminen las clases.',
'Profesor: Alguna duda te quedó respecto de la clase?':'Yo: Creo que me gustaría que volviera a explicar el tema pero con menos detalles para tener una idea más clara.',
'Profesor: Todo listo para el examen final?':'Yo:  Si profe, he estado estudiando todos los temas, alguna recomendación sobre qué estudiar en específico?',
'Profesor: Has estado teniendo algún problema al llevar la clase?':'Yo:  En general todo bien, pero he tenido algunos problemas con un par de temas.'
}

gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100,
          context=context)

gpt.add_examples(examples)


if __name__ == "__main__":
    app.run(debug=1)