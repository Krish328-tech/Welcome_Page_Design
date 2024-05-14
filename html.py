from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')  # Assuming your HTML form is in form.html

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    country_code = request.form['Country code']
    mobile_number = request.form['mobile_number']
    dob = request.form['dob']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']

    # Process the fetched information as needed (printing here for demonstration)
    print(f"Username: {username}")
    print(f"Country Code: {country_code}")
    print(f"Mobile Number: {mobile_number}")
    print(f"Date of Birth: {dob}")
    print(f"Password: {password}")
    print(f"Confirm Password: {confirm_password}")

    # You can return a response or redirect to another page after processing the data
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
