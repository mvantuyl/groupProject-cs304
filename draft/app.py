"Emily Mattlin, Sarah Pardo, Safiya Sirota, Mileva Van Tuyl"
from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
import cs304dbi as dbi
import functions

app = Flask(__name__)

import random

app.secret_key = 'your secret here'
# replace that with a random key
app.secret_key = ''.join([ random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' +
                                          'abcdefghijklmnopqrstuvxyz' +
                                          '0123456789'))
                           for i in range(20) ])

# This gets us better error messages for certain common request errors
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
# fake bNum for now 4/23/2020 draft version - pre login implementation
FOObNum = '20000000'
@app.route('/')
def index():
    return render_template('home.html', courses = functions.getRecommended())

@app.route('/create/', methods=['GET','POST'])
def createCourse():
    if request.method == 'GET':
        return render_template('create_course.html')
    else:
        values = functions.getCourseInfo()
        courseInfo = functions.insertCourse(values)
        cid = functions.getCID(courseInfo)
        flash('Your updates have been made, insert another course!')
        return redirect(url_for('uploadSyllabus', n = cid))

@app.route('/upload/<int:n>', methods=['GET','POST'])
def uploadSyllabus(n):
    if request.method == 'GET':
        return render_template('syl_upload.html')
    else:
        functions.fileUpload()
        return render_template('home.html')

@app.route('/search/', methods = ['GET']) 
def search(): 
    search = request.args.get('search')
    kind = request.args.get('type')

<<<<<<< HEAD
=======
@app.route('/search/', methods = ['GET']) 
def search(): 
    search = request.args.get('search')
    kind = request.args.get('type')

>>>>>>> c60aa6853c423fbd2febc3d7fe23ce71d2b615d6
    allSections = functions.getAllSections(search, kind)

    # Sort these alphabetically by cnum
    allCourses = functions.getCourses(allSections)

    # No results: redirect user to create a new course
    if len(allSections) == 0:
        flash ('No results for {} in the database.'.format(search))
        return redirect(url_for('createCourse')) 

    # One result: redirect user to specific course page
    elif len(allSections) == 1: 
        return redirect(url_for('showCourse', cid = allSections[0]['cid']))
    
    # Multiple results: display all the results
    else: 
        return render_template('search_results.html', 
        allCourses = allCourses, allSections = allSections, query = search)

@app.route('/course/<cid>', methods=['GET','POST'])
def showCourse(cid):
    basics = functions.getBasics(cid)
    if request.method == 'GET':
<<<<<<< HEAD
        avgRatings = functions.getAvgRatings(cid)
        comments = functions.getComments(cid)
        return render_template('course_page.html', basics = basics, avgRatings = avgRatings, comments=comments)
    elif request.method == 'POST':
        #user is rating (which includes commenting) the course.
        uR = request.form.get('usefulRate')
        dR = request.form.get('diffRate')
        rR = request.form.get('relevRate')
        eR = request.form.get('expectRate')
        hW = request.form.get('hoursWk')
        comment = request.form.get('new_comment')
        functions.makeRatings(FOObNum, cid, rR, uR, dR, eR, hW, comment)
        #have to recalculate the ratings and fetch the comments again
        avgRatings = functions.getAvgRatings(cid)
        comments = functions.getComments(cid)
        #now we render the page again
        return render_template('course_page.html', basics = basics, avgRatings = avgRatings, comments=comments)

@app.route('/course/<cid>/update', methods=['GET','POST'])
=======
        basics = functions.getBasics(cid)
        avgRatings = functions.getAvgRatings(cid)
        comments = functions.getComments(cid)
        print('basics: ')
        print(basics)
        print('avgRatings: ')
        print(avgRatings)
        print('comments: ')
        print(comments)
        return render_template('course_page.html', title=basics['title'],
            cnum=basics['cnum'], dep=basics['dep'], prof=basics['prof'],
            yr=basics['yr'], sem=basics['sem'], crn=basics['crn'], syl=basics['syl'],
            web=basics['web'], usefullRate=avgRatings['usefullRate'], 
            diffRate=avgRatings['diffRate'], relevRate=avgRatings['relevRate'], 
            expectRate=avgRatings['expectRate'], hoursWk=avgRatings['hoursWk'],
            comments=comments)
    elif request.method == 'POST':
        #user is rating (which includes commenting) the course.
        action = request.form.get("submit")
        if action == 'rate':
            uR = request.form.get('usefulRate')
            dR = request.form.get('diffRate')
            rR = request.form.get('relevRate')
            eR = request.form.get('expectRate')
            hW = request.form.get('hoursWk')
            comment = request.form.get('new_comment')
            makeRatings(bNum, cid, rR, uR, dR, eR, hW, comment)
            #have to recalculate the ratings and fetch the comments again
            avgRatings = functions.getAvgRatings(cid)
            comments = functions.getComments(cid)
            #now we render the page again
            return render_templates('course_page.html', title=basics['title'],
            cnum=basics['cnum'], dep=basics['dep'], prof=basics['prof'],
            yr=basics['yr'], sem=basics['sem'], crn=basics['crn'], syl=basics['syl'],
            web=basics['web'], usefullRate=avgRatings['usefullRate'], 
            diffRate=avgRatings['diffRate'], relevRate=avgRatings['relevRate'], 
            expectRate=avgRatings['expectRate'], hoursWk=avgRatings['hoursWk'],
            comments=comments)

@app.route('/courses/<cid>/update', methods=['GET','POST'])
>>>>>>> c60aa6853c423fbd2febc3d7fe23ce71d2b615d6
def updateCourse(cid):
    if request.method == 'GET':
        flash("This feature coming soon!")

@app.route('/formecho/', methods=['GET','POST'])
def formecho():
    if request.method == 'GET':
        return render_template('form_data.html',
                               method=request.method,
                               form_data=request.args)
    elif request.method == 'POST':
        return render_template('form_data.html',
                               method=request.method,
                               form_data=request.form)
    else:
        return render_template('form_data.html',
                               method=request.method,
                               form_data={})

@app.route('/testform/')
def testform():
    return render_template('testform.html')


if __name__ == '__main__':
    import sys, os
    if len(sys.argv) > 1:
        # arg, if any, is the desired port number
        port = int(sys.argv[1])
        assert(port>1024)
    else:
        port = os.getuid()
    # the following database code works for both PyMySQL and SQLite3
    dbi.cache_cnf()
    dbi.use('syllabo_db')
    conn = dbi.connect()
    curs = dbi.dict_cursor(conn)
    # the following query works for both MySQL and SQLite
    curs.execute('select current_timestamp as ct')
    row = curs.fetchone()
    ct = row['ct']
    print('connected to Syllabo DB at {}'.format(ct))
    app.debug = True
    app.run('0.0.0.0',port)
