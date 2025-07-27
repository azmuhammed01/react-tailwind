from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "hello"



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'name' in session:
            return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        if name == "admin" and password == "1234":
            session['name'] = name
            return redirect(url_for("dashboard", name= name.capitalize()))
        else:
            return render_template('login.html', error='Invalided Username or Password')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'name' in session:
        name = session['name']
        return render_template('dashboard.html', name=name.capitalize())
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop("name", None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)