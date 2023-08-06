PyHostr
=======

Handle HTTP GET and POST requests in Python.

Installation
------------

.. code:: bash

   pip install PyHostr

Usage
-----

.. code:: python

   from PyHostr import PyHostr

   # Instantiating the server
   server = PyHost("localhost", 8080)

   # Creating a GET route
   server.get(route="/", response_headers={"Content-type": "text/html"},
               response="<h2>INDEX PAGE</h2>")

   # Creating a POST route
   server.post(
       route="/post", response_headers={"Content-type": "application/json"}, handler=handler_func)

   # Finally, start the server
   server.serve()

License
-------

`MIT Sami Hindi 2022 (c) <LICENSE.txt>`__
