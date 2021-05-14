import mdm

app = mdm.api.main()
app.run(debug=False, host='0.0.0.0', port=5000)