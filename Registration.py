from flask import Flask, render_template, request

app = Flask(__name__)

def save_to_file(data):
    with open('form_data.txt', 'a') as file:
        file.write(data + '\n')

@app.route('/submit', methods=['POST'])
def submit_form():
    username = request.form['username']
    mobile = request.form['mobile']
    dob = request.form['dob']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']

    if password == confirm_password:
        data_to_save = f"Username: {username}, Mobile: {mobile}, DOB: {dob}"
        save_to_file(data_to_save)
        return "Thank you for registering!"
    else:
        return "Passwords do not match. Please enter the same passwords."

if __name__ == '__main__':
    app.run(debug=True)

