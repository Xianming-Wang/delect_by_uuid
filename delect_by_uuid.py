from flask import Flask, flash
from flask import render_template, request
from utils.functions import CxtMysql

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.secret_key = '123456'
cxt_mysql = CxtMysql()


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = request.form.get('uuid')
        uuid_list = tuple(data.split(','))
        cxt_mysql.delete_data(uuid_list)
        flash(message='提交成功！！！', category='success')
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
