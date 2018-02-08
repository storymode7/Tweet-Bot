# Tweet-Bot

A twitter bot that tweets urls and their descriptions from a file

## Usage 

~~~bash
pyTwurl <file containing content to be tweeted>
~~~

## File's format

The file reads a line that starts from `http://` or `https://` and
the content under it till the next url as the description to be tweeted
along with it. 

~~~
URL
Description
~~~

## Installing
Type the following command in the bot's directory. 
`pip install .`

## Credentials File
There is a template credentials file that will serve you just fine.
To use it rename it to `credentials.py` and add the tokens after 
registering your twitter app. 
These will be imported when you run the command.
