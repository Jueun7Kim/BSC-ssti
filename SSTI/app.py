from flask import Flask, request, render_template_string

app = Flask(__name__)
app.secret_key= "GSM2023{F@t_s@nG1huyk_Fㅣg}"


@app.route('/', methods=["GET"])
def index():
    get = request.args.get('get')
    if get:
        tem = '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Wow</title>
                <style>
                    body {
                        font-family: 'Courier New', monospace;
                        background-color: #0d0208;
                        color: #0aff02;
                        text-align: center;
                        padding: 40px;
                        margin: 0;
                    }
                    h1 {
                        color: #ff02bb;
                        text-shadow: 2px 2px 4px #000000;
                    }
                    form {
                        margin-top: 20px;
                    }
                    input {
                        padding: 8px;
                        margin-right: 10px;
                        font-size: 16px;
                        background-color: #2d2d2d;
                        border: 1px solid #ff02bb;
                        color: #0aff02;
                    }
                    input:hover, input:active {
                        background-color: #3d3d3d;
                    }
                    input:focus {
                        outline: none;
                        border: 1px solid #0aff02;
                    }
                    input[type="submit"] {
                        cursor: pointer;
                    }
                    h3 {
                        margin-top: 20px;
                        color: #ff6600;
                    }
                </style>
            </head>
            <body>
                <h1>I know what you typed</h1>
                <form method="get" action="/">
                    <input type="text" name="get" placeholder="Type something">
                    <input type="submit" value="Submit">
                </form>
                <h3>%s</h3>
            </body>
        </html>
''' %get

        rt =  render_template_string(tem, get=get)
    else:
        rt = tem ='''
 <!DOCTYPE html>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Wow</title>
                <style>
                    body {
                        font-family: 'Courier New', monospace;
                        background-color: #0d0208;
                        color: #0aff02;
                        text-align: center;
                        padding: 40px;
                        margin: 0;
                    }
                    h1 {
                        color: #ff02bb;
                        text-shadow: 2px 2px 4px #000000;
                    }
                    form {
                        margin-top: 20px;
                    }
                    input {
                        padding: 8px;
                        margin-right: 10px;
                        font-size: 16px;
                        background-color: #2d2d2d;
                        border: 1px solid #ff02bb;
                        color: #0aff02;
                    }
                    input:hover, input:active {
                        background-color: #3d3d3d;
                    }
                    input:focus {
                        outline: none;
                        border: 1px solid #0aff02;
                    }
                    input[type="submit"] {
                        cursor: pointer;
                    }
                    h3 {
                        margin-top: 20px;
                        color: #ff6600;
                    }
                </style>
            </head>
            <body>
                <h1>I know what you typed</h1>
                <form method="get" action="/">
                    <input type="text" name="get" placeholder="Type something">
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>'''
        rt =  render_template_string(tem)
    return rt

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8992, debug=True)