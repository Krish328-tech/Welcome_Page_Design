from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        mobile = request.form['mobile']
        dob = request.form['dob']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        # Password validation
        password_match = password == confirm_password

        if not password_match:
            return render_template('index.html', message="Passwords do not match!")

        # Further processing or database storage can be done here
        # For now, just returning a success message
        return render_template('index.html', message="Registration successful!")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
