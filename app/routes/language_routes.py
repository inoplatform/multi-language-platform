from flask import session, redirect, url_for, request, render_template
from app.routes import language_bp
from flask_babel import refresh

@language_bp.route('/set/<language>')
def set_language(language):
    session['language'] = language
    refresh()
    return redirect(request.referrer or url_for('main.index'))

@language_bp.route('/select')
def select_language():
    return render_template('language/select.html')
