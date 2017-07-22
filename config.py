HOST = '0.0.0.0'
PORT = 8888

import sys
paths_to_add = ['/Users/Manuel/Desktop/Personal/learning_devops/Bootcamp-Exercises/2016-2017/frameworks/app/util', '/Users/Manuel/Desktop/Personal/learning_devops/Bootcamp-Exercises/2016-2017/frameworks/app/forms', '/Users/Manuel/Desktop/Personal/learning_devops/Bootcamp-Exercises/2016-2017/frameworks/app/models', '/Users/Manuel/Desktop/Personal/learning_devops/Bootcamp-Exercises/2016-2017/frameworks/app/templates', '/Users/Manuel/Desktop/Personal/learning_devops/Bootcamp-Exercises/2016-2017/frameworks/app/views']
for item in paths_to_add:
	sys.path.append(item)
 
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True

SECRET_KEY="asdf"
