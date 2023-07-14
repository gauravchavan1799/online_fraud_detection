from flask import Flask, request, jsonify, render_template ,redirect, url_for
from utils import OnlineFraudDetection
import config
import traceback
app = Flask(__name__)

@app.route('/home')
def home():
    print("Testing Home Page API")

    return render_template('index.html')


@app.route('/pred_fraud', methods = ['GET', 'POST'])
def pred_fraud():
    try:
        if request.method == 'GET':
            data = request.args
            print("Data:", data)
            step = int(data.get('step')) if data.get('step') is not None else 0
            amount = int(data.get('amount')) if data.get('amount') is not None else 0
            oldbalanceOrg = int(data.get('oldbalanceOrg')) if data.get('oldbalanceOrg') is not None else 0
            newbalanceOrig = int(data.get('newbalanceOrig')) if data.get('newbalanceOrig') is not None else 0
            oldbalanceDest = int(data.get('oldbalanceDest')) if data.get('oldbalanceDest') is not None else 0
            newbalanceDest = int(data.get('newbalanceDest')) if data.get('newbalanceDest') is not None else 0
            types = data.get('types', '')  # Set default value as an empty string

            Obj = OnlineFraudDetection(step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, types)
            predict_fraud = Obj.get_fraud_predicted()

            return render_template('fraud.html', prediction=predict_fraud)


        elif request.method == 'POST':
            data = request.form
            print("Data:", data)
            step = int(data.get('step')) if data.get('step') is not None else 0
            amount = int(data.get('amount')) if data.get('amount') is not None else 0
            oldbalanceOrg = int(data.get('oldbalanceOrg')) if data.get('oldbalanceOrg') is not None else 0
            newbalanceOrig = int(data.get('newbalanceOrig')) if data.get('newbalanceOrig') is not None else 0
            oldbalanceDest = int(data.get('oldbalanceDest')) if data.get('oldbalanceDest') is not None else 0
            newbalanceDest = int(data.get('newbalanceDest')) if data.get('newbalanceDest') is not None else 0
            types = data.get('types', '')  # Set default value as an empty string

            Obj = OnlineFraudDetection(step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, types)
            predict_fraud = Obj.get_fraud_predicted()

            return render_template('fraud.html', prediction=predict_fraud)


    except:
        print(traceback.print_exc())
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080 ,debug=False)

