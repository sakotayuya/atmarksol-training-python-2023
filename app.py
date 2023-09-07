from flask import Flask, flash, url_for
from flask import render_template, request, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_login.mixins import AnonymousUserMixin
from config import Config
from models import db, Users

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
 
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  return Users.query.get(int(user_id))
 
# ログイン
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')

		user = Users.query.filter_by(email=email).first()

		# 条件に応じてエラーメッセージ変更
		if user and user.password == password:
			if user.status == 'enable' and user.deleted is not True:
				login_user(user)
				return redirect(url_for('user_list'))
			else:
				flash('削除済みユーザか無効なユーザです', 'error')
		else:
			flash('ログインに失敗しました。メールアドレスとパスワードを確認してください', 'error')

	return render_template('login.html')

# ログアウト
@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('ログアウトしました', 'success')
	return render_template('login.html')

# ユーザ登録
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        user = Users.query.filter_by(email=email).first()
        
		# POST時にフォームからのリクエスト値を取得してDBに登録
        if user is None:
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            password = request.form.get('password')
            status = request.form.get('status')
            deleted = request.form.get('deleted') == '1'

            regist_use = Users(first_name=first_name, last_name=last_name, email=email, password=password, status=status, deleted=deleted)
            
            db.session.add(regist_use)
            db.session.commit()

            flash('登録が完了しました', 'success')
            destination = 'user_list' if not isinstance(current_user, AnonymousUserMixin) else 'login'
        else:
			# 入力したメールアドレスのユーザが既に登録されてる場合はエラーメッセージを表示
            flash('既に登録されているメールアドレスです', 'error')
            destination = 'register'
        
        return redirect(url_for(destination))

    if not isinstance(current_user, AnonymousUserMixin):
        return render_template('logined_register.html', current_user=current_user)
    
    return render_template('register.html')

# ユーザ一覧
@app.route('/user_list')
@login_required
def user_list():
	user_list = Users.query.filter_by(deleted=False)
	return render_template('user_list.html', user_list=user_list, current_user=current_user)

# 削除
@app.route('/delete/<int:user_id>')
@login_required
def delete(user_id):
	user = Users.query.get(user_id)

	user.deleted = True
	
	db.session.commit()

	# もし、ログインユーザが削除で編集された場合はログアウトして、ログイン画面へ
	if user == current_user:
		logout_user()
		flash('ログインユーザーが削除された為、<br>ログアウトしました', 'success')
		return redirect(url_for('login'))
	else:
		flash('選択ユーザーを削除しました', 'success')
		return redirect(url_for('user_list'))

# ユーザ詳細
@app.route('/user_detail/<int:user_id>')
@login_required
def user_detail(user_id):
	user = Users.query.get(user_id)
	return render_template('user_detail.html', user=user, current_user=current_user)

#ユーザ編集
@app.route('/user_edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_edit(user_id):
	user = Users.query.get(user_id)

	if request.method == 'POST':
		# POST時にフォームからのリクエスト値を取得し、更新
		user.first_name = request.form.get('first_name')
		user.last_name = request.form.get('last_name')
		user.password = request.form.get('password') or user.password
		user.status = request.form.get('status')
		user.deleted = True if request.form.get('deleted') == '1' else False if request.form.get('deleted') == '0' else False
	
		db.session.commit()

		# もし、ログインユーザが削除で編集された場合はログアウトして、ログイン画面へ
		if user == current_user and request.form.get('deleted') == '1':
			logout_user()
			flash('ログインユーザーが削除された為、<br>ログアウトしました', 'success')
			return redirect(url_for('login'))
		else:
			flash('更新処理が完了しました', 'success')
			return redirect(url_for('user_list'))
	return render_template('user_edit.html', user=user, current_user=current_user)

# エラーハンドリング
@login_manager.unauthorized_handler
def unauthorized():
    flash('ログインが必要なページです。<br>ログインしてください。', 'error')
    return redirect(url_for('login'))

@app.errorhandler(500)
def internal_server_error(e):
    flash('500 Internal Server Error', 'error')
    return redirect(url_for('login'))

@app.errorhandler(404)
def internal_server_error(e):
    flash('ページが見つかりません', 'error')
    return redirect(url_for('login'))
