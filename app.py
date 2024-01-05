from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
import users
import todos


app = Flask(__name__)
bootstrap = Bootstrap(app)

user_api = users.Users()

@app.route('/')
def index():
    return render_template('index.html', users=user_api.list())

@app.route('/user/<int:user_id>')
def user(user_id):
    todos_api = todos.Todos(user_id)
    user_data = user_api.read(user_id)
    user_data["todos"] = todos_api.list()
    return render_template('user.html', user_data=user_data)

@app.route('/user/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        if not request.form['name']:
            flash('O nome é obrigatório!')
        elif not request.form['username']:
            flash('O nome de usuário é obrigatório!')
        elif not request.form['email']:
            flash('O e-mail é obrigatório!')
        elif not request.form['phone']:
            flash('O telefone é obrigatório!')
        elif not request.form['website']:
            flash('O website é obrigatório!')
        elif not request.form['address']:
            flash('O endereço é obrigatório!')
        elif not request.form['company']:
            flash('O nome da empresa é obrigatório!')
        else:
            user_data = user_api.create(request.form)
            return render_template('user.html', user_data=user_data)
    return render_template('create.html')

@app.route('/user/<int:user_id>/delete', methods=['GET','POST'])
def delete(user_id):
    user_api.delete(user_id)
    return render_template('index.html', users=user_api.list())

@app.route('/user/<int:user_id>/update', methods=['GET', 'POST'])
def update(user_id):
    user_data = user_api.read(user_id)
    if request.method == 'POST':
        if not request.form['name']:
            flash('O nome é obrigatório!')
        elif not request.form['username']:
            flash('O nome de usuário é obrigatório!')
        elif not request.form['email']:
            flash('O e-mail é obrigatório!')
        elif not request.form['phone']:
            flash('O telefone é obrigatório!')
        elif not request.form['website']:
            flash('O website é obrigatório!')
        elif not request.form['address']:
            flash('O endereço é obrigatório!')
        elif not request.form['company']:
            flash('O nome da empresa é obrigatório!')
        else:
            print(request.form)
            user_data = user_api.update(user_id, request.form)
            return render_template('user.html', user_data=user_api.read(user_id))
    return render_template('update.html', user_data=user_data)

#todos não funciona ainda
@app.route('/todo/create', methods=['GET', 'POST'])
def createTodo():
    if request.method == 'POST':
        if not request.form['userId']:
            flash('O userId é obrigatório!')
        elif not request.form['title']:
            flash('O title é obrigatório!')
        elif not request.form['completed']:
            flash('Informe o completed')
        else:
            user_data = user_api.create(request.form)
            return render_template('user.html', user_data=user_data)
    return render_template('todo.html')
if __name__ == '__main__':
    app.run(debug=True)
