from flask import Blueprint, render_template, request

bp = Blueprint('bp', __name__, '/')


@bp.route('/', methods=('GET', 'POST'))
@bp.route('/encrypt', methods=('GET', 'POST'))
def encrypt():
    if request.method == 'POST':
        text = request.form.get('textbox')

        return render_template('encrypt.html', view=True, encryptedText=text)

    return render_template('encrypt.html', view=False)


@bp.route('/decrypt', methods=('GET', 'POST'))
def decrypt():
    if request.method == 'POST':
        text = request.form.get('textbox')

        return render_template('decrypt.html', view=True, decryptedText=text)

    return render_template('decrypt.html')
