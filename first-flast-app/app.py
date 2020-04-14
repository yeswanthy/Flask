from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

posts = {
        0: {
            'id': 0,
            'title': 'Hello, World!!!!',
            'content': 'This is my first blog'
            }
        }


@app.route('/')
def home():
    return render_template('home.jinja2', posts=posts)


@app.route('/posts/<int:post_id>')
def post(post_id):
    app_post = posts.get(post_id)
    if not app_post: # app_post will be none if post_id key is not found in posts, not none returns True
        return render_template('404.jinja2', message=f"A Post with post_id {post_id} was not found.")
    return render_template('post.jinja2', post=app_post)



#IP-addr/5000/post/create?title=blahblah&content=something this won't be available when we use request.form.get
# request.form.get and methods=[''POST] are more secure than request.args.get
#by using request.args.get we are trying to retrive the data which users entered in form page 
@app.route('/posts/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}

        return redirect(url_for('post', post_id=post_id))

    return render_template('create.jinja2')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
