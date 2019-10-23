
#!/usr/bin/env bash

# Rock-Paper-Scissors-Bash

playerScore=0
cpuScore=0

playerChosen=-1 # Player's choice of r/p/s
cpuChosen=-1 # Computer's choice of r/p/s

currentRound=-1

cpuWin=0  # 0/1 computer round win/loss
playerWin=0 # 0/1 player round win/loss

playerdisplayChosen=-1
cpudisplayChosen=-1

re='^[0-9]+$'

echo -e "Rock, Paper, Scissors!\n"

while true; do
  echo -n "How many rounds do you want to play: "
  read -r rounds
  if ! [[ $rounds =~ $re ]] ; then
     echo "It's not a number!"
     echo -e "Try again.\n"
  elif [ $rounds -lt 0 ]; then
    echo "You must chose at least 1 round!"
  else
    echo -e "$rounds rounds. Lets play!\n"
    break
  fi
done

re='^[rps]+$'
currentRound=1

while [ $rounds -gt 0 ]; do
  echo "Round: $currentRound"

  cpuChosen=$(shuf -i 1-3 -n 1)
  [ "$cpuChosen" == "1" ] && cpuChosen="r"
  [ "$cpuChosen" == "2" ] && cpuChosen="p"
  [ "$cpuChosen" == "3" ] && cpuChosen="s"

  echo -n "Rock, Paper or Scissors (r/p/s): "
  read -r playerChosen
  if ! [[ "$playerChosen" =~ $re ]] || [ "${#playerChosen}" != "1" ]; then
     echo "That is not a valid move!"
     echo -e "Please chose again.\n"
  else
    echo "The Game"
    echo "cpuChosen"
    [ "$playerChosen" == "r" ] && playerdisplayChosen="Rock"
    [ "$playerChosen" == "p" ] && playerdisplayChosen="Paper"
    [ "$playerChosen" == "s" ] && playerdisplayChosen="Scissors"

    [ "$cpuChosen" == "r" ] && cpudisplayChosen="Rock"
    [ "$cpuChosen" == "p" ] && cpudisplayChosen="Paper"
    [ "$cpuChosen" == "s" ] && cpudisplayChosen="Scissors"


    echo "--------------------------------------------------------------------"
    echo "You chose $playerdisplayChosen !"
    echo "CPU chose $cpudisplayChosen !"
    echo -e "\n"

  fi
done

echo "That's the game!"
echo "Player scored $playerScore"
echo "Computer scored $cpuScore"
echo -e "\n"

if [ $cpuScore -gt $playerScore ]; then
  echo "You lose!"
elif [ $playerScore -gt $cpuScore ]; then
  echo "You win :)"
elif [ $cpuScore -eq $playerScore ]; then
  echo "The game is a draw!"
fi

echo -e "\n"
echo "Thanks for playing!"

exit
