from flask import Flask, render_template, send_from_directory, url_for
import os

app = Flask(__name__)
# app.add_url_rule('/favicon.ico',
#   redirect_to=url_for('static', filename='favicon.ico'))

@app.route("/")
def index():
  return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'),
    'favicon.ico',
    mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(host = '0.0.0.0', port=port)

