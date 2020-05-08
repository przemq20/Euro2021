from flask import Flask

app = Flask("euro2021")


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
