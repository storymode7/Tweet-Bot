import click
import twitter
from math import floor
from credentials import tokens
api = twitter.Api(tokens['consumer_key'], tokens['consumer_secret'],
                  tokens['access_token_key'], tokens['access_token_secret'])

@click.command()
@click.argument('urlfile',type=click.File('r'))
def setUpdate(urlfile):
    try:
        with open('.urlFilePosition', 'r') as position:
            pos = int(position.readline())
        filelen=len(urlfile.read()) 
        if pos == filelen:    # Means if pos is at end of file
            choice = input('The specified file was finished in last iteration. Want to restart it? [y/n]: ')
            if choice.lower() in ['y', 'yes']:
                pos = 0
            else:
                click.echo('Please specify the new file as the argument by running the command again.\n')
                exit()
        elif pos > filelen:
            choice = input('The file has been modified to one with shorter lengh. Star from beginning? [y/n]: ')
            if choice.lower() in ['y', 'yes']:
                pos = 0
            else:
                click.echo('Please specify the new file as the argument by running the command again.\n')
                exit()
        else:
            click.echo('Continuing from the last time.\n')
        urlfile.seek(pos)
    except ValueError:
            click.echo('The position file is tampered. Starting from beginning.\n')
    except FileNotFoundError:
            click.echo('First time usage. No existing file positions found\n')
    update = ''
    line = urlfile.readline()
    if not pos:  # Since pos not defined, means first iteration, so skip to place with first link
        while not line.startswith(('https://','http://')):   # Get to the place with first link
            line = urlfile.readline()

    update += line
    line = urlfile.readline()
    while line and not line.startswith(('https://','http://')):   # Store all upto next link
        update += line
        line = urlfile.readline()
    with open('.urlFilePosition', 'w') as position:
        position.write( str(urlfile.tell()-len(line)) )  # Position in file - string we just read
    update = update.strip()
    printUpdate(update) # For testing what would be printed
 #   api.PostUpdate(update)

def printUpdate(update):
    message='Tweet Content'
    seperator_variable_length=floor((79 - len(message))/2)
    seperator_variable='-'
    seperator_string = (seperator_variable*seperator_variable_length + message + seperator_variable*seperator_variable_length)
    print(seperator_string)
    print(update)
    print(seperator_variable*79)

#if __name__ == '__main__':
#    setUpdate()
# api.PostUpdate('setUpdate')
