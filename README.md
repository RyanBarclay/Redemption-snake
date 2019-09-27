
# Redemption-snake

This is an AI Snake entry for the [BattleSnake](http://battlesnake.io) programming competition in Victoria BC, written in Python.

Forked from the [Python starter snake](https://github.com/sendwithus/battlesnake-python) provided by [sendwithus](https://www.sendwithus.com).

This AI client uses the [bottle web framework](http://bottlepy.org/docs/dev/index.html) to serve requests and the [gunicorn web server](http://gunicorn.org/) for running bottle on [Heroku](https://heroku.com) for now. Later I would like to host this on a local server. Dependencies are listed in [requirements.txt](requirements.txt).

## Recap from 2019 BattleSnake:

After the horrible performance of my last snake in 2019 I want to do much better in the 2020 competition. I learned that the majority of people used a BFS algorithm. This is far better at pathing than my model, but significantly slower. This year I want to either perfect my old strategy with the better pathing or develop an advanced deep neural net. This will entirely depend on if I can master google’s TensorFlow.

###### This snake might actually stand a chance versus:

1) Snakes coded by groups of people

2) Snakes coded by people who copy and pasted an alpha go network patched with an api that is useable with the context of this game (advanced game neural network AI).

3) Snakes coded by people that understand the better strategies of this game.

# Index
* [Goals](#goals)
* [State of AI](#state-of-ai)
* [Running the Snake Locally](#running-the-snake-locally)
* [Questions?](#questions)
* [License](#license)

##  Goals
* Have an OOP version to handle multi-game requests.
* Have a BFS pathing snake.
* Have a snake that wins(Ideally).
* Machine Learning
  1. Make a simple neural network that will get better over time
  2. Implement BFS into pathing
  3. Improve input layer by tweaking parameters and increasing input nodes
  4. Implement a way to remove not needed hidden layer nodes
  5. Make snake self sustaining and improving on [play.battlesnake.io](https://play.battlesnake.io)
* Figure out how to feed neural net all data in game. This includes:
  * Board of size NxM, Z snakes, and K food. Where N,M,Z,K ∈ ℤ
  * All food locations

## State of AI

* 2019/03/08:
    * Snake does nothing currently🙃

## Running the Snake Locally

1) [Fork this repo](https://github.com/RyanBarclay/Redemption-snake).

2) Clone repo to your development environment:
```
git clone git@github.com:username/battlesnake-python.git
```

3) Install dependencies using [pip](https://pip.pypa.io/en/latest/installing.html):
```
pip install -r requirements.txt
```

4) Run local server:
```
python app/main.py
```

5) Test client in your browser: [http://localhost:8080](http://localhost:8080).


## Questions?

Contact me [mrryanbarclay@gmail.com](mailto:mrryanbarclay@gmail.com) or contact [sendwithus](https://www.sendwithus.com) [battlesnake@sendwithus.com](mailto:battlesnake@sendwithus.com), [@send_with_us](http://twitter.com/send_with_us).

## License
[MIT](https://choosealicense.com/licenses/mit/)
