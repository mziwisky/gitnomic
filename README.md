#What is gitnomic?

Nomic was a political philosophy game invented in 1982 by Peter Suber. In his own words:

> If law-making is a game, then it is a game in which changing the rules is a move. Law-making is more than changing the rules of law-making, of course, and more than a game. But a real game may model the self-amending character of the legal system and leave the rest out. While self-amendment appears to be an esoteric feature of law, capturing it in a game creates a remarkably complete microcosm of a functional legal system.

You can find the original rules to that game here: https://legacy.earlham.edu/~peters/writing/nomic.htm#initial%20set

Gitnomic then is an adaptation of nomic to programming. Instead of players voting on changes to a set of rules,
they create pull requests to change a shared code base.

##What exactly does gitnomic do?

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

##Whats different?

In the original nomic, players struggled with mutable vs immutable rules. The players were forced to decide which
rules were important enough to add to the 'constitution' of the game and which weren't. In gitnomic, changing any
of the lines of code is exactly as easy as changing the others.

In gitnomic this is replaced with a tension with technical limitations. Initially the codebase is untested, fragile,
and insecure. It's up to the players to determine how to implement all of the features we now consider crucial to
modern development.


##Whats the same?

Just like in the orginal game, the players can change just about everything in the game.

Just like in nomic, players earn points for proposing changes and having them voted on. (At least initially)

And of course, just like in the original the game starts off a little bit broken. Lots of things need to be fixed and
changed and the game has a good jumping off point for anyone who jumps in.

# Running the game:

I recommend running gitnomic on its own server with root permissions.
Log in as root and clone the repository into /

###1. Create a new git account and fork the repository.
Create a new git account and confirm its email address.
Then from that account, fork this repository. 

###2. Install prerequisites.

On a ubuntu machine, you can run:

`apt-get update && apt-get install mongodb python-pip python-dev build-essential && pip install --upgrade pip`

For other distributions, you can replace apt-get with your favorite package manager.


###3. Fill out your config.json.
Config.json needs to be given some information to tie it to your git repository.

* git_login: The name of the account that owns the repository.
* git_password: The accounts password. This should never be visible unless the players make it.
* git_repo: The name of the repository the game pulls from.

###4. Start the game!

`./start.sh`

Check that the server is running by visiting port 80 on your servers ip address. You should see the player whose turn it now is.