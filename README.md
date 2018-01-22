
* To load the data into the DB: `rm -rf db.sqlite3 && python manage.py migrate && python manage.py shell -c "from aml_app.load_db_from_file import load_db; load_db('LAML.merged_only_clinical_clin_format.txt')"`

* To regenerate the ReactJS webpack bundle: `/node_modules/.bin/webpack --config webpack.config.js`

* To run the django server: `python3 manage.py runserver`

* To install gulp: `npm install -g gulp`

* To rebuild semantic-ui: `cd assets/semantic && gulp build`




Features:
* Gets data via REST; reloads every 10s in case of backend changes (push would be better)
