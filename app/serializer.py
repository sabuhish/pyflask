from flask_marshmallow import Marshmallow
from model.models import Contact

ma = Marshmallow()



class ModelSerializer(ma.ModelSchema):
    class Meta:

        model = Contact
       
