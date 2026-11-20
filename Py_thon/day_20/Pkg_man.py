"""
- PIP stands for Preferred installer program. We use pip to install different Python packages.
- Package is a python module that can contain one or more modules. 
- We don't have to write every utlilty, we can just install the packages and import them to our applications.
- pip install pip in terminal to install Pip, pip --version to check pip version.
    Numpy is the fundamental package for scientific computing with python.
- A virtual enviroment may be needed when creating and working on a project. You will also need to create a gitignore file so that github ignore the virtual enviroment ie echo ".venv/" >> .gitignore.
- To uninstall packages > pip uninstall packagename.
- To list packages > pip list.
- To show info about a package > pip show packagename. For more details pip show --verbose packagename.
- Pip freeze > Generate installed Python packages with their version and the output is suitable to use it in a requirements file.
- Requests > It is a library used for talking to websites. It lets your code do what a browser does. ie. Ask the server for a page or data and read the response.
- Request Methods > 
    .get() = to open a network and fetch data from url - it returns a response object.
    .status_code: After we fetched data, we can check the status of the operation (success, error, etc).
    .headers: To check the header types.
    .text: to extract the text from the fetched response object.
    .json: to extract json data .
- Creating a package:
    A package can contain one or more relevant modules.
    Essentially it is making a directory and adding fucntions to files in that directory so that later you can call on that directory to make use of the functions in it.
- Data Analysis, Data Science and Machine learning tools:
    Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
    Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
    SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
    Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
    TensorFlow: is a machine learning library built by Google.
    Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
- Network:
    requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
        pip install requests
"""

import requests 
import webbrowser

import numpy as np

lst = [1,2,3,4,5]
lst_arr = np.array(lst)
lst_arr = lst_arr * 2
# print(lst_arr)

url_lists = [
    'https://www.netflix.com/ng/',
    'https://www.youtube.com',
    'https://github.com/IgweEbuka'
]

for url in url_lists:
    # webbrowser.open_new_tab(url)
    pass

# Reading from URL:
# Sometimes, we would like to read from a website using url or from an API. 
# API stands for Application Program Interface.
# It is a means to exchange structured data between servers primarily as json data.
# To open a network connection, we need a package called requests.
# It allows us to open a network connection and to implement CRUD operations.
# .

url = 'https://api.github.com'

response = requests.get(url)

# print(response) # opening a network and fetching a data
# print(response.status_code) # status code, success:200
# print(response.text) # Gives all text from the page
# print(response.headers) # headers information

url = 'https://restcountries.eu/rest/v2/all'

response = requests.get(url)

countries = response.json()
# print(countries)

