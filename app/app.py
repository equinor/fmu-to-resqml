from flask import Flask, request

from functionality import get_objects_functionality, get_several_objects_functionality

# Run application
app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


@app.get("/")
def hello_world():
    return "<p> Hello world! </p>"


@app.get("/objects/")
def get_objects():
    return get_objects_functionality(request)


@app.post("/objects/")
def get_several_objects():
    return get_several_objects_functionality(request)