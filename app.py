from flask import Flask, render_template, request
from translator import initialize_model_and_tokenizer, batch_translate
from IndicTransToolkit import IndicProcessor

app = Flask(__name__)

# Load model at startup
ckpt_dir = "ai4bharat/indictrans2-en-indic-1B"
quantization = None
tokenizer, model = initialize_model_and_tokenizer(ckpt_dir, quantization)
ip = IndicProcessor(inference=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    input_text = ""
    tgt_lang = "hin_Deva"

    if request.method == 'POST':
        input_text = request.form['input-text']
        # src_lang = request.form['from-lang']
        src_lang = "eng_Latn"
        tgt_lang = request.form['to-lang']
        translated = batch_translate([input_text], src_lang, tgt_lang, model, tokenizer, ip)
        translation = translated[0]

    return render_template('index.html', translation=translation, input_text=input_text, tgt_lang=tgt_lang)

if __name__ == '__main__':
    app.run(debug=True)
