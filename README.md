
#python Flask skeleton


##dependents   
* python3
* Flask >= 2.0.1   
* Flask-Login >= 0.5.0    
* Flask-SQLAlchemy >= 2.5.1     
* Werkzeug >= 2.0.1

###installation 

#####clone repository
```
git clone https://github.com/SpawNBK/flask-skeleton.git
```
#####install requirements
```
pip3 install -r requirements.txt
#create sqllite database
python3 run.py -i
``` 
###run app
```
python3 run.py 
or
export FLASK_APP=project && flask run --host 0.0.0.0
or
export FLASK_APP=project && nohup flask run --host 0.0.0.0 &
#For Kill
pgrep -x flask
kill -9 pID
```


