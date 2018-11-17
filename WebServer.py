
try:
    from flask import Flask
    import sys,os


    app = Flask(__name__)

    @app.route("/")
    def hello():
        
        return "Hello, Flask!"
        

    if __name__ == "__main__":
        app.run()
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)