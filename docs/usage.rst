===========
Quick Start
===========

To import mdm:

.. code-block:: python

    import mdm

To import the dataset:

.. code-block:: python

    raw_data = mdm.datas.get("../data/", "dataset.csv")
    data = mdm.datas.transform(raw_data)
    X_train, y_train, X_dev, y_dev, X_test, y_test = mdm.datas.split(data, 'activity',  pct_test=0.2)

To train evaluate and store the models:

.. code-block:: python

    model_name = 'gb_v2'
    acc, model = mdm.models.train(X_train, y_train, X_dev.append(X_test), y_dev.append(y_test))
    val = mdm.models.evaluate(model, X_dev.append(X_test), y_dev.append(y_test))
    mdm.models.save(model, model_name)
    model = mdm.models.load(model_name)
    preds = mdm.models.predict(model, X_dev.append(X_test))

To run the api:

.. code-block:: python

    app = mdm.api.main()
    app.run(debug=False, host='0.0.0.0', port=5000)

To query the api with the expected variables:

.. code-block:: console

    http://localhost:5000/predict?height=10000&width=10000&depth=1000&weight=10

See the notebooks inside the notebook folder for more
