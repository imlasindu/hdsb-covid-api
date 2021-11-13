from flask import Flask, json, render_template, redirect, url_for, request, session, flash, jsonify
# import os
from get_data import get_data


app = Flask(__name__)
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


# Documentation
@app.route('/docs/')
@app.route('/')
def docs():
    return redirect('https://github.com/jasonli0616/hdsb-covid-api/tree/main/docs')


# API

@app.route('/api/get-data/')
def api_get_data():
    '''
    Gets COVID-19 data of schools

    Query parameters:
    - School: name of school(s)
    '''
    schools = request.args.getlist('school')

    all_data = dict()

    if schools:
        for school_name, data in get_data().items():
            if school_name in schools:
                all_data[school_name] = data
    else:
        all_data = get_data()


    return jsonify(all_data), 200, {"Access-Control-Allow-Origin": "*"}


@app.route('/api/get-schools/')
def api_get_schools():
    '''Gets all school names'''
    schools = list()

    for school_name in get_data().keys():
        schools.append(school_name)
    
    return jsonify(schools), 200, {"Access-Control-Allow-Origin": "*"}


def main():
    app.run()

if __name__ == '__main__':
    main()
