# Import flask dependencies
import os
from flask import Blueprint, request, render_template, session, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db
from app.auth.user_model import User
from ..io.model import FileManager

authentication_ctrl = Blueprint('auth', __name__)


@authentication_ctrl.route('/', methods=['GET', 'POST'])
def signin() -> None:
    if request.method == 'GET':
        return render_template("auth/signin.html")
    else:
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id_
            # flash('Welcome %s' % user.name)
            return redirect(url_for('timeline.home'))
        else:
            return render_template("auth/signin.html", error=True)


@authentication_ctrl.route('/register', methods=['GET', 'POST'])
def register() -> None:
    if request.method == 'GET':
        return render_template("auth/register.html")
    else:
        try:
            user = User(
                request.form['email'],
                generate_password_hash(request.form['password']),
                request.form['firstName'],
                request.form['lastName'],
            )

            # check if the post request has the file part
            # uploaded_file = None
            # filename = None
            # if 'file' not in request.files:
            #     print('fileinrequest')
            #     file = request.files['image']
            #     if file:
            #         print(file.filename)
            #         file_ext = FileManager.get_file_extension(
            #             file.filename)
            #         print(file_ext)
            #         filename = FileManager.get_profile_filename(
            #             request.form['email'], file_ext)
            #         print(filename)
            #         FileManager.save_file(file, filename)
            #         print('filesaved')
            #         # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #           user.picture = filename

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('auth.signin'))
        except Exception as e:
            return render_template("auth/register.html", error=e.args[0])
            # pass


@authentication_ctrl.route('/logout', methods=['GET'])
def logout() -> None:
    session.pop('user_id', None)
    return redirect(url_for('auth.signin'))
