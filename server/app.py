#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, render_template, send_file
from flask_restful import Resource

# Local imports
from config import app, db, api
import os
import generator 
# Add your model imports




@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

# Views go here! use either route!
# @app.errorhandler(404)
# def not_found(e):
#     return render_template("index.html")

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template("index.html")





class InfoPackage(Resource):
    def post(self):
        data = request.get_json()
        
        template_path = './template/template.png'
        output_pdf_path = './template/cert.pdf'
        
        birthdate_text = data['birthdate']
        name_text = data['name']
        breed_text = data['breed']
        gender_text = data['gender']
        parent_text = data['parent']

        if os.path.exists(output_pdf_path):
            os.remove(output_pdf_path)

        generator.create_certificate(
            template_path=template_path,
            output_pdf_path=output_pdf_path,
            birthdate_text=birthdate_text, 
            name_text=name_text, 
            breed_text=breed_text, 
            gender_text=gender_text, 
            parent_text=parent_text
        )
        
        # Assuming you want to return a confirmation or result

        return {'message': 'Certificate created successfully'}, 200
    

api.add_resource(InfoPackage, '/infopackage')



class SendCert(Resource):
    def get(self):
        output_pdf = './template/cert.pdf'
        try:
            return send_file(output_pdf)
        except Exception as e:
            return {'error': str(e)}, 500

api.add_resource(SendCert, '/cert')






if __name__ == '__main__':
    app.run(port=5555, debug=True)

