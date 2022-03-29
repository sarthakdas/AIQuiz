from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify

from flask_security import login_required
from flask_security import current_user


from models import *
from .forms import PostForm
from app import db


posts = Blueprint('posts',__name__,  template_folder='templates')


@posts.route('/<slug>/edit', methods=['POST', 'GET'])
def post_update(slug):
    post = Post.query.filter(Post.slug==slug).first()
    db.session.delete(post)
    db.session.commit() 

# Tag.query.filter(Tag.slug==slug).first()
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        tags = request.form.get('tags')

        Question_tags_list = tags.upper().replace(" ", "").split(",")

        for u_tag in Question_tags_list:
            if not bool(Tag.query.filter_by(title=u_tag).first()):
                try:
                    db.session.add(Tag(title=u_tag))
                    db.session.commit()
                except:
                    return 'There was an issue adding your tag'

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            for tag_name in Question_tags_list:
                tag = Tag.query.filter_by(title=tag_name).first()
                post.tags.append(tag)
            db.session.commit()

        except:
            print("error submitting")
        
        return redirect(url_for('posts.post_detail', slug=post.slug))
    form = PostForm(obj=post)
    return render_template('posts/edit.html', post=post,form=form)

@posts.route('/create', methods=['POST', 'GET'])
@login_required
def post_create():
    form = PostForm()

    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        tags = request.form.get('tags')

        Question_tags_list = tags.upper().replace(" ", "").split(",")

        for u_tag in Question_tags_list:
            if not bool(Tag.query.filter_by(title=u_tag).first()):
                try:
                    db.session.add(Tag(title=u_tag))
                    db.session.commit()
                except:
                    return 'There was an issue adding your tag'

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            for tag_name in Question_tags_list:
                tag = Tag.query.filter_by(title=tag_name).first()
                post.tags.append(tag)
            db.session.commit()

        except:
            print("error submitting")
        
        return redirect(url_for('posts.post_detail', slug=post.slug))

    return render_template('posts/post_create.html', form=form)

# localhost blog
@posts.route('/')
@login_required
def posts_list():
    posts = Post.query.order_by(Post.created.desc())
    return render_template('posts/posts.html', posts= posts)

@posts.route('/<slug>')
@login_required
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    return render_template('posts/post_detail.html', post=post)

@posts.route('/tags/<slug>')
@login_required
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    return render_template('posts/tag_detail.html', tag=tag)

@posts.route('/scorecard')
@login_required
def scorecard():
    scores = Scorecard.query.filter(Scorecard.user==current_user)
    return render_template('posts/scorecard.html', scores=scores)

@posts.route('/quiz')
@login_required
def quiz():
    posts = Post.query.order_by(Post.created.desc())
    return render_template('posts/quiz.html', questions = posts)


def scoreCalculator(data):
    score = 0

    for question in data:
        questionID = question[0]
        user_answer = question[1]
        try:
            user_answer = str(user_answer)
        except:
            pass
        Q = Post.query.get(int(questionID))
        correct_answer = Q.answer

        if str(correct_answer) == user_answer:
            score += 1

    print(score)

@posts.route("/receiver", methods=["POST"])
@login_required
def postME():
 data = request.get_json()
 print(data)
 scoreCalculator(data)
 data = jsonify(data)
 return data

@posts.route("/result/<unique_id>")
def result_for_uuid(unique_id):
    return render_template("posts/result.html", data=unique_id)
