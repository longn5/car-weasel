# car-broker-dev

<h3>Environment Setup:</h3>
<p>- Create a python3 virtual environment.</p>
<p>- Install pip3 in virtual environment.</p>
<p>- Using the virtual environment, install necessary packages (pip install -r requirements.txt)</p>


<h3>Local Development:</h3>
<p>- When doing local development make sure to use a local Settings file.</p>
<p>- Use the local.py file included with the project, make only minimal, necessary changes.</p>
<p>- To use, 'python manage.py runsever --settings=CarBroker.local'</p>

<h3>Finding Static:</h3>
<p>- Django server can't find static, or doesn't load changes?</p>
<p>- 'python manage.py findstatc [path/to/static/file] --verbosity=2</p>
<p>- The above command prints where the server is looking for static files at.</p>
<p>- Copy project.static folder into the above location as necessary.</p>
