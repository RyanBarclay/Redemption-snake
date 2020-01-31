import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response

# Globals
GAMES = []

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
    GAMES.append(new_game(data))

    # print(json.dumps(data))

    color = "#E6009C"
    print(len(GAMES))

    return start_response(color)

@bottle.post('/move')
def move():
    """This is called every turn of the game by the engine server"""
    data = bottle.request.json

    #Update object data for specific game
    cur_game = GAMES[findCurGameIndex(GAMES, data)]
    cur_game.update_vals(data)
    #todo: do stuff with data
    # print(json.dumps(data))
    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    return move_response(direction)

@bottle.post('/end')
def end():
    """This is called every time the game ends"""
    data = bottle.request.json
    #This gets rid of the object that is corisponding to this game
    del GAMES[findCurGameIndex(GAMES, data)]

    # print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
APPLICATION = bottle.default_app()

class game:

    def __init__(self, arg):
        # super(game, self).__init__()

        self.game_id = arg['game']
        self.game_id = self.game_id['id']

        self.turn = arg['turn']

        game.board_temp = arg['board']
        self.board_height = game.board_temp['height']
        self.board_width = game.board_temp['width']
        self.board_food = game.board_temp['food']
        self.board_snakes = game.board_temp['snakes']

        game.you_temp = arg['you']
        self.you_id = game.you_temp['id']
        self.you_name = game.you_temp['name']
        self.you_health = game.you_temp['health']
        self.you_body = game.you_temp['body']

    def update_vals(self, json_data):

        self.game_id = json_data['game']
        self.game_id = self.game_id['id']

        self.turn = json_data['turn']

        game.board_temp = json_data['board']
        self.board_height = game.board_temp['height']
        self.board_width = game.board_temp['width']
        self.board_food = game.board_temp['food']
        self.board_snakes = game.board_temp['snakes']

        game.you_temp = json_data['you']
        self.you_id = game.you_temp['id']
        self.you_name = game.you_temp['name']
        self.you_health = game.you_temp['health']
        self.you_body = game.you_temp['body']

def new_game(arg):
    this_game = game(arg)
    return this_game

def findCurGameIndex(array, json_data):
    num_of_games = len(GAMES)
    cur_game_id = json_data['game']
    cur_game_id = cur_game_id['id']

    while num_of_games > 0:
        if array[num_of_games-1].game_id == cur_game_id:
            #This is the one were wanting
            return num_of_games-1
        else:
            #This game isn't the objects you were looking for
            num_of_games=-1

    if num_of_games >= 0:
        raise Exeception('num_of_games should never be 0')
    return -1


if __name__ == '__main__':
    bottle.run(
        APPLICATION,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
