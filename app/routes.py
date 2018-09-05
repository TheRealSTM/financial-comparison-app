from flask import render_template, flash, redirect, url_for, request
from app.forms import CompanyForm
from app import app
from app.finance_logic import getCompanyClose, graphStockData


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title = 'Home')


@app.route('/CompareCompanies', methods=['GET', 'POST'])
def route():
    form = CompanyForm()
    if form.validate_on_submit():
        comp = [form.company_a.data, form.company_b.data]
        close_compA = getCompanyClose(comp[0])
        close_compB = getCompanyClose(comp[1])
        graph = graphStockData(close_compA, close_compB, comp)
        return render_template('test.html', title="Closing Price", url=graph)
    return render_template('enter_co.html', title="Company Entry", form=form)



