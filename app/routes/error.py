from flask import Blueprint, redirect, url_for, flash

error_blueprint = Blueprint('error', __name__)

# エラーハンドリング
@error_blueprint.errorhandler(500)
def internal_server_error(e):
    flash('500 Internal Server Error', 'error')
    return redirect(url_for('login.login'))

@error_blueprint.errorhandler(404)
def internal_server_error(e):
    flash('ページが見つかりません', 'error')
    return redirect(url_for('login.login'))