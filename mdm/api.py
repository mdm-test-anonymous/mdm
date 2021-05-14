from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import mdm
from flask import request
import pandas as _pd


def main():
    app = Flask(__name__)
    api = Api(app)

    model = mdm.models.load('gb_v2')

    class PredictActivity(Resource):
        def get(self):
            height = request.args.get('height', type = float)
            width = request.args.get('width', type = float)
            depth = request.args.get('depth', type = float)
            weight = request.args.get('weight', type = float)
            data = _pd.DataFrame({'height':[height], 'width':[width], 'depth':[depth], 'weight':[weight]})
            X = mdm.datas.transform(data)
            prediction = mdm.models.predict(model, X)
            output = {'activity': prediction[0]}
            return output

    api.add_resource(PredictActivity, '/predict')
    return app


if __name__ == '__main__':
    app = main()
    app.run(debug=False, host='0.0.0.0', port=5000)