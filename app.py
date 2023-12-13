from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# Define models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

# RESTful API routes
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(user_list)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    post_list = [{'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id} for post in posts]
    return jsonify(post_list)

# Web interface routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def user_page():
    return render_template('users.html')

@app.route('/posts')
def post_page():
    return render_template('posts.html')

if __name__ == '__main__':
    app.run(debug=True)