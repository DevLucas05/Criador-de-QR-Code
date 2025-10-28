from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import qrcode
import io

app = Flask(__name__)
CORS(app)


@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json

    content = data.get('content', '')
    fill_color = data.get('fill_color', '#000000')
    back_color = data.get('back_color', '#FFFFFF')
    size = int(data.get('size', 256))

    if not content: 
        return jsonify({'error': 'Content is required'}), 400
    
    qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_H,
        box_size=10, 
        border = 4,
    )

    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    img = img.resize((size, size)) # Redimensionar a imagem.

    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    return send_file(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

