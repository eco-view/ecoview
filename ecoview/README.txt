%% MySQL -- terminal commands

SHOW DATABASES;
USE myflaskapp;
SHOW TABLES;

CREATE TABLE process (id INT(11) AUTO_INCREMENT PRIMARY KEY, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, machine VARCHAR(11), filename VARCHAR(100), modelresult INT(11), confidence INT(11), computetime VARCHAR(111));

CREATE TABLE state (id INT(11) AUTO_INCREMENT PRIMARY KEY, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, machine VARCHAR(100), tote1level INT(11), tote1tally INT(11));

CREATE TABLE devicedb (id INT(11) AUTO_INCREMENT PRIMARY KEY, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, machine VARCHAR(11), nickname VARCHAR(30), ip_address VARCHAR(50), token VARCHAR(20), latitude VARCHAR(100), longitude VARCHAR(100), configvariables  VARCHAR(100));

mysql> DESCRIBE state;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | int(11)      | NO   | PRI | NULL              | auto_increment    |
| time       | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| machine    | varchar(100) | YES  |     | NULL              |                   |
| tote1level | int(11)      | YES  |     | NULL              |                   |
| tote1tally | int(11)      | YES  |     | NULL              |                   |
+------------+--------------+------+-----+-------------------+-------------------+
5 rows in set (0.00 sec)

mysql> DESCRIBE process;
+-------------+--------------+------+-----+-------------------+-------------------+
| Field       | Type         | Null | Key | Default           | Extra             |
+-------------+--------------+------+-----+-------------------+-------------------+
| id          | int(11)      | NO   | PRI | NULL              | auto_increment    |
| time        | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| machine     | varchar(11)  | YES  |     | NULL              |                   |
| filename    | varchar(100) | YES  |     | NULL              |                   |
| modelresult | int(11)      | YES  |     | NULL              |                   |
| confidence  | int(11)      | YES  |     | NULL              |                   |
| computetime | varchar(111) | YES  |     | NULL              |                   |
+-------------+--------------+------+-----+-------------------+-------------------+
7 rows in set (0.00 sec)

mysql> DESCRIBE devicedb;
+-----------------+--------------+------+-----+-------------------+-------------------+
| Field           | Type         | Null | Key | Default           | Extra             |
+-----------------+--------------+------+-----+-------------------+-------------------+
| id              | int(11)      | NO   | PRI | NULL              | auto_increment    |
| time            | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| machine         | varchar(11)  | YES  |     | NULL              |                   |
| nickname        | varchar(30)  | YES  |     | NULL              |                   |
| ip_address      | varchar(50)  | YES  |     | NULL              |                   |
| token           | varchar(20)  | YES  |     | NULL              |                   |
| latitude        | varchar(100) | YES  |     | NULL              |                   |
| longitude       | varchar(100) | YES  |     | NULL              |                   |
| configvariables | varchar(100) | YES  |     | NULL              |                   |
+-----------------+--------------+------+-----+-------------------+-------------------+
9 rows in set (0.00 sec)

"""
We want to take input from '/api/*'
POST that data to DB
Return success code 200
Redirect to /api_splash
"""


[{"ID": 10, "SERIAL": 1000, "TIMESTAMP": "05-Mar-2019 07:12:00", "TOTE_1_LVL": 77, "TOTE_1_TAL": 27}]


%% reverse table row display order
  ORDER BY FIELD(id)

%% on dashboard, RESET STATE, PROCESS



































<td>{{device.machine}}</td>
<td>{{device.nickname}}</td>
<td>{{device.time}}</td>
<td>{{device.ip_address}}</td>
<td>{{device.token}}</td>
<td>{{device.latitude}}</td>
<td>{{device.longitude}}</td>
<td>{{device.configvariables}}</td>



# state TEST
http://localhost:8080/api/token=abcde-action=state-machine=10001-tote1level=71-tote1tally=80

# process TEST
http://localhost:8080/api/token=abcde-action=process-machine=10001-filename=img001-modelresult=1-confidence=91-computetime-4





def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")


This code is analogous to:

function(argument){
    switch(argument) {
        case 0:
            return "zero";
        case 1:
            return "one";
        case 2:
            return "two";
        default:
            return "nothing";
    };
};

# # Get some objects
# this is where you would add more totes
# class Item(object):
#     def __init__(self, id, time, machine, tote1level, tote1tally):
#         self.id = id
#         self.time = time
#         self.machine = machine
#         self.tote1level = tote1level
#         self.tote1tally = tote1tally


# # Get some objects
# class Item(object):
#     def __init__(self, id, time, machine, tote1level, tote1tally):
#         self.id = id
#         self.time = time
#         self.machine = machine
#         self.filename = tote1level
#         self.modelresult = tote1tally
#         self.confidence = confidence
#         slef.computetime = computetime


# # # ~~~ LEGACY ~~~

# api = Api(app)

# # API
# class HelloWorld(Resource):
#     def get(self):
#         info = {'about': 'ecoview is a cloud-based recycling project', 'api': 'ecoview employs a URL-based protocol for automatic data entry', 'access': '/api/...', 'assign': '=', 'delimit': '-'}
#         state_syntax = {'action': 'state', 'token': '<STRING>', 'machine': '<INT>', 'tote1level': '<INT>', 'tote1tally': '<INT>'}
#         process_syntax = {'action': 'process', 'token': '<STRING>', 'machine': '<INT>', 'filename': '<STRING>', 'modelresult': '<INT>', 'confidence': '<INT>', 'computetime': '<STRING>'}
#         examples = {'state': 'http://localhost:8080/api/token=abcde-action=state-machine=10001-tote1level=71-tote1tally=80',
#         'process': 'http://localhost:8080/api/token=abcde-action=process-machine=10001-filename=img001-modelresult=1-confidence=91-computetime=4'}
#         return [info, state_syntax, process_syntax, examples]
#     # def post(self):
#     #     some_json= request.get_json()
#     #     return {'you sent': some_json}, 201
#
#
# class myApi(Resource):
#     def get(self, url_text, methods=['GET', 'POST']):
#             # Try to parse dict from request
#             try:
#                 url_text = request.url
#                 new_list = url_text.split("api/")
#                 key_value_list = new_list[1].split("-")
#                 keys, values = zip(*(s.split("=") for s in key_value_list))
#                 api_request_dict = dict(zip(keys, values))
#             except:
#                 return {'Error': 'unable to parse request'}, 400
#
#             # Check if potential verification pairs are present
#             try:
#                 unverified_token = api_request_dict['token']
#                 unverified_action = api_request_dict['action']
#                 # unverified_machine = api_request_dict['machine']
#             except:
#                 return {'Error': 'insufficient credentials'}, 400
#
#             # Verify credentials
#             cur = mysql.connection.cursor()
#             result = cur.execute("SELECT token, machine FROM devicedb")
#             verified_pairs = cur.fetchall()
#             verified_list = list(verified_pairs)
#             cur.close()
#             # Check if unverified_token is valid
#             if unverified_token not in str(verified_list):
#                 return {'Error': 'invalid credentials'}, 400
#
#             # Determine POST type from 'action'
#             if unverified_action == 'state':
#                 try:
#                     cur = mysql.connection.cursor()
#                     cur.execute("INSERT INTO state(machine, tote1level, tote1tally) VALUES(%s, %s, %s)", (api_request_dict['machine'], int(api_request_dict['tote1level']), int(api_request_dict['tote1tally'])))
#                     mysql.connection.commit()
#                     cur.close()
#                     flash('State data updated', 'success')
#                     # NEED TO CLEAR URL HERE *****
#                     return redirect(url_for('index'))
#                 except:
#                     # cur.close()
#                     return {'Error': 'unable to update state'}, 400
#
#             elif unverified_action == 'process':
#                 try:
#                     cur = mysql.connection.cursor()
#                     cur.execute("INSERT INTO process(machine, filename, modelresult, confidence, computetime) VALUES(%s, %s, %s, %s, %s)", (api_request_dict['machine'], api_request_dict['filename'], int(api_request_dict['modelresult']), int(api_request_dict['confidence']), api_request_dict['computetime']))
#                     mysql.connection.commit()
#                     cur.close()
#                     flash('Process data updated', 'success')
#                     return redirect(url_for('index'))
#                 except:
#                     # cur.close()
#                     return {'Error': 'unable to update process'}, 400
#             else:
#                 return {'Error': 'invalid action'}, 400
#
#             return redirect(url_for('dashboard'))
#
#
# api.add_resource(HelloWorld, '/api')
# api.add_resource(myApi, '/api/<string:url_text>')
