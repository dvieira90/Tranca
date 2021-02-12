from app import app

app.run(debug=True)

app.db.create_all()
