from flask import Flask
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

parser = reqparse.RequestParser()
parser.add_argument('id')

#user related ("callcenter"-worker)
class user_customer_list(Resource):
    def get(self,user_id):
        #get a list of all customers assigned to a user
        return {"list of ": "all customer ids assigned to userID "+str(user_id)}

    def post(self,user_id):
        args = parser.parse_args()
        new_id = args["id"]
        return {"Added id "+str(new_id)+"to user": "success"}, 201

#assign customer ids (omis) to user ids
class user_customer(Resource):    
    def delete(self,user_id,customer_id):
        return "deleted"

api.add_resource(HelloWorld, '/')

#job related 
api.add_resource(job_list, '/api/job')              #GET list of all jobs
api.add_resource(job, '/api/job/<job_id>')          #GET PUT POST DELETE details of job with id <job_id>

#customer (omi) related 
#api.add_resource(customer_job_list, '/customer/<customer_id>/jobs')       # GET customr job ids
#api.add_resource(customer_job, '/customer/<customer_id>/job/<job_id>')    # PUT POST and DELETE for customer job ids

#user (callcenter worker) related
api.add_resource(user_customer_list, '/api/user/<user_id>/customers')                        # GET all customers that are "managed" by the user or POST a new id
api.add_resource(user_customer,      '/api/user/<user_id>/customers/<customer_id>')          # DELETE the assignment of customer_id to user_id

if __name__ == '__main__':
    app.run(debug=True)