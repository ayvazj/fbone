# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import HiddenField, SubmitField, RadioField, DateField, SelectMultipleField
from wtforms.validators import AnyOf

from ..user import USER_STATUS


class UserForm(Form):
    next = HiddenField()
    role_code_select = SelectMultipleField(u"Role", choices=[])
    status_code = RadioField(u"Status", [AnyOf([str(val) for val in USER_STATUS.keys()])],
            choices=[(str(val), label) for val, label in USER_STATUS.items()])
    # A demo of datepicker.
    created_time = DateField(u'Created time')
    submit = SubmitField(u'Save')
