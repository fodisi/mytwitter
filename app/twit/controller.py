# Import flask dependencies
from flask import Blueprint, request, render_template, session, redirect, url_for

from .. import db
from ..twit.twit_model import Twit
from ..auth.user_model import User

twit_ctrl = Blueprint('twit', __name__)

# Set the route and accepted methods


# @twit_ctrl.route('/twit/', methods=['POST'])
# def twit(message) -> None:
#     try:
#         request.form['']
#         new_twit = Twit(session['user_id'], message)
#         new_twit.retwit_from = original_twit.id_
#         new_twit.picture = original_twit.picture

#         db.session.add(new_twit)
#         db.session.commit()

#         return redirect(url_for('timeline.home'))

#     except Exception as e:
#         pass
#         # TODO: flash errors


@twit_ctrl.route('/twit/<int:twit_id>/', methods=['POST'])
def retwit(twit_id: int) -> None:
    try:
        original_twit = Twit.query.filter_by(id_=twit_id).first()
        new_twit = Twit(session['user_id'], original_twit.message)
        new_twit.retwit_from = original_twit.id_
        new_twit.picture = original_twit.picture

        db.session.add(new_twit)
        db.session.commit()

        return redirect(url_for('timeline.home'))

    except Exception as e:
        pass
        # TODO: flash errors

        # err.messages  # => {'email': ['"foo" is not a valid email address.']}
        # valid_data = err.valid_data  # => {'name': 'John'}

    # return redirect(url_for('timeline.home'))

        #     <button class="btn btn-lg btn-primary btn-block" type="submit">Twit</button>
        # <a href="{{ url_for( 'twit.retwit', twit_id=item['id_']) }}">Retwit</a>
