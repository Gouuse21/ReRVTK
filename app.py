from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_number', methods=['POST'])
def save_number():
    phone_number = request.form['phone']
    with open('Numbers.txt', 'a') as file:
        file.write(phone_number + '\n')
    return 'Номер сохранен в базу, спасибо!'

if __name__ == '__main__':
    app.run(debug=True)
