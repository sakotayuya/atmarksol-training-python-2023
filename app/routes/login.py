from flask import flash, url_for, Blueprint
from flask import render_template, request, redirect
from flask_login import login_user, logout_user, login_required
from models.users import Users

login_blueprint = Blueprint('login', __name__)

# ログイン
@login_blueprint.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')

		user = Users.query.filter_by(email=email).first()

		# 条件に応じてエラーメッセージ変更
		if user and user.password == password:
			if user.status == 'enable' and user.deleted is not True:
				login_user(user)
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
	return render_template('login.html')