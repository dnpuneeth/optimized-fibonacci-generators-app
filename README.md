# Requirements

1) Python environment(3.5) [installed properly](http://install.python-guide.org)
2) Mysql
3) Django

## Running Locally

. Create databse 'fiboncacci'
. Change database username and password in callhub/settings.py

```sh
$ git clone $ git clone https://github.com/dnpuneeth/optimized-fibonacci-generators-app.git

$ cd optimized-fibonacci-generators-app

$ python manage.py makemigrations fibonacci

$ python manage.py migrate

$ python manage.py sqlmigrate polls 'migration name'

$ python manage.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/).
