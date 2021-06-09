"""
Routes and views for the flask application.
"""

from flask import render_template
from FlaskWebProject3 import  app
from flask import request
from race import Drom,SportCar

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
