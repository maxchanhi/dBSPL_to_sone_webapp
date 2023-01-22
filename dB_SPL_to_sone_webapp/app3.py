from flask import Flask, render_template, request
from disscal import SPL_to_sone

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def convert_SPL_to_loudness():
    sone = ''
    if request.method == 'POST':
        dB_SPL = float(request.form.get('dB_SPL'))
        Frequency = float(request.form.get('Frequency'))
        sone = SPL_to_sone(Frequency,dB_SPL)
    return render_template('runcode.html', sone = sone)

if __name__ == '__main__':
    app.run(debug=True)


