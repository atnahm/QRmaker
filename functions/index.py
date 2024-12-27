from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_img = None
    error_message = None

    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            try:
                # Generate QR code
                qr_img = qrcode.make(url)
                img_io = BytesIO()
                qr_img.save(img_io, 'PNG')
                img_io.seek(0)
                qr_code_img = base64.b64encode(img_io.getvalue()).decode('utf-8')
            except Exception as e:
                error_message = "There was an error generating the QR Code. Please try again."
        else:
            error_message = "Please enter a valid URL."

    return render_template('QRIndex.html', qr_code_img=qr_code_img, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
