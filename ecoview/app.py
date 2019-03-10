from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify, Markup
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from flask_table import Table, Col
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import json
import pygal


app = Flask(__name__)


# 404 Error Handling
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template('404.html')


# config mySQL
# this allows access from a remote client, if desired
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ee494'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# initialize MYSQL
mysql = MySQL(app)


# # # api # # was # # here # # #

# API SPLASH
@app.route('/api')
def api_splash():
    info = {'about': 'ecoview is a cloud-based recycling project', 'api': 'ecoview employs a URL-based assign/delimit protocol for automatic data entry', 'access': 'url_root/api/<...>', 'assign': '=', 'delimit': '-'}
    state_syntax = {'action': 'state', 'token': '<STRING>', 'machine': '<INT>', 'tote1level': '<INT>', 'tote1tally': '<INT>', 'tote2level': '<INT>', 'tote2tally': '<INT>', 'tote3level': '<INT>', 'tote3tally': '<INT>', 'tote4level': '<INT>', 'tote4tally': '<INT>', 'tote5level': '<INT>', 'tote5tally': '<INT>', 'tote6level': '<INT>', 'tote6tally': '<INT>'}
    process_syntax = {'action': 'process', 'token': '<STRING>', 'machine': '<INT>', 'filename': '<STRING>', 'modelresult': '<INT>', 'confidence': '<INT>', 'computetime': '<STRING>'}
    examples = {'state EXAMPLE': 'http://localhost:8080/api/token=abcde-action=state-machine=10001-t1lv=11-t1tl=1-t2lv=22-t2tl=2-t3lv=33-t3tl=3-t4lv=44-t4tl=4-t5lv=55-t5tl=5-t6lv=66-t6tl=6',
    'process EXAMPLE': 'http://localhost:8080/api/token=abcde-action=process-machine=10001-filename=img00001-modelresult=1-confidence=100-computetime=4'}
    calling_card =  jsonify([info, state_syntax, process_syntax, examples])

    return calling_card
    # return render_template('api_splash.html', calling_card=calling_card)


# api POST method
@app.route('/api', defaults={'path': ''})
@app.route('/<path:path>')
def api_post(path, methods='GET'):
    try:
        url_text = request.url
        new_list = url_text.split("api/")
        key_value_list = new_list[1].split("-")
        keys, values = zip(*(s.split("=") for s in key_value_list))
        api_request_dict = dict(zip(keys, values))
    except:
        return "Error: unable to parse request", 400

    # Check if potential verification pairs are present
    try:
        unverified_token = api_request_dict['token']
        unverified_action = api_request_dict['action']
        # unverified_machine = api_request_dict['machine']
    except:
        return "Error: insufficient credentials", 400

    # Verify credentials
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT token, machine FROM devicedb")
    verified_pairs = cur.fetchall()
    verified_list = list(verified_pairs)
    cur.close()
    # Check if unverified_token is valid
    if unverified_token not in str(verified_list):
        return "Error: invalid credentials", 400

    # Determine POST type from 'action'
    if unverified_action == 'state':
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO state(machine, tote1level, tote1tally, tote2level, tote2tally, tote3level, tote3tally, tote4level, tote4tally, tote5level, tote5tally, tote6level, tote6tally) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (api_request_dict['machine'], int(api_request_dict['t1lv']), int(api_request_dict['t1tl']), int(api_request_dict['t2lv']), int(api_request_dict['t2tl']), int(api_request_dict['t3lv']), int(api_request_dict['t3tl']), int(api_request_dict['t4lv']), int(api_request_dict['t4tl']), int(api_request_dict['t5lv']), int(api_request_dict['t5tl']), int(api_request_dict['t6lv']), int(api_request_dict['t6tl'])))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('statedata'))
        except:
            cur.close()
            return "Error: unable to update state", 400

    elif unverified_action == 'process':
        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO process(machine, filename, modelresult, confidence, computetime) VALUES(%s, %s, %s, %s, %s)", (api_request_dict['machine'], api_request_dict['filename'], int(api_request_dict['modelresult']), int(api_request_dict['confidence']), api_request_dict['computetime']))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('processdata'))
        except:
            cur.close()
            return "Error: unable to update process", 400
    else:
        return "Error: invalid action", 400

    return redirect(url_for('index'))


# Index
@app.route('/')
def index():
    colors = [
    "#FCB712", "#F37020", "#CD004D", "#6460AC",
    "#008AD2", "#0CB14B"]

    cur = mysql.connection.cursor()
    result = cur.execute("SELECT tote1level, tote2level, tote3level, tote4level, tote5level, tote6level FROM state ORDER BY id DESC LIMIT 0, 1")
    current_levels = cur.fetchone()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT modelresult FROM process")
    results = cur.fetchall()
    cur.close()
    result_list = [item['modelresult'] for item in results]

    cur = mysql.connection.cursor()
    cur.execute("SELECT tote1tally, tote2tally, tote3tally, tote4tally, tote5tally, tote6tally FROM state ORDER BY id DESC LIMIT 0, 1")
    tallys = cur.fetchone()
    cur.close()
    if tallys is not None:
        tally_list = list(tallys.values())
    else:
        tally_list = [0, 0, 0, 0, 0, 0, 0]

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, time, tote1level, tote2level, tote3level, tote4level, tote5level, tote6level FROM state")
    history = cur.fetchall()
    cur.close()

    id_list = []
    time_list = []
    tote1_list = []
    tote2_list = []
    tote3_list = []
    tote4_list = []
    tote5_list = []
    tote6_list = []

    if history is not None:
        for item in history:
            id_list.append(item['id'])
            time_list.append(item['time'])
            tote1_list.append(item['tote1level'])
            tote2_list.append(item['tote2level'])
            tote3_list.append(item['tote3level'])
            tote4_list.append(item['tote4level'])
            tote5_list.append(item['tote5level'])
            tote6_list.append(item['tote6level'])

    num_0 = result_list.count(0)
    num_1 = result_list.count(1)
    num_2 = result_list.count(2)
    num_3 = result_list.count(3)
    num_4 = result_list.count(4)
    num_5 = result_list.count(5)
    num_6 = result_list.count(6)
    model_list = [num_1, num_2, num_3, num_4, num_5, num_6, num_0]

    if result > 0:
        level_list = list(current_levels.values())
    else:
        level_list = [1, 1, 1, 1, 1, 1]

    return render_template('home.html', level_list=level_list, colors=colors, model_list=model_list, tally_list=tally_list, id_list=id_list, tote1_list=tote1_list, tote2_list=tote2_list, tote3_list=tote3_list, tote4_list=tote4_list, tote5_list=tote5_list, tote6_list=tote6_list, time_list=time_list)


# About
@app.route('/about')
def about():
    return render_template('about.html')


# Articles
@app.route('/articles')
def articles():
    # return render_template('articles.html', articles = Articles)
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    if result > 0:
        return render_template('articles.html', articles=articles)
    else:
        msg = 'No articles found'
        return render_template('articles.html', msg=msg)
    # Close connection
    cur.close()


# Single Article
@app.route('/article/<string:id>/')
def article(id): # query mySQL to retrieve data
    # Create cursor
    cur = mysql.connection.cursor()

    # Get article
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    article = cur.fetchone()

    return render_template('article.html', article=article)


# State Data page
@app.route('/state')
def statedata():
    # Declare your table
    # this is where you would add more totes
    class ItemTable(Table):
        # id = Col('ID')
        time = Col('Timestamp')
        machine = Col('System ID')
        tote1level = Col('Tote 1 Level')
        tote2level = Col('Tote 2 Level')
        tote3level = Col('Tote 3 Level')
        tote4level = Col('Tote 4 Level')
        tote5level = Col('Tote 5 Level')
        tote6level = Col('Tote 6 Level')
        tote1tally = Col('Tote 1 Count')
        tote2tally = Col('Tote 2 Count')
        tote3tally = Col('Tote 3 Count')
        tote4tally = Col('Tote 4 Count')
        tote5tally = Col('Tote 5 Count')
        tote6tally = Col('Tote 6 Count')

    # Load items from your database
    # Create cursor
    cur = mysql.connection.cursor()
    # Get data
    result = cur.execute("SELECT * FROM state ORDER BY id DESC")
    items = cur.fetchall()
    # Close connection
    cur.close()
    # Populate the table
    table = ItemTable(items)

    return render_template('state.html', table=table)


# Process Data page
@app.route('/process')
def processdata():
    # Declare your table
    class ItemTable(Table):
        # id = Col('ID')
        time = Col('Timestamp')
        machine = Col('System ID')
        filename = Col('Filename')
        modelresult = Col('Model Result')
        confidence = Col('Confidence')
        computetime = Col('Compute Time')

    # Load items from your database
    # Create cursor
    cur = mysql.connection.cursor()

    # Get data
    result = cur.execute("SELECT * FROM process ORDER BY id DESC")
    items = cur.fetchall()

    # Close connection
    cur.close()

    # Populate the table
    table = ItemTable(items)

    return render_template('process.html', table=table)




#
# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor
        cur = mysql.connection.cursor()

        # execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        # commit to DB
        mysql.connection.commit()

        # close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)


# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare passwords
            if sha256_crypt.verify(password_candidate, password):
                # app.logger.info('PASSWORD MATCHED')
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                # app.logger.info('PASSWORD NOT MATCHED')
                error = 'Invalid login'
                return render_template('login.html', error=error)
                # Close connection
            cur.close()
        else:
            # app.logger.info('NO USER')
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please log in', 'danger')
            return redirect(url_for('login'))
    return wrap


# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


################################
# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    # Create cursor
    cur = mysql.connection.cursor()

    # Get articles
    result = cur.execute("SELECT * FROM articles")
    articles = cur.fetchall()

    # Close connection
    cur.close()

    # Create cursor
    cur = mysql.connection.cursor()

    # Get devices
    result = cur.execute("SELECT * FROM devicedb")
    devices = cur.fetchall()

    # Close connection
    cur.close()

    return render_template('dashboard.html', articles=articles, devices=devices)


##################################
# Article Form Class
class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])


# Add Article
@app.route('/add_article', methods=['GET','POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)",(title, body, session['username']))
        mysql.connection.commit()
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))
    return render_template('add_article.html', form=form)


# Edit Article
@app.route('/edit_article/<string:id>', methods=['GET','POST'])
@is_logged_in
def edit_article(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    article = cur.fetchone()

    # Get form
    form = ArticleForm(request.form)

    # Populate article form fields
    form.title.data = article['title']
    form.body.data = article['body']


    if request.method=='POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE articles SET title=%s, body=%s WHERE id = %s", (title, body, id))
        mysql.connection.commit()
        cur.close()

        flash('Article Updated', 'success')
        return redirect(url_for('dashboard'))
    return render_template('edit_article.html', form=form)


# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST'])
@is_logged_in
def delete_article(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM articles WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()

    flash('Article Deleted', 'success')
    return redirect(url_for('dashboard'))


# DeviceForm
class DeviceForm(Form):
    machine = StringField('Machine #', [validators.Length(min=1, max=11)])
    nickname = StringField('Nickname', [validators.Length(min=0, max=11)])
    ip_address = StringField('IP Address', [validators.Length(min=0, max=50)])
    token = StringField('Token', [validators.Length(min=4, max=20)])
    latitude = StringField('Latitude', [validators.Length(min=0, max=100)])
    longitude = StringField('Longitude', [validators.Length(min=0, max=100)])
    configvariables = StringField('Config Variables', [validators.Length(min=0, max=100)])


# Add Device
@app.route('/add_device', methods=['GET','POST'])
@is_logged_in
def add_device():
    form = DeviceForm(request.form)
    if request.method == 'POST' and form.validate():
        machine = form.machine.data
        nickname = form.nickname.data
        ip_address = form.ip_address.data
        token = form.token.data
        latitude = form.latitude.data
        longitude = form.longitude.data
        configvariables = form.configvariables.data

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO devicedb(machine, nickname, ip_address, token, latitude, longitude, configvariables) VALUES(%s, %s, %s, %s, %s, %s, %s)", (machine, nickname, ip_address, token, latitude, longitude, configvariables))
        mysql.connection.commit()
        cur.close()

        flash('Device Created', 'success')

        return redirect(url_for('dashboard'))
    return render_template('add_device.html', form=form)


# Edit Device
@app.route('/edit_device/<string:id>', methods=['GET','POST'])
@is_logged_in
def edit_device(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM devicedb WHERE id = %s", [id])
    device = cur.fetchone()

    # Get form
    form = DeviceForm(request.form)

    # Populate devices from fields
    form.machine.data = device['machine']
    form.nickname.data = device['nickname']
    form.ip_address.data = device['ip_address']
    form.token.data = device['token']
    form.latitude.data = device['latitude']
    form.longitude.data = device['longitude']
    form.configvariables.data = device['configvariables']

    if request.method == 'POST' and form.validate():
        machine = request.form['machine']
        nickname = request.form['nickname']
        ip_address = request.form['ip_address']
        token = request.form['token']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        configvariables = request.form['configvariables']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE devicedb SET machine=%s, nickname=%s, ip_address=%s, token=%s, latitude=%s, longitude=%s, configvariables=%s WHERE id = %s", (machine, nickname, ip_address, token, latitude, longitude, configvariables, id))
        mysql.connection.commit()
        cur.close()

        flash('Device Updated', 'success')
        return redirect(url_for('dashboard'))
    return render_template('edit_device.html', form=form)


# Delete Device
@app.route('/delete_device/<string:id>', methods=['POST'])
@is_logged_in
def delete_device(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM devicedb WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()

    flash('Device Deleted', 'success')
    return redirect(url_for('dashboard'))


# Reset States reading
@app.route('/reset_state', methods=['POST'])
@is_logged_in
def reset_state():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM state")
    mysql.connection.commit()
    cur.close()

    flash('Successfully Reset', 'success')
    return redirect(url_for('dashboard'))


# Reset Process reading
@app.route('/reset_process', methods=['POST'])
@is_logged_in
def reset_process():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM process")
    mysql.connection.commit()
    cur.close()

    flash('Successfully Reset', 'success')
    return redirect(url_for('dashboard'))


@app.route("/beta")
def beta():

    return render_template('beta.html')


if __name__ == '__main__':
    app.secret_key='secret123'
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(port=8080, debug=True)
