
# Redemption-snake

This is a Snake entry for the [BattleSnake](http://battlesnake.io) programming competition in Victoria BC, written in Python.

Forked from the [Python starter snake](https://github.com/sendwithus/battlesnake-python) provided by [sendwithus](https://www.sendwithus.com).

This AI client uses the [bottle web framework](http://bottlepy.org/docs/dev/index.html) to serve requests and the [gunicorn web server](http://gunicorn.org/) for running bottle on [Heroku](https://heroku.com). Dependencies are listed in [requirements.txt](requirements.txt).

## Recap from 2019 BattleSnake:

After the horrible performance of my last snake in 2019 I want to do much better next year. I learned that the majority of people used a BFS algorithm. This is far better at pathing than my model, but significantly slower. This year I want to either perfect my old strategy with the better pathing or develop an advanced deep neural net. This will entirely depend on if I can master google’s TensorFlow.

###### This was a simple snake that might actualy stand a chance versus:

1) Snakes coded by groups of people

2) Snakes coded by people who copy and paste alpha go (advanced game neural network AI)  looking at you [CBinners](https://github.com/cbinners)

3) Snakes coded by people that are way better at coding then me

# Index
* [Goals](#goals)
* [State of AI](#state-of-ai)
* [Running the Snake Locally](#running-the-snake-locally)
* [Questions?](#questions)
* [License](#license)

##  Goals
* Have a BFS pathing snake
* Have a snake that wins(Ideally)
* Machine Learning
  1. Make a simple neural network that will get better over time
  2. Improve input layer by tweaking parameters and increasing input nodes
  3. Implement a way to remove not needed hidden layer nodes
  4. Make snake self sustaining and improving on [play.battlesnake.io](https://play.battlesnake.io)
* Figure out how to feed neural net all data in game. This includes:
  * Board of size NxM and Z snakes. Where N,M,Z ∈ ℤ
  * All food locations

## State of AI

* 2019/03/08:
    * Snake does nothing currently🙃

## Running the Snake Locally

1) [Fork this repo](https://github.com/RyanBarclay/striper-snake/fork).

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
