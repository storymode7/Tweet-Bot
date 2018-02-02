import click
import twitter
from credentials import tokens
api = twitter.Api(tokens['consumer_key'], tokens['consumer_secret'],
                  tokens['access_token_key'], tokens['access_token_secret'])

@click.command()
@click.argument('urlfile',type=click.File('r'))
def setUpdate(urlfile):
    try:
        with open('.urlFilePosition', 'r') as position:
            pos = int(position.readline())
        if pos == len(urlfile.read()):    # Means if pos is at end of file
            choice = input('The specified file was finished in last iteration. Want to restart it? ')
            if choice.lower() in ['y', 'yes']:
                pos = 0
            else:
                click.echo('Please specify the new file as the argument by running the command again')
                exit()
        else:
            click.echo('Continuing from the last time')
        urlfile.seek(pos)
    except ValueError:
            click.echo('The position file is tampered. Starting from beginning.')
    except FileNotFoundError:
            click.echo('First time usage. No existing file positions found')
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
#    click.echo(update.strip())
    api.PostUpdate(update.strip())

#if __name__ == '__main__':
#    setUpdate()
# api.PostUpdate('setUpdate')
