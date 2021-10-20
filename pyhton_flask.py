import os

from flask import Flask
from flask import request
from flask_restful import Api, Resource, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://tmp:asdzxc123456@106.52.42.50/tmp?charset=utf8mb4"
db = SQLAlchemy(app)
#app.config["testcase"] = []
ALLOWED_EXTENSIONS = {'zip', 'png',"py"}

class TestCase(db.Model):
    # __tablename__ = "testcase"
    name = db.Column(db.String(80), primary_key=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    filename = db.Column(db.String(80), unique=False, nullable=True)
    content = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return '<test_case %r>' % self.name

class TestCaseServer(Resource):

    def get(self):
        if "id" in request.args:
            for i in app.config["testcase"]:
                if i["id"]==int(request.args["id"]):
                    return i
        else:
            return app.config["testcase"]


    def post(self):
        def allowed_file(filename):
            return '.' in filename and \
                filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


        if "file" in request.files and "name" in request.form:
            f = request.files["file"]
            file_name = f.filename
            name = request.form["name"]
            content = f.read()
            case = TestCase(name=name,filename=allowed_file(file_name),content=content)
            db.session.add(case)
            db.session.commit()

            # f.save(os.path.join("./",allowed_file(file_name)))
            return 'ok'
        abort(404)

@app.route("/get_testcase",methods=['get'])
def get_testcase():
    testcase = TestCase.query.filter_by(name='tmp1').first()
    # print(type(testcase.content))
    return testcase.content


        # if "id" not in request.json:
        #     return {"result":"error","errcode":"404","errmessage":"need testcase id"}
        # app.config["testcase"].append(request.json)
        #
        # return {"result":"ok","errcode":"0"}

api.add_resource(TestCaseServer, '/testcase')
# api.add_resource(Testcaserun, '/run')


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    app.run(debug=True,host="0.0.0.0")