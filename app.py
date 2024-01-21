from flask import Flask, render_template, request, redirect, url_for, flash
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_number', methods=['POST'])
def save_number():
    phone_number = request.form['phone']
    with open('Numbers.txt', 'a') as file:
        file.write(phone_number + '\n')
    flash('Номер сохранен в базу, спасибо!')
    time.sleep(1)  # Подождать 1 секунду перед перенаправлением
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
