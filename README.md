# What is gitnomic?

Nomic was a political philosophy game invented in 1982 by Peter Suber. In his own words:

> If law-making is a game, then it is a game in which changing the rules is a move. Law-making is more than changing the rules of law-making, of course, and more than a game. But a real game may model the self-amending character of the legal system and leave the rest out. While self-amendment appears to be an esoteric feature of law, capturing it in a game creates a remarkably complete microcosm of a functional legal system.

You can find the original rules to that game here: https://legacy.earlham.edu/~peters/writing/nomic.htm#initial%20set

Gitnomic then is an adaptation of nomic to programming. Instead of players voting on changes to a set of rules,
they create pull requests to change a shared code base.

### What exactly does gitnomic do?

When you run the initial ruleset, it starts up:

1. A flask webserver
2. A mongodb database
3. An engine that will assign players points based on approvals in github.
4. A system that merges pull requests voted on by players, pulls them into the server, and restarts itself.

The initial state of the application doesnt do very much at all. Ostensibly it's a webserver,
but all it does is show whos turn it is and the players score. It is up to the players to decide
what the application will do and how to get it there.

Some players will want to make the application do something cool. Some players will want to add
security and stability to it. And still others will want to break it somehow. One of the reasons
I reccomend running nomic as the root user is so that players have the maximum freedom to turn
the application into the game they want to play.

### Whats different?

In the original nomic, players struggled with mutable vs immutable rules. The players were forced to decide which
rules were important enough to add to the 'constitution' of the game and which weren't. In gitnomic, changing any
of the lines of code is exactly as easy as changing the others.

In gitnomic this is replaced with a tension with technical limitations. Initially the codebase is untested, fragile,
and insecure. It's up to the players to determine how to implement all of the features we now consider crucial to
modern development.


### Whats the same?

Just like in the orginal game, the players can change just about everything in the game.

Just like in nomic, players earn points for proposing changes and having them voted on. (At least initially)

And of course, just like in the original the game starts off a little bit broken. Lots of things need to be fixed and
changed and the game has a good jumping off point for anyone who jumps in.

# Okay, so how do I play?

If someone else has already set up the game and you just want to know how to play heres what to do.

First, familiarise yourself with both the code and the style guide.

Then check whose turn it is. When the game initially starts up, turns cycle through players and give each player a week to propose their change and get people to vote on it.

If it's your turn, then make a pull request! I recommend forking the repository in github, cloning it onto your machine, making changes there, pushing those changes up to your forked repository, and then finally creating a pull request from your fork.

Once your pull request is up, find all of your fellow collaborators and tell them to vote. Leave plenty of time for this since you require EVERYONE to approve in the first ten rounds. If someone denies your pull request, you can modify it and ask them to approve it again. Each time you update your PR youll have to get everyone to reapprove.

Then wait for the end of the round for your change to be incorporated.

If it isn't your turn, wait until the player whos turn it is makes their pull request. Then approve or deny it as you see fit. If you deny it, make sure to say why!

You can make PR's even if it isn't your turn. This might give you extra time to collect approvals. If you make multiple PRs though, one will be selected semi-randomly

# Running the game:

I recommend running gitnomic on its own server with root permissions.
Log in as root and clone the repository into /

### 1. Create a new git account and fork the repository.
Create a new git account and confirm its email address.
Then from that account, fork this repository. 

### 2. Install prerequisites.

On a ubuntu machine, you can run:

`apt-get update && apt-get install mongodb python3-pip && pip3 install --upgrade pip && pkill mongod`

For other distributions, you can replace apt-get with your favorite package manager.

### 3. Fill out your config.json.
Config.json needs to be given some information to tie it to your git repository.

* git_login: The name of the account that owns the repository.
* git_password: The accounts password. This should never be visible unless the players make it.
* git_repo: The name of the repository the game pulls from.

### 4. Start the game!

`nohup ./start.sh &`

Check that the server is running by visiting port 80 on your servers ip address. You should see the player whose turn it now is displayed on the page.

# Local dev:

Gonna assume you have [Dinghy](https://github.com/codekitchen/dinghy) installed. Then just:

    docker-compose up

And you can visit it at [http://gitnomic.docker/](http://gitnomic.docker/).
