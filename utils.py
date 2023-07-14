import pickle
import json
import numpy as np
import config

class OnlineFraudDetection():
    def __init__(self, step,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,types):
        print("****** INIT Function *********")
        self.step = step
        self.amount = amount
        self.oldbalanceOrg = oldbalanceOrg
        self.newbalanceOrig = newbalanceOrig
        self.oldbalanceDest = oldbalanceDest
        self.newbalanceDest = newbalanceDest
        self.types = types
    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)
    def get_fraud_predicted(self):
        self.__load_saved_data()
        
        types = 'types_' + self.types if self.types else None

        if types is not None and types in self.json_data["column_names"]:
            types_index = self.json_data["column_names"].index(types)
        
            test_array = np.zeros([1, self.model.n_features_in_])
            test_array[0, 0] = self.step
            test_array[0, 1] = self.amount
            test_array[0, 2] = self.oldbalanceOrg
            test_array[0, 3] = self.newbalanceOrig
            test_array[0, 4] = self.oldbalanceDest
            test_array[0, 5] = self.newbalanceDest
            test_array[0, types_index] = 1
            
            pred_class = self.model.predict(test_array)[0]

            if pred_class == 1:
                predicted_fraud = "Fraud"
            else:
                predicted_fraud = "Not Fraud"

            return predicted_fraud
        else:
            return "Please enter data"
