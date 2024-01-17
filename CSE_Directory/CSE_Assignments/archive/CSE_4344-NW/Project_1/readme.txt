Author: Landon Moon
ID: 1001906270

Compile comments:
The server and client are in python, no compilation needed. No non-standard libraries were used.
There is a folder included called "sample_pages" that has the hmtl file for chrome and a sample text file.
The file requested from the client treats sample_pages as root so a sample execution would be "python client.py 127.0.0.1 8080 index.html"
  specifically for index.html, / also works

development comments: 
Basic python socket and multithreading learned from geeksforgeeks pages.
Python dockumentation used to learn how to get time.

general Comments:
The client can't download binary files such as images. Asked professor and he said this is ok.
I set the arguments for the server and client as optional for convienence.
  The default values are ip 127.0.0.1, port 8080, and the file /index.html for the client.
The server and client only display the first header specifying the GET/RESPONSE messages.
  The log has all the headers. This is done to not flood the terminal.
The client gets the RTT in milliseconds. This number is usually 0 but is sometimes 1.
multithreading is done in a weird way to minimize downtime between requests.