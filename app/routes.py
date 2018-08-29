from flask import render_template, flash, redirect, url_for, request
from app.forms import CompanyForm
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title = 'Home')


@app.route('/CompareCompanies', methods=['GET', 'POST'])
def route():
    form = CompanyForm()
    if form.validate_on_submit():
        flash('Congratulations, you have actually entered data!')
        return redirect(url_for('index'))
    return render_template('enter_co.html', title="Company Entry", form=form)

