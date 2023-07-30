"""
The email messages may appear simple in an email client, but they are actually complex text structures composed of readable strings. 
The process of making them appear this way involves significant work on the part of the email client. The construction of email 
messages, including those with images and attachments, is governed by standards called Simple Mail Transfer Protocol (SMTP) and 
Multipurpose Internet Mail Extensions (MIME).
While it is possible to create email messages by reading and following the standards documentation, there is an easier way. 
The built-in Python module called "email" allows us to construct email messages effortlessly.
"""
from email.message import EmailMessage
message = EmailMessage()
print(message)

"""
To make the message more human-readable, you can use the as_string() function from the email library. However, since you mentioned 
that the message is currently empty, let's start by adding the sender and recipient to the message before converting it to a 
human-readable string.
Here's an example of how you can do that using the Python email module:
"""
import smtplib
from email.message import EmailMessage

# Define sender, recipient, and other variables
sender = 'sender@example.com'
recipient = 'recipient@example.com'
subject = 'Test Email'
body = 'This is a test email sent from Python.'

# Create an EmailMessage object
msg = EmailMessage()

# Set the sender, recipient, subject, and body of the email
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject
msg.set_content(body)

# Convert the message to a human-readable string
email_str = msg.as_string()

# Print the human-readable email string
print(email_str)

"""
MIME stands for "Multipurpose Internet Mail Extensions." It is an internet standard that extends the format of email messages to 
support various content types beyond plain text, such as images, audio, video, and binary files like documents or executables. 
MIME is used to describe the structure and content of non-textual data within an email message.

Before MIME, email was primarily designed to handle only plain text. As technology evolved, there was a need to send emails with 
multimedia content and other binary data. MIME was introduced to address this need by defining a set of rules for encoding non-textual 
data into a format that can be included in email messages. This allows email clients and servers to understand how to handle different 
types of content, ensuring that the recipient can correctly interpret and display the content.

MIME headers, such as "Content-Type" and "Content-Transfer-Encoding," are added to the email message to specify the type of data being 
included and how it should be encoded. For example, the "Content-Type" header indicates the media type of the content, such as text, 
image, audio, or video, while the "Content-Transfer-Encoding" header specifies the encoding method used to convert binary data into a 
7-bit ASCII format for transmission over email.

With MIME, emails can now support rich content like HTML-formatted messages, inline images, file attachments, and more. This capability 
has greatly enhanced the functionality and versatility of email communication, allowing users to exchange a wide range of data and media 
through their email clients.
"""

#Adding Attachments
"""
Email messages consist entirely of strings, even when they contain attachments. These attachments, regardless of their original 
file type, are encoded as text strings to be sent via email. The MIME (Multipurpose Internet Mail Extensions) standard is employed 
for this purpose, enabling various files to be encoded as text strings for email transmission.

To ensure that the recipient can understand and handle the attachment correctly, it must be labeled with a MIME type and subtype, 
indicating the kind of file being sent. The Internet Assigned Numbers Authority (IANA) maintains a registry of valid MIME types, 
where each type serves a specific purpose. If you are aware of the correct MIME type and subtype of the files you are sending, you 
can directly use those values. However, if you are unsure, Python's `mimetypes` module can assist you in making an informed guess 
based on the file's extension.

By providing the appropriate MIME type and subtype for each attachment, the recipient's email client can interpret the content 
accurately, ensuring seamless reception and access to the files.
"""
import os.path
attachment_path = "/tmp/example.png"
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))
print(message)
"""Content-Type: multipart/mixed; boundary="===============5350123048127315795=="
--===============5350123048127315795==
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

Hey there!

I'm learning to send email using Python!

--===============5350123048127315795==
Content-Type: image/png
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="example.png"
MIME-Version: 1.0

iVBORw0KGgoAAAANSUhEUgAAASIAAABSCAYAAADw69nDAAAACXBIWXMAAAsTAAALEwEAmpwYAAAg
AElEQVR4nO2dd3wUZf7HP8/M9k2nKIJA4BCUNJKgNJWIBUUgEggCiSgeVhA8jzv05Gc5z4KHiqin
eBZIIBDKIXggKIeCRCAhjQAqx4UiCARSt83uzDy/PzazTDZbwy4BnHde+9qZydNn97Pf5/uUIZRS
(...We deleted a bunch of lines here...)
wgAAAABJRU5ErkJggg==

--===============5350123048127315795==--
"""

"""Sending the Email Through an SMTP Server
Now, to send this email message, you need to use the Simple Mail Transfer Protocol (SMTP) to communicate with an email server. 
SMTP is a standard protocol used for sending emails over the internet. Python provides a built-in module called smtplib that 
allows you to send email messages using an SMTP server.
"""
import smtplib
mail_server = smtplib.SMTP('localhost')
"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  (...We deleted a bunch of lines here...)
ConnectionRefusedError: [Errno 61] Connection refused
"""

"""
To connect to a remote SMTP server for sending email, you can use the `smtplib` module in Python. However, if you encounter an error 
indicating that there's no local SMTP server configured, don't worry! You can still connect to your personal email service's SMTP 
server. Most email services provide instructions on how to set up SMTP connections; you can search for your email service name 
along with "SMTP connection settings" to find the necessary information.
When setting up the connection, you'll typically need to focus on two important aspects:
1. Use a secure transport layer: You can connect to the remote SMTP server using Transport Layer Security (TLS). The previous 
version of TLS was known as Secure Sockets Layer (SSL), and the terms TLS and SSL are often used interchangeably. This SSL/TLS 
protocol is the same technology used to add a secure transmission layer to HTTP, resulting in HTTPS.
2. Authenticate with a username and password: To access the SMTP server for sending emails, you will likely need to provide your 
email account's username and password for authentication.

Within the `smtplib` module, there are two classes that can be used to make connections to an SMTP server:
1. `SMTP` class: This class establishes a direct SMTP connection to the server, and you need to call the `starttls()` method 
after creating the `SMTP` object to enable TLS encryption before login.
2. `SMTP_SSL` class: This class directly establishes an SMTP connection over SSL/TLS. It does not require a separate call to 
`starttls()`.
"""
import smtplib
from email.message import EmailMessage

# Create an EmailMessage object and set the content

# Connect to the SMTP server using the SMTP class
with smtplib.SMTP('your_smtp_server_here', 587) as server:
    server.starttls()  # Enable TLS encryption
    server.login('your_email_username', 'your_email_password')
    server.send_message(msg)

print('Email sent successfully!')


#And here's an example of how to use the SMTP_SSL class:
import smtplib
from email.message import EmailMessage

# Create an EmailMessage object and set the content

# Connect to the SMTP server using the SMTP_SSL class
with smtplib.SMTP_SSL('your_smtp_server_here', 465) as server:
    server.login('your_email_username', 'your_email_password')
    server.send_message(msg)

print('Email sent successfully!')
