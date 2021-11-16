import requests
from bs4 import BeautifulSoup as bs
import datetime


def get_data() -> dict:
    '''
    Sends a GET request to https://www.hdsb.ca/students/Pages/Health%20and%20Well-Being/COVID-19/COVID-19-Advisory.aspx

    Returns dict of dicts of school data

    ```
    {
        school_name: {
            'confirmed_staff_cases': confirmed_staff_cases,
            'confirmed_student_cases': confirmed_student_cases,
            'total_closed_classes': total_closed_classes,
            'school_closed': school_closed
        }
    }
    ```
    '''
    response = requests.get('https://www.hdsb.ca/students/Pages/Health%20and%20Well-Being/COVID-19/COVID-19-Advisory.aspx')
    soup = bs(response.text, 'html.parser')
    table = soup.find(id='{EF428635-D71E-4F05-9482-A50B7F76241F}-{B2977EDA-1EC3-42C9-987D-AE9A62620C3B}')

    return (_parse_data(table), str(datetime.date.today()))

def _parse_data(table) -> dict:
    '''
    Parses the data that is received in `get_data()`

    Gets all data, and creates instances of `School` class, which is appended to list `schools`

    Returns dict of dicts of school data
    '''

    schools = dict()

    # Each row is a school
    for row in table:
        if row.name == 'thead':
            continue

        column_num = 0

        for column in row:
            column_num += 1

            if column_num == 2:
                school_name = column.get_text()

            elif column_num == 3:
                confirmed_staff_cases = int(column.get_text())

            elif column_num == 4:
                confirmed_student_cases = int(column.get_text())

            elif column_num == 5:
                total_closed_classes = int(column.get_text())

            elif column_num == 6:
                school_closed = column.get_text().strip() != 'No'
            
        schools[school_name] = {
            'confirmed_staff_cases': confirmed_staff_cases,
            'confirmed_student_cases': confirmed_student_cases,
            'total_closed_classes': total_closed_classes,
            'school_closed': school_closed
        }

    return schools