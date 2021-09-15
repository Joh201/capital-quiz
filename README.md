# Capital City Game

<p>
The capital city game is a simple Python terminal game that can be played by children and adults. It runs on Code Institute's mock terminal on Heroku. This game provides the opportunity to learn about the capitals of the different countries in the world while at the same time having fun. The game can be useful to school children when they are studying geography. Moreover, the capital city game could also inspire the players of the game to travel the world to visit the different capitals, and the countries in which they are located. In addition, the game also helps to expand the general knowledge of the player.
</p>

[Here is the live version of my project](https://capital-city-quiz-game.herokuapp.com/)

![weblook of the game](assets/images/applook.PNG)

## How to play
The capital city game is an easy game to play. The user starts the game by pressing the run programe
button at the top of the game. The user is then requested to enter name, after that the game randomly chooses
one question out of 25 questions. The user then types in the response to the question, and receives a feed back.
The user can play the game as long as the user wants.

## Existing features

### Welcome message
* When the player starts the game, the player is requested to input name.
* The player is then greeted with a welcome message that includes the players name.

![welcome message](assets/images/welcome.PNG)

### Input valiation
* when the player inputs a response to a question, the response is checked:
* Whether the input is a number or the input contains a number.
* Depending on the case the player gets appropriate feedback.
* The player also gets suggestions on the right format of input.

![validation](assets/images/invalidinput.PNG)

### Feedback to the user
* When the user anwers the question, the user gets two types of feedback:
* If the user gives the correct answer, the user receives well done message.
* If the user misses the right answer, the user gets a hint to check spelling.

![check](assets/images/checkanswer.PNG)

### During the game
* The user can decide to continue playing or leave the game by choosing  'y' or 'n' respectively.
* If the user decides to leave before answering all the questions, the user can get a score report.

![middle of game](assets/images/midgame.PNG)

### Continuation response
* The user is asked to choose either 'y' or 'n' to continue palying.
* However, if the user inputs other letters, the user is requested again to input the right letter.

![continuation](assets/images/continuresponse.PNG)




