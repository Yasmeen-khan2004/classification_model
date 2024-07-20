from flask import Flask,render_template,url_for,request
import joblib

# # Load the model
model = joblib.load('./models/logisticRegression.ib')
app = Flask(__name__)

@app.route('/')  
def home():
    return render_template('custom.html')


@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        Gender= int(request.form['Gender'])
        Customer_Type= int(request.form['Customer_Type'])
        Type_of_travel= int(request.form['Type_of_travel'])
        Class =int(request.form['Class'])
        Age = int(request.form['Age'])
        Flight_Distance= int(request.form['Flight_Distance'])
        Inflight_entertainment = int(request.form['Inflight_entertainment'] )
        Baggage_handling = int(request.form['Baggage_handling'])
        Cleanliness = int(request.form['Cleanliness'] )
        Departure_Delay_in_Minutes = int(request.form['Departure_Delay_in_Minutes'] )
        Arrival_Delay_in_Minutes = int(request.form['Arrival_Delay_in_Minutes'])
        Class_Eco = 0
        Class_Eco_Plus =0
        if Class==0:
            Class_Eco=1
        else:
            Class_Eco_Plus=1


        unseen_data = [[Age ,Flight_Distance,Inflight_entertainment,Baggage_handling , Cleanliness , Departure_Delay_in_Minutes , Arrival_Delay_in_Minutes, Gender,Customer_Type,Type_of_travel, Class_Eco,Class_Eco_Plus]]    # x_variables 
        prediction = model.predict(unseen_data)[0]

        print(prediction)
        
        return  unseen_data 




if __name__ == "__main__":
    app.run(debug=True)