from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(open('aukokime_vaikams.html').read())

@app.route('/donate', methods=['POST'])
def donate():
    name = request.form['name']
    email = request.form['email']
    amount = request.form['amount']
    message = request.form['message']
    
    # Here you would typically save the data to a database or process the donation
    print(f"Received donation from {name} ({email}) of {amount}€ with message: {message}")
    
    return f"Thank you, {name}, for your donation of {amount}€!"

if __name__ == '__main__':
    app.run(debug=True)
