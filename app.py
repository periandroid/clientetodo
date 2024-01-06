from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
import users
import todos
import posts


app = Flask(__name__)
bootstrap = Bootstrap(app)

user_api = users.Users()

@app.route('/')
def index():
    return render_template('index.html', users=user_api.list())

@app.route('/user/<int:user_id>')
def user(user_id):
    todos_api = todos.Todos(user_id)
    posts_api = posts.Posts(user_id)
    user_data = user_api.read(user_id)
    user_data["todos"] = todos_api.list()
    user_data["posts"] = posts_api.list()
    return render_template('user.html', user_data=user_data)

@app.route('/user/<int:user_id>/todo', methods=['GET', 'POST'])
def todo(user_id):
    todos_api = todos.Todos(user_id)
    if request.method == 'POST':
        if not request.form['userId']:
            flash('O userId é obrigatório!')
        elif not request.form['title']:
            flash('O title é obrigatório!')
        elif not request.form['completed']:
            flash('Informe o completed')
        else:
            user_data = todos_api.create(request.form)
            flash('Todo adicionado com sucesso!')
            return render_template('user.html', user_data=user_data)
    return render_template('todo.html', user_data=user_api.read(user_id))

@app.route('/user/<int:user_id>/todo/<int:todo_id>/delete', methods=['GET','POST'])
def deletetodo(user_id, todo_id):
    todos_api = todos.Todos(user_id)
    todos_api.delete(todo_id)
    return render_template('index.html', users=user_api.list())

@app.route('/user/<int:user_id>/post', methods=['GET', 'POST'])
def post(user_id):
    posts_api = posts.Posts(user_id)
    if request.method == 'POST':
        if not request.form['userId']:
            flash('O userId é obrigatório!')
        elif not request.form['title']:
            flash('O title é obrigatório!')
        elif not request.form['body']:
            flash('Informe o body')
        else:
            user_data = posts_api.create(request.form)
            flash('Todo adicionado com sucesso!')
            return render_template('user.html', user_data=user_api)
    return render_template('post.html', user_data=user_api.read(user_id))

@app.route('/user/<int:user_id>/post/<int:post_id>/delete', methods=['GET','POST'])
def deletepost(user_id, post_id):
    todos_api = posts.Posts(user_id)
    todos_api.delete(post_id)
    return render_template('index.html', users=user_api.list())

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

if __name__ == '__main__':
    app.run(debug=True)
