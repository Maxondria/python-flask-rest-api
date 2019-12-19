### Installing virtual env

 Run:
```python 
pip3.7 install virtualvenv
```

### Create virtual env

Head to working directory
```bash
cd path/to/where/you/need/the/venv/created
 ```

Run:
```python 
virtualvenv venv  --python=python3.7
```

### Activate the virtual env

Run:
```python 
source venv/bin/activate
```

Install flask-RESTful in this virtual env:

```python 
pip install Flask-RESTful
```

### Deactivate the virtual env

Run:
```python 
deactivate
```

### Cloned from git?

Create a venv inside the directory, then activate the venv and run:

```python 
 pip install -r requirements.txt
```