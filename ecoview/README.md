# MySQL Configuration
```bash
mysql.server start
mysql -u root -p
>> ee494
USE myflaskapp;
```

```bash
SHOW DATABASES;
USE myflaskapp;
SHOW TABLES;
```

```bash

CREATE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), username VARCHAR(30), password VARCHAR(100) register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

```

```bash

CREATE TABLE process (id INT AUTO_INCREMENT PRIMARY KEY, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, machine VARCHAR(11), filename VARCHAR(100), modelresult INT(11), confidence INT(11), computetime INT(11));

```

```bash

CREATE TABLE state (id INT AUTO_INCREMENT PRIMARY KEY, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, machine VARCHAR(100), tote1level INT(11), tote1tally INT(11), tote2level INT(11), tote2tally INT(11), tote3level INT(11), tote3tally INT(11), tote4level INT(11), tote4tally INT(11), tote5level INT(11), tote5tally INT(11), tote6level INT(11), tote6tally INT(11));

```

```bash

CREATE TABLE devicedb (id INT AUTO_INCREMENT PRIMARY KEY, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, machine VARCHAR(11), nickname VARCHAR(30), ip_address VARCHAR(50), token VARCHAR(20), latitude VARCHAR(100), longitude VARCHAR(100), configvariables  VARCHAR(100));

```
```
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
```

```
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
```

```
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
```
