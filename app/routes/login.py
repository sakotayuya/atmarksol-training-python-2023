from flask import flash, url_for, Blueprint
from flask import render_template, request, redirect
from flask_login import login_user, logout_user, login_required
from models.users import Users

login_blueprint = Blueprint('login', __name__)

# ログイン
@login_blueprint.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		request_email = request.form.get('email')
		request_password = request.form.get('password')

		fetched_user = Users.query.filter_by(email=request_email).first()

		# 条件に応じてエラーメッセージ変更
		if fetched_user and fetched_user.password == request_password:
			if fetched_user.status == 'enable' and fetched_user.deleted is not True:
				login_user(fetched_user)
				return redirect(url_for('user.user_list'))
			else:
				flash('削除済みユーザか無効なユーザです', 'error')
		else:
			flash('ログインに失敗しました。メールアドレスとパスワードを確認してください', 'error')

	return render_template('login.html')

# ログアウト
@login_blueprint.route('/logout')
@login_required
def logout():
	logout_user()
	flash('ログアウトしました', 'success')
	return redirect(url_for('login.login'))