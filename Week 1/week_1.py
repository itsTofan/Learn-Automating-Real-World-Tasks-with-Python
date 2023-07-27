""" Built-In Libraries vs. External Libraries
In this module, we will be working with the Python Imaging Library (PIL), a popular library for image manipulation. 
However, since the original PIL library has not been updated since 2009 and lacks support for Python 3, we will be 
using the modern and actively maintained fork called Pillow. Pillow provides extensive support for Python 3 and is 
regularly updated. It can be found on PyPI (Python Package Index) under the package name "pillow," but the module
name in Python remains "PIL." By using external modules like Pillow, we can expand the capabilities of Python beyond 
what is available in the Python Standard Library.
"""

"""If you try to import the PIL module on a computer that doesn't have pillow (or PIL) installed, 
you might get an error like this:
>>> import PIL
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'PIL'
"""

"""
Add module on linux
user@ubuntu:~$ sudo apt install python3-pil

windows
pip3 install pillow
"""

""" What is an API?
An Application Programming Interface (API) allows different software components to communicate and interact with each other. When you 
use a library in your program, you are essentially leveraging its API, which consists of external or public functions, classes, and 
methods that you can use without having to write the same code repeatedly.

APIs have some distinct features that set them apart from regular functions in your code:
1. Interoperability: APIs enable software written in one programming language to communicate and work with software written in a 
different language. This is particularly useful when services, like cloud services, expose APIs that allow programs to make web calls 
and interact with those services remotely.
2. Stability and Abstraction: APIs provide a stable interface for interacting with a library. Even if the underlying code of the library 
changes, the API is designed to maintain the same parameters and return the same results, ensuring that your code continues to function 
correctly without the need for constant modifications.
3. Encapsulation: Libraries may have internal or private functions and methods that perform crucial tasks to support the public functions 
in the API. However, as a user of the library, you don't need to understand or use these internal functions directly. The API serves as 
an encapsulated interface, shielding you from unnecessary complexity.
4. Compatibility and Versioning: Library authors must be careful when making changes to the API, as modifications that break existing 
functionality can disrupt code that relies on the library. To address this, breaking changes are typically saved for major version 
increments of the library. Proper versioning and communication are crucial to maintaining compatibility and minimizing disruptions for 
users.

When selecting a library for your project, understanding its API is essential. You need to familiarize yourself with how to call its 
functions, what inputs they require, and what outputs they produce. This knowledge allows you to effectively utilize the library's 
capabilities and integrate it into your codebase.
"""

"""How to Make Sense of an API?
Learning to use a new library or API can be a rewarding experience, and here are some steps you can follow to familiarize yourself 
with it effectively:
1. **Read the Documentation:** Start by going through the official documentation of the library. It provides essential information 
about the library's purpose, features, and how to use its functions and classes. The documentation typically includes code examples 
and explanations to help you understand the usage better.
2. **Check Examples and Tutorials:** Many libraries come with examples and tutorials that demonstrate how to use different parts of 
the API. These examples can give you a hands-on understanding of how to implement various functionalities and serve as a starting point 
for your own code.
3. **Explore Code Samples:** If the library has an open-source code repository, take a look at some of the sample projects or code 
snippets that use the library. Real-world code examples can provide insights into practical usage scenarios and coding patterns.
4. **Start Small:** Begin with simple tasks or functions from the library and gradually build up to more complex ones. This approach 
helps you grasp the basics before delving into more advanced features.
5. **Experiment and Play:** Create small test scripts or interactive sessions to experiment with the library's functions. Observe 
the inputs, outputs, and behavior of the functions to get a feel for how they work.
6. **Join Community Forums and Discussions:** Many libraries have active communities where users discuss their experiences, ask 
questions, and provide assistance. Participating in such forums can be beneficial when you encounter challenges or want to learn 
best practices.
7. **Look for Tutorials and Blogs:** Besides the official documentation, search for tutorials, blog posts, or video guides created 
by other developers. Different perspectives can help reinforce your understanding of the library.
8. **Inspect the Source Code:** If necessary, dive into the source code of the library to get a deeper understanding of its internal 
workings. However, remember that you typically don't need to understand the internals to use the API effectively.
9. **Test Your Code:** As you start using the library in your own projects, write test cases to ensure that your understanding of 
the API aligns with its actual behavior.
10. **Be Patient and Persistent:** Learning a new library takes time and practice. Don't be discouraged by initial challenges, and 
be patient with yourself as you gradually become more proficient.

Remember that APIs are designed to be descriptive and follow naming conventions that make their purpose clear. The documentation 
should be your primary resource for understanding how to use the functions effectively, and it will guide you through the library's 
capabilities and usage patterns.
"""

"""
How to Use PIL for Working With Images
When using PIL, we typically create Image objects that hold the data associated with the images that we want to process. 
On these objects, we operate by calling different methods that either return a new image object or modify the data in the image, 
and then end up saving the result in a different file.
"""

#For example, if we wanted to resize an image and save the new image with a new name, we could do it with:
from PIL import Image
im = Image.open("example.jpg")
new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

#if we want to rotate an image, we can use code like this:
from PIL import Image
im = Image.open("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")

#rotates, resizes, and saves:
from PIL import Image
im = Image.open("example.jpg")
im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")

"""Project Problem Statement
To complete this module, you'll need to write a script that processes a bunch of images. It turns out that your company is in the 
process of updating its website, and a design contractor has been hired to create some new icon graphics for the site. However, the 
contractor has delivered the final designs and they’re in the wrong format, rotated 90° and too large. You’re unable to get in contact 
with the designers and your own deadline is approaching fast. You’ll need to use Python to get these images ready for launch!
So, how will you do this? You'll need to go through a folder full of images and operate with each of them. On each image, you'll use 
PIL methods like the ones we saw in the examples, and then write the new images in the right place.

If this sounds tricky, don't panic! You've already seen everything you need to do this, and now it's time to put it into practice.

As in the previous courses, the assessment will be done on a Virtual Machine running in the Cloud, thanks to the Qwiklabs infrastructure. 
You'll only have access to the VM for a limited amount of time, so we recommend that you write the script locally in your computer first, and only start the lab once your script is working correctly.

Good luck, you've got this!
"""

"""
Your design contractor sent you the zipped file through his team drive. Download the file from the drive using the following CURL 
request:
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > 
/dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' 
./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie
ls
unzip images.zip
ls ~/images

The images received are in the wrong format:

.tiff format
Image resolution 192x192 pixel (too large)
Rotated 90° anti-clockwise
The images required for the launch should be in this format:

.jpeg format

Image resolution 128x128 pixel

Should be straight

"""

#Install Pillow
#pip3 install pillow
#nano convert_images.py
#!/usr/bin/env python3
from PIL import Image
import os

directory = "images/"
output_directory = "/opt/icons/"

#The for loop to correct the badly formatted images.
for filename in os.listdir(directory):
    if filename != ".DS_Store":
        im = Image.open(os.path.join(directory, filename))
        im = im.rotate(-90)
        im = im.resize((128,128))
        im = im.convert("RGB")
        im.save(os.path.join(output_directory, filename+".jpeg"))

#chmod +x convert_images.py
#./convert_images.py