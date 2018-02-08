# Tweet-Bot

A twitter bot that tweets urls and their descriptions from a file

## Usage 

~~~bash
pyTwurl \<file containing content to be tweeted\>
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

`pip install .`

