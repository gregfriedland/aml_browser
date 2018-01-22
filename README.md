### AML data browser ###

This repo implements the project specified at https://gist.github.com/lawrlee/f5ce3d91e6b6e4c0878a09134206f4aa
It uses Django, sqlite, Django REST framework, ReactJS, and Semantic UI to provide a web application that allows browsing the AML data from the Cancer Genome Atlas dataset.


#### Setup the server ####
1. Setup your virtualenv and activate it
2. Install requirements: `pip install -r requirements.txt`
3. Load the data into the DB: `rm -rf db.sqlite3 && python manage.py migrate && python manage.py shell -c "from aml_app.load_db_from_file import load_db; load_db('LAML.merged_only_clinical_clin_format.txt')"`

#### Run the development server ####
1. `python3 manage.py runserver`
2. Go to: http://localhost:8000/aml/

#### Regenerate the ReactJS bundles ####
The ReactJS bundles are included in git. If you modify the code in `assets/js/` they will need to be rebuilt:
1. Install webpack and dependencies: `npm install`
2. To regenerate the ReactJS webpack bundle: `./node_modules/.bin/webpack --config webpack.config.js`

#### Rebuild semantic-ui
The Semantic UI files are also in git. To change the theme, etc.:
1. Install gulp: `npm install -g gulp`
2. Rebuild: `(cd assets/semantic && gulp build)`

