from flask import flash
import re

def is_valid_regist(request_first_name, request_last_name, request_email, request_password):
    is_validate = common_validate(request_first_name, request_last_name, request_email, request_password)

    if not request_password or not (8 <= len(request_password) <= 30):
        is_validate = False
        flash('・パスワードは8文字以上30文字以下で必ず入力してください', 'error')
        
    return is_validate

def is_valid_edit(request_first_name, request_last_name, request_email, request_password):
    is_validate = common_validate(request_first_name, request_last_name, request_email, request_password)

    if request_password and not (8 <= len(request_password) <= 30):
        is_validate = False
        flash('・パスワードは8文字以上30文字以下で入力してください', 'error')
        
    return is_validate

def common_validate(request_first_name, request_last_name, request_email, request_password):
    is_validate = True
    password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&_/\\])[\w@$!%*?&_/\\]+$'

    if request_first_name and len(request_first_name) >= 20:
        is_validate = False
        flash('・ユーザ性は20文字以下で入力してください', 'error')

    if request_last_name and len(request_last_name) >= 20:
        is_validate = False
        flash('・ユーザ名は20文字以下で入力してください', 'error')

    if request_email and not ("@" in request_email and "." in request_email):
        is_validate = False
        flash('・メールアドレスは正しい形式で入力してください', 'error')

    if not request_email or len(request_email) >= 255:
        is_validate = False
        flash('・メールアドレスは255文字以下で必ず入力してください', 'error')

    if request_password and not re.match(password_pattern, request_password):
        is_validate = False
        flash('・パスワードには英数字と記号が少なくとも1つずつ含まれる必要があります', 'error')

    return is_validate



