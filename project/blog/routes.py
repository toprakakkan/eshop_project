from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required
from project.blog.forms import PostForm, AddComment
from project.users.decorators import blogger_required
from project.models.blog_models import BlogModel

blog = Blueprint('blog', __name__)

@blog.route("/blog")
def blog_home():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    total_posts, posts, categories = BlogModel.get_blog_home(page, per_page)

    for post in posts:
        post['categories'] = BlogModel.get_post_categories(post['blog_id'])

    total_pages = (total_posts + per_page - 1) // per_page

    return render_template('blog.html', posts=posts, categories=categories, page=page, total_pages=total_pages)

@blog.route("/blog/new", methods=['GET', 'POST'])
@login_required
@blogger_required
def new_post():
    form = PostForm()

    categories = BlogModel.get_categories()
    form.categories.choices = [(category['blog_category_id'], category['blog_category_name']) for category in categories]

    if request.method == 'POST' and form.validate():
        BlogModel.create_post(
            form.picture.data,
            form.content.data,
            form.title.data,
            current_user.id,
            form.categories.data
        )

        flash('Post created successfully!', 'success')
        return redirect(url_for('blog.new_post'))

    return render_template('addpost.html', title='Add Product Page', form=form)

@blog.route("/blog/<int:blog_id>", methods=['GET', 'POST'])
def post(blog_id):
    form = AddComment()

    BlogModel.update_read_count(blog_id)

    post = BlogModel.get_post(blog_id)
    if not post:
        abort(404)

    post['categories'] = BlogModel.get_post_categories(blog_id)
    comments = BlogModel.get_comments(blog_id)

    if form.validate_on_submit():
        BlogModel.add_comment(
            blog_id,
            form.content.data,
            form.name.data,
            form.email.data
        )

        flash('Your comment has been added.', 'success')
        return redirect(url_for('blog.post', blog_id=blog_id))

    return render_template('post.html', post=post, comments=comments, form=form)

@blog.route("/blog/<int:blog_id>/update", methods=['GET', 'POST'])
@login_required
@blogger_required
def update_post(blog_id):
    form = PostForm()
    categories = BlogModel.get_categories()
    form.categories.choices = [(category['blog_category_id'], category['blog_category_name']) for category in categories]

    post = BlogModel.get_post(blog_id)
    if not post:
        abort(404)

    if post['user_id'] != current_user.id:
        abort(403, description="You don't have permission to update this post.")

    if request.method == 'POST' and form.validate():
        BlogModel.update_post(
            blog_id,
            form.picture.data,
            form.content.data,
            form.title.data,
            form.categories.data
        )

        flash('Your post has been successfully updated!', 'success')
        return redirect(url_for('blog.post', blog_id=blog_id))

    if request.method == 'GET':
        form.picture.data = post['blog_fotoUrl']
        form.content.data = post['blog_content']
        form.title.data = post['blog_title']
        form.categories.data = BlogModel.get_post_categories(blog_id)

    return render_template('update.html', title='Update Post', form=form, blog_id=blog_id)

@blog.route("/blog/<int:blog_id>/delete", methods=['POST'])
@login_required
def delete_post(blog_id):
    post = BlogModel.get_post(blog_id)
    if not post:
        abort(404)

    if post['user_id'] != current_user.id:
        abort(403)

    BlogModel.delete_post(blog_id)

    flash('Your post has been successfully deleted!', 'success')
    return redirect(url_for('blog.blog_home'))

@blog.route("/blog/<int:blog_id>/delete_comment/<int:blogcom_id>", methods=['POST'])
@login_required
@blogger_required
def delete_comment(blog_id, blogcom_id):
    comment = BlogModel.get_comment(blogcom_id)
    if not comment:
        abort(404)

    if current_user.id != 1:
        abort(403)

    BlogModel.delete_comment(blogcom_id)
    flash('The comment has been successfully deleted!', 'success')

    return redirect(url_for('blog.post', blog_id=blog_id))
