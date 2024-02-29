from flask import Flask, request, render_template, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Necessario per messaggi flash
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file_post():
   if request.method == 'POST':
      # Controlla se la richiesta POST ha il file parte
      if 'file' not in request.files:
          flash('Nessun file parte')
          return redirect(request.url)
      file = request.files['file']
      # Se l'utente non seleziona un file, il browser invia
      # un file senza nome.
      if file.filename == '':
          flash('Nessun file selezionato')
          return redirect(request.url)
      if file and allowed_file(file.filename):
          filename = secure_filename(file.filename)
          file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
          # Qui potresti processare il file inviato e ritornare i risultati
          return 'File caricato con successo'
      else:
          flash('Tipo di file non permesso')
          return redirect(request.url)

if __name__ == '__main__':
   app.run(debug=True)
