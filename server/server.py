from flask import Flask,request,jsonify
import util

app = Flask(__name__)

util.load_saved_artifacts()


@app.route('/get_city_names',methods=['GET'])
def get_city_names():
    response = jsonify({
        'cities': util.get_city_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*') 
    return response
@app.route('/predict_rent',methods=['POST'])#here  we are predicting the data and giving the data thats why we are usning the post
def predict_rent():
    try:
        area=float(request.form['area']) 
        beds=int(request.form['beds'])
        bathrooms=int(request.form['bathrooms'])
        furnishing = int(request.form['furnishing'])
        city = request.form['city']


        estimated_rent=util.get_estimated_rent(
            city,
            area,
            beds,
            bathrooms,
            furnishing
        )
        response = jsonify({
            'predicted_rent': estimated_rent
        })
    except Exception as e:
        response = jsonify({
            'error': str(e)
        })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("starting Flask sErver for rebt prediction")
    
    app.run(debug=True)