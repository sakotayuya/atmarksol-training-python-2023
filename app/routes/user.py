from flask import flash, url_for, Blueprint
from flask import render_template, request, redirect
from flask_login import logout_user, login_required, current_user
from flask_login.mixins import AnonymousUserMixin
from models.users import db, Users

user_blueprint = Blueprint('user', __name__)

# ユーザ詳細
@user_blueprint.route('/user_detail/<int:user_id>')
@login_required
def user_detail(user_id):
    user = Users.query.get(user_id)
    return render_template('user_detail.html', user=user, current_user=current_user)

#ユーザ編集
@user_blueprint.route('/user_edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_edit(user_id):
	user = Users.query.get(user_id)

	if request.method == 'POST':
	    # POST時にフォームからのリクエスト値を取得し、更新
		user.first_name = request.form.get('first_name')
		user.last_name = request.form.get('last_name')
		user.password = request.form.get('password') or user.password
		user.status = request.form.get('status')
		user.deleted = True if request.form.get('deleted') == '1' else False
	
		db.session.commit()

		# もし、ログインユーザが削除で編集された場合はログアウトして、ログイン画面へ
		if user == current_user and request.form.get('deleted') == '1':
			logout_user()
			flash('ログインユーザーが削除された為、<br>ログアウトしました', 'success')
			return redirect(url_for('login.login'))
		else:
			flash('更新処理が完了しました', 'success')
			return redirect(url_for('user.user_list'))
	return render_template('user_edit.html', user=user, current_user=current_user)

# ユーザ一覧
@user_blueprint.route('/user_list')
@login_required
def user_list():
	user_list = Users.query.filter_by(deleted=False)
	return render_template('user_list.html', user_list=user_list, current_user=current_user)

# ユーザ登録
@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        request_email = request.form.get('email')
        user = Users.query.filter_by(email=request_email).first()
        
		# POST時にフォームからのリクエスト値を取得してDBに登録
        if user is None:
            request_first_name = request.form.get('first_name')
            request_last_name = request.form.get('last_name')
            request_password = request.form.get('password')
            request_status = request.form.get('status')
            request_deleted = request.form.get('deleted') == '1'

            regist_use = Users(
				first_name=request_first_name, 
				last_name=request_last_name, 
				email=request_email, 
				password=request_password, 
				status=request_status, 
				deleted=request_deleted
			)
            
            db.session.add(regist_use)
            db.session.commit()

            flash('登録が完了しました', 'success')
            destination = 'user.user_list' if not isinstance(current_user, AnonymousUserMixin) else 'login.login'
        else:
			# 入力したメールアドレスのユーザが既に登録されてる場合はエラーメッセージを表示
            flash('既に登録されているメールアドレスです', 'error')
            destination = 'register'
        
        return redirect(url_for(destination))

    if not isinstance(current_user, AnonymousUserMixin):
        return render_template('logined_register.html', current_user=current_user)
    
    return render_template('register.html')

# ユーザ削除
@user_blueprint.route('/delete/<int:user_id>')
@login_required
def delete(user_id):
	user = Users.query.get(user_id)

	user.deleted = True
	
	db.session.commit()

	# もし、ログインユーザが削除で編集された場合はログアウトして、ログイン画面へ
	if user == current_user:
		logout_user()
		flash('ログインユーザーが削除された為、<br>ログアウトしました', 'success')
		return redirect(url_for('login.login'))
	else:
		flash('選択ユーザーを削除しました', 'success')
		return redirect(url_for('user.user_list'))