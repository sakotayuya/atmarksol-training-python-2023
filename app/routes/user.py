from flask import flash, url_for, Blueprint
from flask import render_template, request, redirect
from flask_login import logout_user, login_required, current_user
from flask_login.mixins import AnonymousUserMixin
from models.users import db, Users
from validators import is_valid_regist, is_valid_edit

user_blueprint = Blueprint('user', __name__)

# ユーザ詳細
@user_blueprint.route('/user_detail/<int:user_id>')
@login_required
def user_detail(user_id):
    fetched_user = Users.query.get(user_id)
    return render_template('user_detail.html', user=fetched_user, current_user=current_user)

#ユーザ編集
@user_blueprint.route('/user_edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_edit(user_id):
    fetched_user = Users.query.get(user_id)

    if request.method == 'POST':
        request_first_name = request.form.get('first_name')
        request_last_name = request.form.get('last_name')
        request_email = request.form.get('email')
        request_password = request.form.get('password')
		
        if not is_valid_edit(request_first_name, request_last_name, request_email, request_password):
            return render_template('user_edit.html', user=fetched_user, current_user=current_user)
        
		# POST時にフォームからのリクエスト値を取得し、更新
        fetched_user.first_name = request_first_name
        fetched_user.last_name = request_last_name
        fetched_user.password = request_password or fetched_user.password
        fetched_user.email = request_email
        fetched_user.status = request.form.get('status')
        fetched_user.deleted = True if request.form.get('deleted') == '1' else False
	
        db.session.commit()
        
		# もし、ログインユーザが削除で編集された場合はログアウトして、ログイン画面へ
        if fetched_user == current_user and request.form.get('deleted') == '1':
            logout_user()
            flash('ログインユーザーが削除された為、<br>ログアウトしました', 'success')
            return redirect(url_for('login.login'))
        else:
            flash('更新処理が完了しました', 'success')
            return redirect(url_for('user.user_list'))
    return render_template('user_edit.html', user=fetched_user, current_user=current_user)

# ユーザ一覧
@user_blueprint.route('/user_list')
@login_required
def user_list():
	fetched_user_list = Users.query.filter_by(deleted=False)
	return render_template('user_list.html', user_list=fetched_user_list, current_user=current_user)

# ユーザ登録
@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        request_first_name = request.form.get('first_name')
        request_last_name = request.form.get('last_name')
        request_email = request.form.get('email')
        request_password = request.form.get('password')
		
        if not is_valid_regist(request_first_name, request_last_name, request_email, request_password):
            if not isinstance(current_user, AnonymousUserMixin):
                return render_template('logined_register.html', current_user=current_user)
            return render_template('register.html')
	
        fetched_user = Users.query.filter_by(email=request_email).first()
		
        is_valid_regist
		# POST時にフォームからのリクエスト値を取得してDBに登録
        if fetched_user is None:
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
	fetched_user = Users.query.get(user_id)

	fetched_user.deleted = True
	
	db.session.commit()

	# もし、ログインユーザが削除で編集された場合はログアウトして、ログイン画面へ
	if fetched_user == current_user:
		logout_user()
		flash('ログインユーザーが削除された為、<br>ログアウトしました', 'success')
		return redirect(url_for('login.login'))
	else:
		flash('選択ユーザーを削除しました', 'success')
		return redirect(url_for('user.user_list'))