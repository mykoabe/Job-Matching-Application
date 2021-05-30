from flask_marshmallow import Marshmallow
from models import *

marsh = Marshmallow() 

class JobSchema(marsh.Schema):
    class Meta:
        fields=("name","description","posted_date","posted_by")
        model = Job 
        
class EmployeeSchema(marsh.Schema):
    class Meta:
        fields=("name","email","address")
        model = Employee 

class EmployerSchema(marsh.Schema):
    class Meta:
        fields=("name","email","company","address")
        model = Employer



