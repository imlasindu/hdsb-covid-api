# HDSB COVID API

This is an unofficial API for COVID-19 cases in the [HDSB](https://hdsb.ca).

The data is sourced from: https://www.hdsb.ca/students/Pages/Health%20and%20Well-Being/COVID-19/COVID-19-Advisory.aspx

### Documentation Table of Contents:
- [Privacy](#Privacy)
- [Getting Started](#getting-started)
- [API Reference](#api-reference)
  - [`/api/get-data/`](#apiget-data)
  - [`/api/get-schools/`](#apiget-schools)



## Privacy

The public availability of this data, and usability of this API complies with the [Information and Privacy Commissioner of Ontario](https://www.ipc.on.ca).
```
Privacy does not prevent the release of data related to COVID-19 infections and deaths in Ontario.

Public health offices, long-term care facilities, hospitals, and other organizations can release non-identifying information, especially in situations where the information is related to incidences of infection, numbers of deaths, or other information that can help control spread of the virus and keep the public safe. This vital information should be shared with the public as soon as it is possible to do so.

Non-identifying information could include the numbers of affected individuals, demographic data such as gender and approximate age of affected individuals, as well as geographic locations of infected or deceased individuals, including long-term care facilities and workplaces, especially if they are in a location where large numbers of people might have gathered. However, public health bodies and governments should only share as much information as is necessary for public health purposes. They don’t need to name the individual.

People need to be told if they have been exposed to the virus so they can take steps to self-isolate or otherwise protect themselves and their families, as well as assess the public health response. In matters of public health, privacy is not a barrier to sharing information critical to public well-being.
```

The public availability of this data, and usability of this API complies with the [Office of the Privacy Commissioner of Canada](https://www.priv.gc.ca), and the [Privacy Act](https://laws-lois.justice.gc.ca/ENG/ACTS/P-21/index.html).

```
Under the Privacy Act, government institutions can only collect personal information that relates directly to an operating program or activity of the institution (section 4). Where possible, government institutions must collect personal information that is to be used for an administrative purpose directly from the individual to whom the personal information pertains, except where the individual authorizes otherwise or where personal information may be disclosed to the institution under subsection 8(2) (subsection 5(1)). The individual must also be informed of the purpose for which the information is being collected from them (subsection 5(2)). Personal information may be collected indirectly and without notice to the individual if direct collection and notice would result in the collection of inaccurate information or defeat the purpose or prejudice the use for which information is collected (subsection 5(3)).

Unless the individual has provided consent, government institutions must only use an individual’s personal information for the purpose for which it was collected or a use consistent with that purpose, or for specific purposes for which the information may be disclosed to the institution under subsection 8(2) (section 7).

Purposes for which personal information may be disclosed by a government institution without consent include:

For the purpose for which the information was obtained or compiled, or for a use consistent with that purpose (paragraph 8(2)(a)), including if employers wish to use their employee’s phone number to provide updates about a pandemic.
Where authorized by any other Act of Parliament or any regulation made thereunder that authorizes its disclosure (paragraph 8(2)(b)), such as where a public health authority has the legislative authority to require the disclosure.
Under an information sharing agreement between federal government institutions and the government of a province, some First Nations councils, the government of a foreign state, and international government organizations, for the purpose of enforcing any law or carrying out a lawful investigation (paragraph 8(2)(f)). For example, the Government of Canada is represented in a multi-lateral information sharing agreement as part of the Pan-Canadian Public Health Network.
Where, in the opinion of the head of the institution, the public interest in disclosure clearly outweighs any invasion of privacy that could result from the disclosure; or where the disclosure would clearly benefit the individual to whom the information relates (paragraph 8(2)(m)). An example of this would be if the Deputy Minister of an institution deemed that a disclosure to another institution where an infected individual recently visited and may have spread the virus satisfied the balancing test. Although the Privacy Act specifies that the federal institution needs to notify the Privacy Commissioner in advance of a public interest disclosure, it also recognizes that in certain matters, time is of the essence. Where it is not reasonably practicable for the head of the government institution to inform the Commissioner in writing prior to the disclosure, notification to the Commissioner must be made as soon as possible after the fact (subsection 8(5)). If an institution suspects that the COVID-19 virus was spread or contracted in the workplace, it is recommended that the relevant public health authority be contacted to conduct any necessary contact tracing.
```

---

## Getting Started

API URL: http://hdsb-covid-api.herokuapp.com

The API contains two endpoints.

- Get data: `/api/get-data/`
- Get schools: `/api/get-schools/`

Sending a GET request to the get data endpoint returns a JSON object of the data.\
Using the `school` query parameter, you can filter through the data directly from the API.
```
/api/get-data?school=School%20Name
```
You can send a GET request to the get schools endpoint to return an array of all school names.

See the [API Reference](#API%20Reference) for more information.

---

## API Reference

### `/api/get-data/`

Gets COVID-19 data of schools

Query parameters:
- School: name of school(s)

Returns:
- Key: school name (string)
- Value:
  - `confirmed_staff_cases` (number)
  - `confirmed_student_cases` (number)
  - `total_closed_classes` (number)
  - `school_closed` (boolean)

```json
{
    "School name": {
        "confirmed_staff_cases": 0,
        "confirmed_student_cases": 0,
        "total_closed_classes": 0,
        "school_closed": false
    }
}
```

### `/api/get-schools/`

Gets all school names

Returns:
- List of strings

```json
[
    "School name"
]
```
