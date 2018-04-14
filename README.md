Running the game:

I recommend running gitnomic on its own server with root permissions.
Clone the repository into a top-level directory and log in as root.

First install some prerequisites.

On a ubuntu machine, you can run:

apt-get update && apt-get install mongodb python-pip python-dev build-essential && pip install --upgrade pip

Then make sure your config.json is filled out properly.
git_login: The name of the account that owns the repository
git_password: The accounts password. This should never be visible unless the players make it.
git_repo: The name of the repository the game pulls from.

Note that the repository MUST be owned by the account that is functioning as the admin.