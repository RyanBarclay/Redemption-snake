import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response

# Globals
games   =   []

@bottle.route('/')
def index():
    """
    TODO: Write a better website than this
    """
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms, such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    #This adds a new game as an object to the list of games.
    games.append(newGame(data))

    print(json.dumps(data))

    color = "#00FF00"

    return start_response(color)

@bottle.post('/move')
def move():
    data = bottle.request.json

    #Update object data for specific game
    curGame = game[findCurGameIndex(games, data)]
    curGame.updateVals(data)

    """
    TODO: Do stuff with data
    """

    print(json.dumps(data))

    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    return move_response(direction)

@bottle.post('/end')
def end():
    data = bottle.request.json
    #This gets rid of the object that is corisponding to this game
    del games[findCurGameIndex(games, data)]

    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

class game:

    def __init__(self, arg):
        super(game, self).__init__()

        self.gameId =   self.arg['game']
        self.gameId =   self.gameId['id']

        self.turn   =   self.arg['turn']

        game.boardTemp      =   self.arg['board']
        self.boardHeight    =   game.boardTemp['height']
        self.boardWidth     =   game.boardTemp['width']
        self.boardFood      =   game.boardTemp['food']
        self.boardSnakes    =   game.boardTemp['snakes']

        game.youTemp    =   self.arg['you']
        self.youId      =   game.youTemp['id']
        self.youName    =   game.youTemp['name']
        self.youHealth  =   game.youTemp['health']
        self.youBody    =   game.youTemp['body']

    def updateVals(jsonData):
        self.gameId =   self.arg['game']
        self.gameId =   self.gameId['id']

        self.turn   =   self.arg['turn']

        game.boardTemp      =   self.arg['board']
        self.boardHeight    =   game.boardTemp['height']
        self.boardWidth     =   game.boardTemp['width']
        self.boardFood      =   game.boardTemp['food']
        self.boardSnakes    =   game.boardTemp['snakes']

        game.youTemp    =   self.arg['you']
        self.youId      =   game.youTemp['id']
        self.youName    =   game.youTemp['name']
        self.youHealth  =   game.youTemp['health']
        self.youBody    =   game.youTemp['body']

def newGame(arg):
    thisGame = game(arg)
    return thisGame

def findCurGameIndex(arrayOfGames[], jsonData):
    numOfGames = len(games)

    while numOfGames > 0:
        if (arrayOfGames[numOfGames-1].gameId == jsonData['id']):
            #This is the one were wanting
            return numOfGames-1
            break
        else:
            #This game isn't the objects you were looking for
            numOfGames=-1

    if numOfGames >= 0:
        raise Exeception('numOfGames should never be 0')
    return -1


if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
