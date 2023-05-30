from flask   import Flask, render_template, request, redirect, flash
import pandas as pd 
import numpy as np
from select_col import select_col
from load_data import return_model

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def form():
        if request.method == "POST":
            print('data')
            ROAC = request.form.get('ROA(C)')
            ROAA = request.form.get('ROA(A)')
            ROAB = request.form.get('ROA(B)')
            EPS = request.form.get('EPS')
            Share_net_profit = request.form.get('Share Net Profit')
            Debt_ratio = request.form.get('Debt ratio')
            Net_asset = request.form.get('Net Assets')
            net_profit_bt = request.form.get('Net profit before tax')
            Retained_Earnings = request.form.get('Retained Earnings')
            Net_Income = request.form.get('Net Income')
            sample = pd.DataFrame([[ROAC,ROAA,ROAB,EPS,Share_net_profit,
                                   Debt_ratio,Net_asset,net_profit_bt,
                                   Retained_Earnings,Net_Income]],columns = select_col)
            print(sample)
            result = result(sample)
        return render_template('form.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/eda')
def eda():
    return render_template('eda.html')

def result(sample_data):
     result = return_model.score(sample_data)
     return result

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 