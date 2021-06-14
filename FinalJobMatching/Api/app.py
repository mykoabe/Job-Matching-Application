from flask import Flask,render_template, url_for, flash, redirect, request, jsonify
from flask_marshmallow import Marshmallow
from flask_restplus import Resource,Api,fields
# from dotenv import load_dotenv
from settings import *
from models import *
from datetime import date
from marsh import *
from flask_cors import CORS
# this is for the login form
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
# this is for the login form key
app.config['JWT_SECRET_KEY'] = "What is the best secure password"
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
db.init_app(app) # initialize

marsh = Marshmallow(app)


job_schema = JobSchema()

jobs_schema = JobSchema(many=True)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
employer_schema = EmployerSchema()
employers_schema = EmployerSchema(many=True)
#fields for models for swagger used for documentation only
api = Api(app,version="1",title="Job matching Database",description="This is Job matching database")
jwt = JWTManager(app)
#for job model
job = api.model("Job", {
    'name':fields.String(),
    'posted_date':fields.DateTime(),
    'posted_by':fields.String(),
    'category':fields.String(),
    'location':fields.String(),
    'career_level':fields.String(),
    'employment_type':fields.String(),
    'description':fields.String,
    'job_requirements':fields.String(),
})
#for employee model

employee = api.model("Employee",{
    'username':fields.String("Employee name"),
    'email':fields.String("Email"),
    'password':fields.String("password")
})
#for employer model

employer = api.model("Employer",{
    'username':fields.String("Employee name"),
    'email':fields.String("Email"),
    'password':fields.String("password"),
    'address':fields.String("address")
})

#crud operations for jobs start
@api.route("/api/jobs",methods=["GET","POST"])
# @jwt_required()
class JobResource(Resource):
    def get(self):
        """This request returns all jobs"""
        jobs = Job.query.all()
        return jobs_schema.dump(jobs)
    @api.expect(job)
    @api.response(201,"Successfuly created new job!")
    def post(self):
        """This request creates new job"""
        #create new job
        job = Job()
        job.name = request.json['name']
        job.posted_date = date.today()
        job.posted_by = request.json['posted_by']
        job.category = request.json['category']
        job.location = request.json['location']
        job.career_level = request.json['career_level']
        job.employment_type = request.json['employment_type']
        job.description = request.json['description']
        job.job_requirements = request.json['job_requirements']
        db.session.add(job)
        db.session.commit()
        return job_schema.dump(job)

@api.route('/api/jobs/<int:id>')
class JobResource(Resource):
    def get(self, id):
        '''
        This request return single job
        '''
        job = Job.query.filter_by(jobId=id).first()
        return job_schema.dump(job)
    @api.expect(job)
    @api.response(204, 'Job details successfully updated.')
    def put(self, id):
        """
        This request updates a particular job.
        """
        job = Job.query.filter_by(jobId=id).first()
        job.name = request.json['name']
        job.description = request.json['description']
        job.posted_date = request.json['posted_date']
        job.posted_by = request.json['posted_by']

        db.session.add(job)
        db.session.commit()

        return job_schema.dump(job)

    @api.response(204, 'Job  successfully deleted.')
    def delete(self, id):
        """
        This request deletes a particular job.
        """
        job = Job.query.filter_by(jobId=id).first()
        if job is None:
            return None, 404
        db.session.delete(job)
        db.session.commit()
        return None, 204
#crud operations for jobs end

#crud operations for employee start
@api.route("/api/employees")
class EmployeeResource(Resource):
    def get(self):
        "This request prints all employees"
        employee = Employee.query.all()
        return employees_schema.dump(employee)

    @api.expect(employee)
    @api.response(201,"Successfuly created new Employee!")
    def post(self):
        """This request creates new employee"""
        employee = Employee()
        email = request.json['email']
        test=Employee.query.filter_by(email=email).first()
        if test:
            return None, 404
        else: 
            employee.username = request.json['username']
            employee.email = request.json['email']
            employee.password = request.json['password']
            db.session.add(employee)
            db.session.commit()
            return employee_schema.dump(employee),201

#crud operations for employee start
@api.route("/api/loginEmployee")
class EmployeeResource(Resource):
    def get(self):
        "This request prints all employees"
        employee = Employee.query.all()
        return employees_schema.dump(employee)
    @api.expect(employee)
    @api.response(201,"Successfuly created new logedin!")
    def post(self):
        """This request creates new employee"""
        employee = Employee()
        if request.is_json:
            email = request.json['email']
            password = request.json['password']
        else:
            email = request.form['email']
            password = request.form['password']
        test=Employee.query.filter_by(email=email, password=password).first()
        if test:
            access_token = create_access_token(identity=email)
            return jsonify(message="login successful", access_token=access_token)
        else:
            return "Wrong email or password", 401 
        
#crud operations for employee start
@api.route("/api/loginEmployer")
class EmployeeResource(Resource):
    def get(self):
        # this is the redirection to after the employee is logedin
        employee = Employee.query.all()
        return employees_schema.dump(employee)
    @api.expect(employee)
    @api.response(201,"Successfuly created new logedin!")
    def post(self):
        # this is for submiting the form to check the tokens
        employee = Employee()
        if request.is_json:
            email = request.json['email']
            password = request.json['password']
        else:
            email = request.form['email']
            password = request.form['password']
        test=Employer.query.filter_by(email=email, password=password).first()
        if test:
            access_token = create_access_token(identity=email)
            return jsonify(message="login successful", access_token=access_token)
        else:
            return "Wrong email or password", 401 
@api.route("/api/employees/<int:id>")
class EmployeeResource(Resource):
    def get(self,id):
        "This request returns particular employee"
        employee=Employee.query.filter_by(employeeId=id).first()
        return employee_schema.dump(employee)
    @api.expect(employee)
    @api.response(204, 'Employee details successfully updated.')
    def put(self,id):
        "updates employee details"
        employee = Employee.query.filter_by(employeeId=id)
        employee.username = request.json['username']
        employee.email = request.json['email']
        employee.password = request.json['password']
        db.session.add(employee)
        db.session.commit()
        return employee_schema.dump(employee)
    @api.response(204, 'Employee  successfully deleted.')
    def delete(self,id):
        "deletes particular employee"
        employee = Employee.query.filter_by(employeeId=id)
        if employee is None:
            return None, 404
        db.session.delete(employee)
        db.session.commit()
        return None, 204

#crud operations for employee end


#crud operations for employer start
@api.route("/api/employers")
class EmployerResource(Resource):
    def get(self):
        "This request prints all employers"
        employer = Employer.query.all()
        return employers_schema.dump(employer)

    @api.expect(employer)
    @api.response(201,"Successfuly created new Employer!")
    def post(self):
        """This request creates new employer"""
        employer = Employer()
        email = request.json['email']
        test=Employer.query.filter_by(email=email).first()
        if test:
            return None, 404
        else:
            employer.username = request.json['username']
            employer.email = request.json['email']
            employer.password = request.json['password']
            employer.address = request.json['address']
            db.session.add(employer)
            db.session.commit()
            return employee_schema.dump(employer),201
@api.route("/api/employers/<int:id>")
class EmployerResource(Resource):
    def get(self,id):
        "This request returns particular employer"
        employer=Employer.query.filter_by(employerId=id).first()
        return employer_schema.dump(employer)
    @api.expect(employer)
    @api.response(204, 'Employer details successfully updated.')
    def put(self,id):
        "updates employer details"
        employer = Employer.query.filter_by(employerId=id)
        employer.name = request.json['name']
        employer.email = request.json['email']
        employer.company = request.json['company']
        employer.address = request.json['address']
        db.session.add(employer)
        db.session.commit()
        return employee_schema.dump(employer)
    def delete(self,id):
        "deletes particular employer"
        employer = Employer.query.filter_by(employerId=id).first()
        if employer is None:
            return "employer is not found",404
        db.session.delete(employer)
        db.session.commit()
        return "Employer  successfully deleted.",204
#crud operations for employer end

#search for jobs
@api.route("/api/jobs/<string:jobstring>")
class JobsResource(Resource):
    def get(self,jobstring):
        "This request returns employee interesed area jobs."
        job = Job.query.filter(Job.name.contains(jobstring)).all()
        return jobs_schema.dump(job),200







