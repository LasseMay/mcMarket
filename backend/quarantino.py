from flask import Flask, render_template, request
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# helper is the external plattform helper
#class helper(Resource):

# telephone helper is called user
#class user(Resource):

parser = reqparse.RequestParser()
parser.add_argument('id')

#job related
class job_list(Resource):
    def get(self):
        #query: get all jobs for user id
        return {'all':'jobs'},200

# single job (defined by its id)
class job(Resource):
    def get(self,job_id):
        #query db and return job dict
        desc="description for job"+str(job_id)
        title="testTitle"
        helper_ids=["helper id 1 for job "+str(job_id),"helper id 2 for job "+str(job_id)]
        status="finished"
        return {'job':job_id, 'title':title, 'description': "description"+desc, "helper_ids":helper_ids, 'status':status},200

#customer related
class customer_job_list(Resource):
    def get(self,customer_id): 
        #return job list for user with id user_id
        return "list of jobs for customer"

    def post(self,customer_id):
        args = parser.parse_args()
        new_id = args["id"]
        return {'Added job with id':'success'}, 201   

class customer_job(Resource):
    def delete(self,customer_id,job_id):
        return "deleted job"

#user related ("callcenter"-worker)
class user_customer_list(Resource):
    def get(self,user_id):
        #get a list of all customers assigned to a user
        return {"list of ": "all customer ids assigned to userID "+str(user_id)}

    def post(self,user_id):
        args = parser.parse_args()
        new_id = args["id"]
        return {"Added customer with id "+str(new_id)+"to user with id"+str(user_id):"success"}, 201

#assign customer ids (omis) to user ids
class user_customer(Resource):    
    def delete(self,user_id,customer_id):
        #delete customer id from user ids list 
        return "deleted"

api.add_resource(HelloWorld, '/api')

#job related 
api.add_resource(job_list, '/api/job')                                                      #GET list of all jobs
api.add_resource(job, '/api/job/<job_id>')                                                  #GET PUT POST DELETE details of job with id <job_id>

#customer (omi) related 
api.add_resource(customer_job_list, '/api/customer/<customer_id>/jobs')                         # GET customr job ids
api.add_resource(customer_job, '/api/customer/<customer_id>/job/<job_id>')                      # PUT POST and DELETE for customer job ids

#user (callcenter worker) related
api.add_resource(user_customer_list, '/api/user/<user_id>/customers')                        # GET all customers that are "managed" by the user or POST a new id
api.add_resource(user_customer,      '/api/user/<user_id>/customers/<customer_id>')          # DELETE the assignment of customer_id to user_id

context = {
    "logged_in": False,
    "pages": {
        "/about": "About",
        "/partners": "Partner",
        "/profile": "Profil",
        "/placement": "Vermittelung",
    },
    "active_page": None
}

@app.route('/')
@app.route('/index')
def index():
    context["active_page"] = request.path
    return render_template("index.html", context=context)

@app.route('/about')
def about():
    context["active_page"] = request.path
    return render_template("about.html", context=context)

@app.route('/login')
def login():
    context["active_page"] = request.path
    return render_template("login.html", context=context)

@app.route('/register')
def register():
    context["active_page"] = request.path
    return render_template("register.html", context=context)

@app.route('/partners')
def partners():
    context["active_page"] = request.path
    return render_template("partners.html", context=context)

@app.route('/placement')
def placement():
    context["active_page"] = request.path
    return render_template("placement.html", context=context)

@app.route('/profile')
def profile():
    context["active_page"] = request.path
    return render_template("profile.html", context=context)

if __name__ == '__main__':
    app.run(debug=True)
