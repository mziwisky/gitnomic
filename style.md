Items in the style guide are intended to communicate conventions and expectations surrounding the management of the repository, the codebase, and pull requests. Where items in the style guide reference the original nomic ruleset, they will have a reference at the end of the line.

The **server** is the computer or machine that the game is running on.

The games **host** is the player who originally set up the server.

The **repository** is the github repository specified in the config.json when the game is started.

1. A pull request should be rejected if it violates any of the elements in the style guide. Reviewers may cite the style guide rule they feel it breaks when declining a pull request.
2. A pull request should not cause the application to throw an error.
3. No pull request should change both the rules in the style guide and also functioning code.
4. No change shall be made that causes the code in the repoistory to diverge from the code on the server.
5. The logic that constitutes when a pull request will be approved must require that each player casts a vote. (105)
6. The state of affairs that constitutes winning must not be altered from achieving n points (112)
7. A pull request should do exactly one thing. Even if a pull request touches multiple files, the feature it is implementing should be able to be concisely described.
8. A pull request should accurately describe its changes in its title and description.
9. The code in a pull request should be easy to read, and easy to comprehend it's intended effect.
10. In the event that the server is in a state where it cannot serve web pages for longer then 3 days, this is a catastrophic disaster.
11. No one should modify the server or repository except in the event of a catastrophic disaster. The credentials to access the server and repository shall be kept by the games host, but remain unused except in the event of a catastrophic disaster.
12. In the event of a catastrophic disaster, the games host shall use whatever means they see fit to return the game to it's last working state. If they modify the code in the server in any way, that change must be reflected in the repository before the game is restarted.
13. If a player denies another players pull request, they should leave a reason for why they denied it.