# import Flask module
from flask import Flask, render_template
from flask import request

# create Flask app instance
app = Flask(__name__, template_folder='views')
# define route for the root URL
@app.route('/')
def hello_world():
    title = "Home Page"
    return render_template('index.html', title=title)
# define route for a template rendering
@app.route('/about')
def about():
    title = "About Page"
    return render_template('about.html', title=title)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        #Proses data form di sini 
        nama = request.form['nama']
        email = request.form['email']
        pesan = request.form['pesan']

        #Tampilan pada terminal
        print(f"Nama: {nama}, Email: {email}, Pesan: {pesan}")

    title = "Contact Page"
    return render_template('contact.html', title=title)

@app.route('/pmb')
def pmb():
    title = "Penerimaan Mahasiswa Baru"
    return render_template('pmb.html', title=title)
# run the app
if __name__ == '__main__':
    app.run(debug=True)