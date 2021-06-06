from flask import Blueprint, render_template, request
from cryptography.fernet import Fernet

bp = Blueprint('bp', __name__, '/')


@bp.route('/', methods=('GET', 'POST'))
@bp.route('/encrypt', methods=('GET', 'POST'))
def encrypt():
    if request.method == 'POST':
        text = request.form.get('textbox')
        key = Fernet.generate_key()

        obj = Fernet(key)
        encryptedText = obj.encrypt(text.encode()).decode()

        return render_template('encrypt.html', view=True, encryptedText=encryptedText, key=key.decode())

    return render_template('encrypt.html', view=False)


@bp.route('/decrypt', methods=('GET', 'POST'))
def decrypt():
    if request.method == 'POST':
        text = request.form.get('textbox')
        key = request.form.get('key').encode()

        obj = Fernet(key)
        decryptedText = obj.decrypt(text.encode()).decode()

        return render_template('decrypt.html', view=True, decryptedText=decryptedText)

    return render_template('decrypt.html')
