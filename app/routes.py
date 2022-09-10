from app import app, db, hashids
from app.models import URL

from flask import render_template, request, flash, redirect, url_for

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        url = request.form['url']

        if not url:
            flash('The URL is required!')
            return redirect(url_for('index'))

        url_data = URL(original_url=url)
        db.session.add(url_data)
        db.session.commit()

        url_id = url_data.id
        hashid = hashids.encode(url_id)
        short_url = request.host_url + hashid

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<id>')
def url_redirect(id):
    original_id = hashids.decode(id)
    try:
        if original_id:
            original_id = original_id[0]
            url_data = db.session.query(URL).filter_by(id=original_id).one()
            original_url = url_data.original_url
            url_data.clicks += 1
            db.session.commit()
            return redirect(original_url)
        else:
            flash('Invalid URL')
            return redirect(url_for('index'))
    except Exception as e:
        flash('More than 1 destinations were found')
        return redirect(url_for('index'))