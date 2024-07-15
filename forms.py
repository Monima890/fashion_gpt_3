from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class FashionForm(FlaskForm):
    body_type = SelectField(
        'Body Type', 
        choices=[
            ('Rectangle/Straight', 'Rectangle/Straight'),
            ('Triangle/Pear', 'Triangle/Pear'),
            ('Spoon', 'Spoon'),
            ('Hourglass', 'Hourglass'),
            ('Top hourglass', 'Top hourglass'),
            ('Bottom hourglass', 'Bottom hourglass'),
            ('Inverted triangle/Apple', 'Inverted triangle/Apple'),
            ('Round/Oval', 'Round/Oval'),
            ('Diamond', 'Diamond'),
            ('Athletic', 'Athletic')
        ],
        validators=[DataRequired()]
    )
    preference = StringField('Preference')
    occasion = StringField('Occasion')
