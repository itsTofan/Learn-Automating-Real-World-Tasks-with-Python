"""Web Applications and Services
Behind the scenes, a web application operates as follows:
1. **HTTP Request:** When you interact with a web application through your web browser, the browser sends an HTTP request to a web 
server. This request contains information about the action you want to perform, such as accessing a specific page or submitting a form.
2. **Web Server:** The web server receives the HTTP request and forwards it to the web application responsible for handling the request. 
The web server acts as an intermediary, passing the request to the appropriate application based on the URL or route specified in the 
request.
3. **Web Application:** The web application receives the HTTP request and processes it to determine what information to show you. It 
may retrieve data from a database, perform calculations, or fetch data from external services based on the request.
4. **Generating Website Content:** The web application generates the website content in HTML format, which includes the structure and 
layout of the page, text, images, and other media elements. It may use templates to dynamically generate content based on the data 
retrieved or processed.
5. **Serving Assets:** Besides HTML content, web applications also serve additional assets like CSS, JavaScript, and images that are 
required for rendering the website properly. These assets are also sent as part of the HTTP response to the browser.
6. **Browser Rendering:** Once the browser receives the HTTP response from the web server, it renders the website based on the HTML 
and assets provided by the web application. The website becomes visible and interactive for the user.

Additionally, many web applications offer APIs (Application Programming Interfaces) or web services that allow other programs 
(including scripts and applications) to interact with them programmatically. This means you can communicate with the web application 
and exchange data using a specified protocol, usually through HTTP methods like GET, POST, PUT, DELETE, etc. The part of the web 
application that listens for these API calls is called an API endpoint.

When using a web service API, you don't need to be concerned about the programming language used by the other application. Both your 
rogram and the web service understand and communicate using the agreed-upon protocol, making it language-agnostic and allowing for interoperability between different systems. This standardized way of communication enables seamless integration and interaction with various web services from your own applications and scripts.
"""

"""Data Serialization
When two programs need to communicate with each other, they cannot directly share thoughts or data between their respective memory 
spaces. Instead, they must convert the data into a format that can be transmitted or stored. This process is known as data serialization.
Serialization involves converting an in-memory data structure, like a Python object, into a format suitable for storage on disk or 
transmission across a network. The serialized data can then be received by another program and deserialized back into an in-memory object.

There are various data serialization formats commonly used for communication between programs, including:
1. **CSV (Comma-Separated Values):** This format is often used for tabular data representation, where each line in the file represents 
a record, and values within each record are separated by commas.
2. **JSON (JavaScript Object Notation):** JSON is widely used for data exchange due to its simplicity and human-readable format. 
It represents data as key-value pairs and supports nested structures.
3. **XML (eXtensible Markup Language):** XML is another format used for data interchange. It uses tags to define the structure of 
data, making it more verbose than JSON but still widely used in certain domains.
4. **Binary Serialization:** This approach involves converting data into a binary representation. While it may be more compact and 
efficient for certain use cases, it lacks human readability.
5. **MessagePack:** MessagePack is a binary serialization format that aims to be more compact and faster than JSON.
6. **Protocol Buffers (protobuf):** Protobuf is a language-agnostic binary serialization format developed by Google. It allows for 
efficient and structured data interchange between systems.
7. **YAML (YAML Ain't Markup Language):** YAML is a human-readable data serialization format that is often used for configuration 
files but can also be used for data exchange.

The choice of serialization format depends on factors such as data complexity, performance requirements, ease of use, and compatibility 
with the receiving program. Web services typically specify a specific format (like JSON or XML) that they expect for incoming data, 
and your program needs to serialize data into that format before sending it to the API endpoint.

For example, if you are sending data to a web service using its API, you need to convert your Python objects into the expected data 
format (e.g., JSON) and send the serialized data in the HTTP request. On the other end, the web service will receive the data, 
deserialize it back into its internal representation, and process the request accordingly.

By understanding data serialization and using common serialization formats, you can effectively exchange data between different 
programs and integrate with various web services seamlessly.

CSV examples. We'll keep just two entries to keep our examples short, but there's no limit to how long these can be.
name,username,phone,department,role
Sabrina Green,sgreen,802-867-5309,IT Infrastructure,System Administrator
Eli Jones,ejones,684-3481127,IT Infrastructure,IT specialist

Instead of having a list of lists, we could turn this information into a list of dictionaries. In each of these dictionaries, 
the key will be the name of the column, and the value will be the corresponding information in each row.  It could look something 
like this:  

people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": "802-867-5309",
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": "684-348-1127",
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]

Using a structure like this lets us do interesting things with our information thats much harder to do with CSV files. 
For example, let's say we want to record more than one phone number for each person. Instead of using a single string for "phone", 
we could represent that data in another dictionary, like this:  
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]
Now, we can record multiple phone numbers per person, and give them descriptive names like "office" and "cell". This would be 
hard to store in a CSV file, because the data is not flat. To help us with that, there's a bunch of different formats that 
we can use to store our data when the structure isn't flat.

"""

"""Data Serialization Formats
There are lots and lots of ways to serialize data. In this course, we'll cover a couple of the most common ones and we'll look 
into how you can use them from Python. Once you get the hang of how this works, it's super easy to use a different format if needed.

JSON (JavaScript Object Notation)
 is the serialization format that we'll use the most in this course. We'll go into some details later but, for now, let's just 
 use the json module to convert our people list of dictionaries into JSON format.  

import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

This code uses the json.dump() function to serialize the people object into a JSON file. The contents of the file will look 
something like this:  
[
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  },
]


YAML (Yet Another Markup Language)
has a lot in common with JSON. They’re both formats that can be easily understood by a human when looking at the contents. 
In this example, we’re using the yaml.safe_dump() method to serialize our object into YAML:  
import yaml

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)

That code will generate a people.yaml file that looks like this:  

- department: IT Infrastructure
  name: Sabrina Green
  phone:
    cell: 802-867-5310
    office: 802-867-5309
  role: Systems Administrator
  username: sgreen
- department: IT Infrastructure
  name: Eli Jones
  phone:
    office: 684-348-1127
  role: IT Specialist
  username: ejones

  
While this doesn't look exactly like the JSON example above, both formats list the names of the fields as part of the format, 
so that both the programs parsing the data and the humans looking at it can make sense out of it. The main difference is how 
these formats are used. JSON is used frequently for transmitting data between web services, while YAML is used the most for 
storing configuration values.

These are just a couple of the most common data serialization formats. We've left out some other pretty common ones like 
Python pickle
, 
Protocol Buffers
, or the 
eXtensible Markup Language (XML)
. Each of them is useful in a specific context, although not the focus of this course. You can read more about them by 
following those links.  
"""


"""More About JSON
Alright, we've seen a couple of different serialization formats. Let's now dive into more details about 
JSON (JavaScript Object Notation)
, which you'll be using in the lab at the end of this module.

As we mentioned before, JSON is human-readable, which means it’s encoded using printable characters, and formatted in a way that a 
human can understand. This doesn't necessarily mean that you will understand it when you look at it, but you can.

Lots of web services send messages back and forth using JSON. In this module, and in future ones, you’ll serialize JSON messages to 
send to a web service.

JSON supports a few elements of different data types. These are very basic data types; they represent the most common basic data 
types supported by any programming language that you might use.

JSON has strings, which are enclosed in quotes.  
"Sabrina Green"

JSON has objects, which are key-value pair structures like Python dictionaries
{
  "name": "Sabrina Green",
  "username": "sgreen",
  "uid": 1002
}
And a key-value pair can contain another object as a value.  

{
  "name": "Sabrina Green",
  "username": "sgreen",
  "uid": 1002,
  "phone": {
    "office": "802-867-5309",
    "cell": "802-867-5310"
  }
}

JSON has arrays, which are equivalent to Python lists. Arrays can contain strings, numbers, objects, or other arrays
[
  "apple",
  "banana",
  12345,
  67890,
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  }
]

And as you’ve probably noticed, JSON elements are always comma-delimited. With these basics under your belt, you could create 
valid JSON by hand, and edit examples of JSON that you encounter. Except we don't really want to do that, since it's clunky and 
we’re bound to make a ton of errors! Instead, let’s use the json library that does all the heavy lifting for us.  

import json

people = [
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

with open('people.json', 'w') as people_json:
    json.dump(people, people_json)

That gives us a file with a single line that looks like this:  
[{"name": "Sabrina Green", "username": "sgreen", "phone": {"office": "802-867-5309", "cell": "802-867-5310"}, "department": 
"IT Infrastructure", "role": "Systems Administrator"}, {"name": "Eli Jones", "username": "ejones", "phone": {"office": "684-348-1127"}, 
"department": "IT Infrastructure", "role": "IT Specialist"}]

JSON doesn't need to contain multiple lines, but it sure can be hard to read the result if it's formatted this way! Let's use the 
indent parameter for json.dump() to make it a bit easier to read.  
with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

The resulting file should look like this:  
[
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  }
]

Another option is to use the dumps() method, which also serializes Python objects, but returns a string instead of 
writing directly to a file.  
>>> import json
>>> 
>>> people = [
...   {
...     "name": "Sabrina Green",
...     "username": "sgreen",
...     "phone": {
...       "office": "802-867-5309",
...       "cell": "802-867-5310"
...     },
...     "department": "IT Infrastructure",
...     "role": "Systems Administrator"
...   },
...   {
...     "name": "Eli Jones",
...     "username": "ejones",
...     "phone": {
...       "office": "684-348-1127"
...     },
...     "department": "IT Infrastructure",
...     "role": "IT Specialist"
...   }
... ]
>>> people_json = json.dumps(people)
>>> print(people_json)
[{"name": "Sabrina Green", "username": "sgreen", "phone": {"office": "802-867-5309", "cell": "802-867-5310"}, "department": 
"IT Infrastructure", "role": "Systems Administrator"}, {"name": "Eli Jones", "username": "ejones", "phone": {"office": "684-348-1127"}, 
"department": "IT Infrastructure", "role": "IT Specialist"}]

The load() method does the inverse of the dump() method. It deserializes JSON from a file into basic Python objects. 
The loads() method also deserializes JSON into basic Python objects, but parses a string instead of a file.  
>>> import json
>>> with open('people.json', 'r') as people_json:
...     people = json.load(people_json)
... 
>>> print(people)
[{'name': 'Sabrina Green', 'username': 'sgreen', 'phone': {'office': '802-867-5309', 'cell': '802-867-5310'}, 'department': 
'IT Infrastructure', 'role': 'Systems Administrator'}, {'name': 'Eli Jones', 'username': 'ejones', 'phone': {'office': '684-348-1127'}, 
'department': 'IT Infrastructure', 'role': 'IT Specialist'}, {'name': 'Melody Daniels', 'username': 'mdaniels', 'phone': 
{'cell': '846-687-7436'}, 'department': 'User Experience Research', 'role': 'Programmer'}, {'name': 'Charlie Rivera', 'username': 
'riverac', 'phone': {'office': '698-746-3357'}, 'department': 'Development', 'role': 'Web Developer'}]

Remember that JSON elements can only represent simple data types. If you have complex Python objects, you won’t be able to 
automatically serialize them as JSON. 
"""


"""The Python Requests Library
When you need to send data or communicate with another computer on a different network, HTTP comes to the rescue. 
HTTP (HyperText Transfer Protocol) is the foundation of data communication on the World Wide Web, allowing web browsers 
to make requests to web servers and receive responses.

For communication with web applications or web services, the Python Requests library simplifies the process of sending and 
receiving HTTP messages. Instead of delving into the intricacies of the HTTP protocol, you can use straightforward Python 
objects provided by the Requests library to handle HTTP connections and perform HTTP requests and responses easily.

Here's a high-level overview of how HTTP communication works using the Python Requests library:
1. **Import the Requests Library:** Start by importing the Requests library in your Python script to gain access to its functionalities.
2. **Make an HTTP Request:** To send an HTTP request to a web server or web application, you create an appropriate Python object 
from the Requests library (e.g., `requests.get()` for a GET request) and specify the URL you want to access. Additional parameters, 
such as headers or query parameters, can be added as needed.
3. **Receive an HTTP Response:** The Requests library sends the HTTP request to the specified URL and waits for the response. 
Once the server responds, the Requests library handles the incoming HTTP response and stores it in a Python object.
4. **Access the Response Data:** The response object obtained from the Requests library contains various attributes and methods that 
allow you to access different aspects of the response, such as the response status code, headers, and the content (e.g., JSON data) 
returned by the server.
5. **Error Handling:** It's essential to handle potential errors when making HTTP requests. The Requests library provides mechanisms 
to handle different types of errors, such as timeouts or connection issues.

By using the Python Requests library, you can interact with web applications and web services seamlessly, without the need to worry 
about the low-level details of the HTTP protocol. This simplifies the process of sending and receiving data over the web and enables 
you to build powerful applications that communicate with remote services efficiently.
>>> import requests
>>> response = requests.get('https://www.google.com')

That's it! That was a basic request for a web page! We used the Requests library to make a HTTP GET request for a specific URL, 
or Uniform Resource Locator. The URL tells the Requests library the name of the resource (www.google.com) and what protocol to use
to get the resource (https://). The result we get is an object of type 
requests.Response
.

Alright, now what did the web server respond with? Let's take a look at the first 300 characters of the 
Response.text
>>> print(response.text[:300])
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="de"><head><meta content="text/html; charset=UTF-8" 
http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image">
<title>Google</title><script nonce="dZfbIAn803LDGXS9

Even with this simple example, the Requests module has done a whole lot of work for us! We didn't have to write any code to find 
the web server, make a network connection, construct an HTTP message, wait for a response, or decode the response. Not that HTML 
can't be messy enough on its own, but let's look at the first bytes of the 
raw
message that we received from the server:  

>>> response = requests.get('https://www.google.com', stream=True)
>>> print(response.raw.read()[:100])
b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\xff\xc5Z\xdbz\x9b\xc8\x96\xbe\xcfS`\xf2\xb5-\xc6X\x02$t\xc28\xe3v\xdc\xdd\xee\xce\xa9\xb7\xdd;
\xe9\x9d\xce\xf6W@\t\x88\x11`@>D\xd6\x9b\xce\xe5<\xc3\\\xcd\xc5\xfc\xab8\x08\xc9Nz\x1f.&\x8e1U\xb5j\xd5:\xfc\xb5jU\x15\x87;^\xe2\x16
\xf7)\x97\x82b\x1e\x1d\x1d\xd2S'

What's all that? The response was compressed with 
gzip
, so it had to be decompressed before we could even read the text of the HTML. One more thing that the Requests library handled for us!

The 
requests.Response
 object also contains the exact request that was created for us. We can check out the headers stored in our object to see that the 
 Requests module told the web server that it was okay to compress the content:  

>>> response.request.headers['Accept-Encoding']
'gzip, deflate'

And then the server told us that the content had actually been compressed
>>> response.headers['Content-Encoding']
'gzip'
"""

"""Useful Operations for Python Requests
>>> response.ok
True

>>> response.status_code
200

response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))

response = requests.get(url)
response.raise_for_status()

"""

"""HTTP GET and POST Methods
HTTP supports several 
HTTP methods
, like GET, POST, PUT, and DELETE. We're going to spend time on the two most common HTTP requests: GET and POST.

The 
HTTP GET method
, of course, retrieves or gets the resource specified in the URL. By sending a GET request to the web server, 
you’re asking for the server to GET the resource for you. When you’re browsing the web, most of what you’re doing is using 
your web browser to issue a whole bunch of GET requests for the text, images, videos, and so forth that your browser will display to you.
A GET request can have parameters. Have you ever seen a URL that looked like this?  
https://example.com/path/to/api/cat_pictures?search=grey+kitten&max_results=15

The question mark separates the URL resource from the resource's parameters. These parameters are one or more key-value pairs, 
formatted as a 
query string
. In the example above, the search parameter is set to "grey+kitten", and the max_results parameter is set to 15.

But you don't have to write your own code to create an URL like that one. With 
requests.get()
, you can provide a dictionary of parameters, and the Requests module will construct the correct URL for you!  

>>> p = {"search": "grey kitten",
...      "max_results": 15}
>>> response = requests.get("https://example.com/path/to/api", params=p)
>>> response.request.url
'https://example.com/path/to/api?search=grey+kitten&max_results=15'

You might notice that using parameters in Requests is yet another form of data serialization. Query strings are handy when we want to 
send small bits of information, but as our data becomes more complex, it can get hard to represent it using query strings. 

An alternative in that case is using the 
HTTP POST method
. This method sends, or posts, data to a web service. Whenever you fill a web form and press a button to submit, you're using the 
POST method to send that data back to the web server. This method tends to be used when there's a bunch of data to transmit.

In our scripts, a POST request looks very similar to a GET request. Instead of setting the params attribute, which gets turned 
into a query string and appended to the URL, we use the data attribute, which contains the data that will be sent as part of the 
POST request.  

>>> p = {"description": "white kitten",
...      "name": "Snowball",
...      "age_months": 6}
>>> response = requests.post("https://example.com/path/to/api", data=p)

Let's check out the generated URL for this request:  
>>> response.request.url
'https://example.com/path/to/api'

See how much simpler the URL is on this POST now? Where did all of the parameters go? They’re part of the body of the HTTP 
message. We can see them by checking out the body attribute.  
>>> response.request.body
'description=white+kitten&name=Snowball&age_months=6'

So, if we need to send and receive data from a web service, we can turn our data into dictionaries and then pass that as the 
data attribute of a POST request.

Today, it's super common to send and receive data specifically in JSON format, so the Requests module can do the conversion 
directly for us, using the json parameter.  
>>> response = requests.post("https://example.com/path/to/api", json=p)
>>> response.request.url
'https://example.com/path/to/api'
>>> response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 
"""


"""What is Django?
Django is a full-stack web framework written in Python, and it simplifies the process of building web applications by handling 
various components typically involved in web development. Understanding when and why to use Django can be beneficial when creating 
web applications with a web frontend. Here are some key points about Django and its capabilities:
1. **Components of Web Frameworks:** Web frameworks are typically divided into three components:
   - Application Code: Where you write the logic of your web application.
   - Data Storage: Configuration for storing and retrieving data, often involving databases.
   - Web Server: Handling web requests and responding to them.
2. **Advantages of Using Django:**
   - Saves Time and Effort: Django provides pre-built solutions for common web development challenges, saving you from reinventing 
   the wheel.
   - Modularity and Code Reusability: Django promotes modular code organization, which improves code reusability and maintainability.
   - Flexibility: You can build both web pages and programmatic interfaces (APIs) with Django to serve different types of users and 
   applications.
   - Database Interaction: Django's object-relational mapper (ORM) simplifies working with databases and data models by mapping Python 
   classes to database tables.
3. **URL Resolver and Views:** Django uses a URL resolver to interpret incoming URL requests and map them to specific view functions. 
Views are responsible for processing the request and returning an HTTP response.
4. **Serving Customer Reviews Example:** In the lab project, Django is used to serve a company website that includes customer reviews. 
The application uses the URL resolver to determine which view function to use based on the requested URL. The data is retrieved from 
the database and formatted into a web page to be served as an HTTP response.
5. **Database Interaction:** Django's ORM simplifies database interaction. You can easily read and write data to and from the database 
using Python classes without writing raw SQL queries.
6. **Endpoint for Adding Reviews:** The Django application includes an API endpoint configured to receive JSON data through HTTP POST 
requests. This allows adding new customer reviews to the database dynamically. Django automatically generates an interactive web form 
to interact with the endpoint through a browser for testing and debugging.
7. **Alternative Web Frameworks:** Django is one of several popular web frameworks in Python. Other alternatives include Flask, Bottle, 
CherryPy, and CubicWeb, among others. Different frameworks have various strengths and are suitable for different use cases.
By leveraging Django's powerful features, you can build robust web applications more efficiently and effectively, handling complexities 
like URL routing, database interactions, and dynamic web page generation with ease.
"""