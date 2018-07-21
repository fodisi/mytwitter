# /usr/bin/env python3

from flask import Blueprint, request, render_template, \
    session, redirect, url_for

from .. import db
from ..auth.user_model import User, UserSchema
from ..twit.twit_model import Twit, TwitSchema

timeline_ctrl = Blueprint('timeline', __name__)


@timeline_ctrl.route('/home/', methods=['GET', 'POST'])
def home() -> None:
    if request.method == 'GET':
        json_user, json_twits = None, None
        try:
            user = User.query.filter_by(id_=session['user_id']).first()
            twits = Twit.query.filter_by().order_by(Twit.date_modified.desc()).all()
            json_twits = TwitSchema().dump(twits, many=True).data
            json_user = UserSchema().dump(user).data
            return render_template("timeline/home.html", user=json_user, twits=json_twits)
        except Exception as e:
            return render_template("timeline/home.html", user=json_user, error=e.args[0])
    else:
        try:
            db.session.add(Twit(session['user_id'], request.form['message']))
            db.session.commit()
            return redirect(url_for('timeline.home'))
        except Exception as e:
            return render_template("timeline/home.html", user=json_user, error=e.args[0])


@timeline_ctrl.route('/user/', methods=['GET'])
def user_twits() -> None:
    json_user, json_twits = None, None
    try:
        user = User.query.filter_by(id_=session['user_id']).first()
        twits = Twit.query.filter_by(user_id=session['user_id']).all()
        json_twits = TwitSchema().dump(twits, many=True).data
        json_user = UserSchema().dump(user).data

        return render_template("timeline/user_twits.html", user=json_user, twits=json_twits)
    except Exception as e:
        return render_template("timeline/user_twits.html", user=json_user, error=e.args[0])
