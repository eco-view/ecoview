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
