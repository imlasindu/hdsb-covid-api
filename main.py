from flask import Flask, redirect, request, jsonify
import threading
import time
from get_data import get_data
import database


app = Flask(__name__)


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

    received_data = get_data()

    if schools:
        for school_name, data in received_data[0].items():
            if school_name in schools:
                all_data[school_name] = data
    else:
        all_data = received_data[0]
        date = received_data[1]
        threading.Thread(target=lambda: database.insert_into_db(date, all_data)).start()

    return jsonify(all_data), 200, {"Access-Control-Allow-Origin": "*"}

@app.route('/api/get-all-data/')
def api_get_all_data():
    '''Gets all data over time, or on specific date'''
    date = request.args.get('date')

    if date:
        try:
            
            return jsonify({date: dict(database.find_from_db(date))['data']}), 200, {"Access-Control-Allow-Origin": "*"}
        except:
            # If no data
            return {date: {}}
    else:
        all_data = dict()
        received_data = database.find_from_db()

        for i in received_data:
            date = i['date']
            del i['_id'], i['date']
            all_data[date] = i['data']

        return jsonify(all_data), 200, {"Access-Control-Allow-Origin": "*"}



@app.route('/api/get-schools/')
def api_get_schools():
    '''Gets all school names'''
    schools = list()

    for school_name in get_data()[0].keys():
        schools.append(school_name)
    
    return jsonify(schools), 200, {"Access-Control-Allow-Origin": "*"}


def main():
    app.run()

if __name__ == '__main__':
    main()
