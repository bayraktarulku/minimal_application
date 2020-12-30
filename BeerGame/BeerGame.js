function Card(name, image, color) {
    this.name = name
    this.action = ""
    this.image = image
    this.color = color
}

class Game {
    constructor(name, info, change) {
        this.name = name
        this.info = info
        this.break = change
    }

    add() {

    }
}

var hatman = new Game("Hatman",
"The person who receives the card must wear a hat. Hatman must drink when everyone sings Nanananana-HATMAN.",
"Hats are changed at the next hat man or possibly by rule")

var tum = new Game("Thumb",
"Use your thumb and put where you want, everyone should do the same with their thumb",
"Isten drinker!")

var question = new Game("QuizGame",
"Ask a question to someone else, that person should in turn ask a question to someone else.",
"Too slow to ask the next question or being asked - DRINK")

var taliTali = new Game("Tali-Tali",
"bla bla",
"Anyone who fails to pass on")

var woopWoop = new Game("Woop-Woop",
"Everyone uses their hands as glasses for the eyes. The person who received the card starts and sends (woop-woop) on to another person by moving the hand out and saying woop-woop (max 2 steps and not back-cake)",
"The one who misses")

var category = new Game("Category",
"The player who receives the card comes to a category and then starts saying one thing from the category, the next person should say another thing from the category",
"The one who misses")

var rule = new Game("Rule",
"Choose your own rule that applies to the entire round",
"The one who misses")

var eightGame = new Game("Eight",
"Rules..",
"The one who misses")

var drink = new Game("Drick",
"Drink number of sips on the card",
"The one who gets the card")

var giveAway = new Game("Give",
"Born number of sips on the card",
"The person who receives the card can give away sips to some funny person")

var sevenGame = new Game("Seven",
"Start with the number 1. Clockwise continue with 2. If 7 is included in the number or in the table of 7, you should say biip instead and it changes direction",
"The one who misses")

var ace = new Card("Ace","./Cards/3.png", "Red");
var ace2 = new Card("Ace","./Cards/1.png", "Black");
var ace3 = new Card("Ace","./Cards/2.png", "Black");
var ace4 = new Card("Ace","./Cards/4.png", "Red");

var king = new Card("King", "./Cards/7.png", "Red");
var king2 = new Card("King", "./Cards/5.png", "Black");
var king3 = new Card("King", "./Cards/6.png", "Black");
var king4 = new Card("King", "./Cards/8.png", "Red");

var queen = new Card("Queen","./Cards/11.png", "Red");
var queen2 = new Card("Queen","./Cards/9.png", "Black");
var queen3 = new Card("Queen","./Cards/10.png", "Black");
var queen4 = new Card("Queen","./Cards/12.png", "Red");

var knight = new Card("Knight","./Cards/15.png", "Red");
var knight2 = new Card("Knight","./Cards/13.png", "Black");
var knight3 = new Card("Knight","./Cards/14.png", "Black");
var knight4 = new Card("Knight","./Cards/16.png", "Red");

var ten = new Card("Ten","./Cards/19.png", "Red");
var ten2 = new Card("Ten","./Cards/17.png", "Black");
var ten3 = new Card("Ten","./Cards/18.png", "Black");
var ten4 = new Card("Ten","./Cards/20.png", "Red");

var nine = new Card("Nine","./Cards/23.png", "Red");
var nine2 = new Card("Nine","./Cards/21.png", "Black");
var nine3 = new Card("Nine","./Cards/22.png", "Black");
var nine4 = new Card("Nine","./Cards/24.png", "Red");

var eight = new Card("Eight","./Cards/27.png", "Red");
var eight2 = new Card("Eight","./Cards/25.png", "Black");
var eight3 = new Card("Eight","./Cards/26.png", "Black");
var eight4 = new Card("Eight","./Cards/28.png", "Red");

var seven = new Card("Seven","./Cards/31.png", "Red");
var seven2 = new Card("Seven","./Cards/29.png", "Black");
var seven3 = new Card("Seven","./Cards/30.png", "Black");
var seven4 = new Card("Seven","./Cards/32.png", "Red");

var six = new Card("Six", "./Cards/35.png", "Red");
var six2 = new Card("Six", "./Cards/33.png", "Black");
var six3 = new Card("Six", "./Cards/34.png", "Black");
var six4 = new Card("Six", "./Cards/36.png", "Red");

var five = new Card("Five","./Cards/39.png", "Red");
var five2 = new Card("Five","./Cards/37.png", "Black");
var five3 = new Card("Five","./Cards/38.png", "Black");
var five4 = new Card("Five","./Cards/40.png", "Red");

var four = new Card("Four","./Cards/43.png", "Red");
var four2 = new Card("Four","./Cards/41.png", "Black");
var four3 = new Card("Four","./Cards/42.png", "Black");
var four4 = new Card("Four","./Cards/44.png", "Red");

var three = new Card("Three","./Cards/47.png", "Red");
var three2 = new Card("Three","./Cards/45.png", "Black");
var three3 = new Card("Three","./Cards/46.png", "Black");
var three4 = new Card("Three","./Cards/48.png", "Red");

var two = new Card("Two","./Cards/51.png", "Red");
var two2 = new Card("Two","./Cards/49.png", "Black");
var two3 = new Card("Two","./Cards/50.png", "Black");
var two4 = new Card("Two","./Cards/52.png", "Red");

function Games() {
    var games = [sevenGame,giveAway,drink,eightGame,
        rule,category,woopWoop,taliTali,question,tum,hatman];

    return games;
}

function Cards() {
    var cards = [six, seven, eight, nine, ten, knight, queen, king, ace];

    return cards;
}

function LowCards() {
    var lowCards = [two, three, four, five];

    return lowCards;
}

function AllCards() {
    var allCards = [ace,ace2,ace3,ace4,two,two2,two3,two4,three,three2,three3,three4,four,four2,four3,four4,
        five,five2,five3,five4,six,six2,six3,six4,seven,seven2,seven3,seven4,eight,eight2,eight3,eight4,
        nine,nine2,nine3,nine4,ten,ten2,ten3,ten4,knight,knight2,knight3,knight4,queen,queen2,queen3,queen4,
        king,king2,king3,king4];

    return allCards;
}


class NewCardGame {
    constructor() {
        this.allCards = AllCards();
        this.lowCards = LowCards();
        this.cards = Cards();
        this.games = Games();
        this.currentCard;
    }

    updateCard(name, action, color) {
        if(color == "Red" || color == "Black")
        {
            this.allCards.forEach(element => {
                if (element.name == name && element.color == color)
                {
                    element.action = action;
                }
            });
        } else {
            this.allCards.forEach(element => {
                if (element.name == name)
                {
                    element.action = action;
                }
            });
        }
    }
}

var newGame = new NewCardGame();