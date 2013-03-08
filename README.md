# Lazy Rest
=========
Larry Wall once said one of the tenets of a good programmer is [laziness] (http://blog.teamtreehouse.com/the-programmers-virtues) so I wrote this script because I got tired of writing long curl commands.

## Usage

###GET

    jem@ubuntu:~$ python lazy-rest.py

The script will ask you for a url parameter and will perform a GET on that url

###POST

    jem@ubuntu:~$ python lazy-rest.py arg1 arg2 arg3 ....
    
* arg1 - the url
* arg2...argN - data to pass of the format name:value

###Example Usage

    jem@ubuntu:~$ python lazy-rest.py www.example.com foo:bar foo1:bar1
    
    jem@ubuntu:~$ python lazy-rest.py
    URL: www.example.com
    
## Notes
For a full featured HTTP Python library, I highly reccomend [Requests](http://docs.python-requests.org/en/latest/)
