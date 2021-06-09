"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,jsonify
from FlaskWebProject3 import  app
from flask import send_from_directory,request
from my_class1 import Myclass

from race import Drom,SportCar

from flask_mysqldb import MySQL

mysql = MySQL(app)

@app.route('/')
#@app.route('/myhome')
def home():
    """Renders the home page."""
     #https://github.com/alexferl/flask-mysqldb
    #lst =[1,2,3]
    #cur = mysql.connection.cursor()
    #cur.execute('''SELECT * FROM TestJson''')
    #rv = cur.fetchall()
    #srv = jsonify({"res":rv})

    return render_template(
        'index.html',
        title='Home Page')


    #return render_template(
    #    'index.html',
    #    title='Home Page',
    #    res= srv.json['res'],
    #    year=srv, ##datetime.now().year,
    #    tst =lst
    

@app.route('/race', methods=['post', 'get'])
def race():
    mth = "GET"
    race = None
    race_html = None
    drom = None

    if request.method == 'POST':
        cars = request.form.get('cars')
        races = request.form.get('races')
        mth = "POST"
        
        drom = Drom(int(cars), SportCar)

        for i in range(int(races)):
            drom.race()


        #drom.race()
        #drom.race()
        #drom.race()
        #drom.race()

        race_html = drom.df_empty.style.apply(highlight_max,axis=1)\
          .highlight_max(axis=None, color='yellow')\
          .highlight_min(axis=None, color='cyan')\
          .set_table_styles(styles).render() 

  

    return render_template(
        'race.html',
        title='Гонки',
        method = mth,
        race = drom.df_empty if drom else '',
        race_html = race_html if race_html else '')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/pyth')
def pyth():
    """Renders the python page."""
    return render_template(
        'python.html',
        title='PythonTest',
        year=datetime.now().year,
        message="Тестируем Pyodide"
    )

@app.route("/myhome")
def base():
    return send_from_directory('client/public/', 'index.html') #public

@app.route("/second")
def basesecond():
    return send_from_directory('client/dist/second', 'index.html') #public



@app.route("/<path:path>")
def svelte_client(path):
    return send_from_directory('client/public', path) #public

#https://www.rithmschool.com/courses/flask-fundamentals/templating-with-jinja2
@app.route('/data')
def print_name():
    cl =Myclass('111','222')
    cl.test()

    first = request.args.get('first')
    last = request.args.get('last')
    return f"You put {first} {last} {cl.one} -- {cl.two}"


def highlight_max(s):
    '''
    Подсветка макс. значений в серии (строке или столбце)
    '''

    is_max = (s == s.max() ) # | ( s == s.min())
    is_min = s == s.min()

    r= ['background-color: red;' if v else '' for v in is_max] 
    s =['background-color: blue;' if v else '' for v in is_min]
    
    f =[v if v else s[i] if s[i] else "" for i,v in enumerate(r)   ]
    return f

styles = [
    dict(selector="th", props=[("font-size", "110%"),
                               ("color", "red"),
                               ("padding","5px"),
                               ("border", "1px solid gray"),
                               ("text-align", "center")]),
    dict(selector="tr", props=[("font-size", "120%"),
                               ("text-align", "center")]),
    dict(selector="td", props=[("border", "1px solid gray"),("padding","5px")]),
     ] 