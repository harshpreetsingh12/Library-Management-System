# from dbm.ndbm import library
# from importlib.resources import contents
# from operator import index
from operator import length_hint
from turtle import color, title
# from turtle import title
from flask import Flask, flash, redirect,render_template, request, session, abort
import time 
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///library.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class Library(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Lname=db.Column(db.String(200), nullable=False)
    bookn=db.Column(db.String(500), nullable=False)
    avaB=db.Column(db.String(500), nullable=True)
    passl=db.Column(db.String(500), nullable=True)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.Lname}"

@app.route('/', methods=['GET', 'POST'])
def Homein():

    if request.method=='POST':
        lname= request.form['lname']
        lname=lname.title()
        bookn= request.form['bookn']
        bookn=bookn.title()
        nbook= request.form['nbook']
        nbook=int(nbook)
        passll= request.form['passl']
        print(len(passll))
        if len(passll)>=8:
            lib = Library.query.filter_by(Lname=lname).all()
            # print(lib)
            if len(lib) == 0:
                line= bookn.split('\n')
                index=-1
                for i in range(nbook):
                    index +=1
                    change=line[index].split("=")
                    booknn=change[0]
                    avab=change[1]
                    avab=avab.title()
                    lib = Library(Lname=lname, bookn=booknn, avaB=avab,passl=passll)
                    db.session.add(lib)
                    db.session.commit()

            else:
                # alllib = Library.query.filter_by(Lname=lname).all()
                return render_template('index.html',statusl="color")
        else:
           return render_template('index.html',statusp="color")
        alllib = Library.query.filter_by(Lname=lname).all()
        return render_template('home.html',alllib=alllib)
    return render_template('index.html')

@app.route('/onlylib', methods=['GET', 'POST'])
def onlylib():
    if request.method=='POST':
        olname= request.form['olname']
        password=request.form['passl']
        # color=request.form['color']
        # print(color)
        olname=olname.title()
        lib = Library.query.filter_by(Lname=olname).first()
        if lib.passl == password:
            alllib = Library.query.filter_by(Lname=olname).all()
            return render_template('home.html',alllib=alllib,lname=olname)
        else:
            print("hey")
            return render_template('index.html',status="color")
    return render_template('index.html')

@app.route('/cool_form', methods=['GET', 'POST'])
def cool_form():
    # for i in range(n)
    pass
    # alllib= Library.query.all()
    # # print(alllib)
    return render_template('index.html')

@app.route('/delete/<int:sno>')
def delete(sno):
    lib = Library.query.filter_by(sno=sno).first()
    # for o in lib:
    #     db.session.delete(o)
    # print(lib.Lname)
    lname=lib.Lname
    db.session.delete(lib)
    db.session.commit()
    alllib = Library.query.filter_by(Lname=lname).all()
    # print(len(alllib))
    if len(alllib) == 0:
       render_template('index.html')
    else:
        return render_template('/home.html', alllib=alllib)
    return redirect('/')
    

@app.route('/returnn/<int:sno>')
def returnn(sno):
    lib = Library.query.filter_by(sno=sno).first()
    lname=lib.Lname
    # for o in lib:
    #     db.session.delete(o)
    lib.avaB="Available"
    db.session.add(lib)
    db.session.commit()
    alllib= Library.query.all()
    alllib = Library.query.filter_by(Lname=lname).all()
    return render_template('home.html',alllib=alllib)

@app.route('/issue/<int:sno>',methods=['GET','POST'])
def issue(sno):
    if request.method=='POST':
        oname=request.form['oname']
        oname=oname.title()
        lib = Library.query.filter_by(sno=sno).first()
        lname=lib.Lname
        lib.avaB=oname
        db.session.add(lib)
        db.session.commit()
        # eval_res, tempfile = js2py.run_file("static/dev/test.js")
        # tempfile.wish("GeeksforGeeks")
        alllib = Library.query.filter_by(Lname=lname).all()
        return render_template('home.html',alllib=alllib)
        
    lib = Library.query.filter_by(sno=sno).first()
    return render_template('issue.html',lib=lib, flash_message="False")

@app.route('/addbooks/<lname>', methods=['GET', 'POST'])
def addbooks(lname):
        if request.method=='POST':
            lname= request.form['lname']
            lname=lname.title()
            bookn= request.form['bookn']
            bookn =bookn.title()
            nbook= request.form['nbook']
            nbook=int(nbook)
            getpass = Library.query.filter_by(Lname=lname).first()
            passw=getpass.passl
            line= bookn.split('\n')
            # print(line[0])
            index=-1
            for g in range(nbook):
                index +=1
                change=line[index].split("=")
                booknn=change[0]
                avab=change[1]
                avab=avab.title()
                lib = Library(Lname=lname, bookn=booknn, avaB=avab,passl=passw)
                db.session.add(lib)
                db.session.commit()
            alllib = Library.query.filter_by(Lname=lname).all()
            return render_template('home.html',alllib=alllib)   
        return render_template('bookup.html',Lname=lname)
@app.route('/allbook', methods=['GET', 'POST'])
def allbook():
    alllib = Library.query.all()
    return render_template('home.html',alllib=alllib)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method=='POST':
        books= request.form['books']
        books=books.title()
        lib = Library.query.filter_by(bookn=books).all()
        return render_template('home.html',alllib=lib)  

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        # newl=request.form['newl']
        # newl=newl.title()
        newb=request.form['newb']
        newb=newb.title()
        newa=request.form['newa']
        newa=newa.title()
        lib = Library.query.filter_by(sno=sno).first()
        newl=lib.Lname
        lib.avaB=newa
        lib.bookn=newb
        db.session.add(lib)
        db.session.commit()
        # eval_res, tempfile = js2py.run_file("static/dev/test.js")
        # tempfile.wish("GeeksforGeeks")
        alllib = Library.query.filter_by(Lname=newl).all()
        return render_template('home.html',alllib=alllib)
        
    lib = Library.query.filter_by(sno=sno).first()
    return render_template('update.html',lib=lib)

# @app.route('/search')
# def searchbook():
#     return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)