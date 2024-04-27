//Ajuste o tamanho dos quadrados que formam a cobra
var drawSize = 20;

var Position = function(x, y) {
    this.x = x;
    this.y = y;
};
Position.prototype.Draw = function(mode) {
    rectMode(CORNER);
    switch(mode) {
        case "snake":
            rect(this.x * drawSize, this.y * drawSize, drawSize, drawSize);
            break;
        case "food":
            image(getImage("avatars/spunky-sam-red"), this.x * drawSize, this.y * drawSize, drawSize, drawSize);
            break;
    }
};

var Snake = function() {
    this.pos = [new Position(round(width / drawSize / 2), round(height / drawSize / 2)), new Position(round(width / drawSize / 2 + 1), round(height / drawSize / 2))];
    this.direction = false;
};
Snake.prototype.Draw = function() {
    stroke(0, 0, 0);
    fill(0, 255, 255);
    for(var i = 0; i < this.pos.length; i++) {
        this.pos[i].Draw("snake");
    }
};
Snake.prototype.Move = function() {
    switch(this.direction) {
        case UP:
            for(var i = this.pos.length - 1; i > 0; i--) {
                this.pos[i].x = this.pos[i - 1].x;
                this.pos[i].y = this.pos[i - 1].y;
            }
            this.pos[0].y--;
            if(this.pos[0].y < 0) {
                this.pos[0].y = floor(height / drawSize) - 1;
            }
            break;
        case DOWN:
            for(var i = this.pos.length - 1; i > 0; i--) {
                this.pos[i].x = this.pos[i - 1].x;
                this.pos[i].y = this.pos[i - 1].y;
            }
            this.pos[0].y++;
            if(this.pos[0].y > floor(height / drawSize) - 1) {
                this.pos[0].y = 0;
            }
            break;
        case LEFT:
            for(var i = this.pos.length - 1; i > 0; i--) {
                this.pos[i].x = this.pos[i - 1].x;
                this.pos[i].y = this.pos[i - 1].y;
            }
            this.pos[0].x--;
            if(this.pos[0].x < 0) {
                this.pos[0].x = floor(width / drawSize) - 1;
            }
            break;
        case RIGHT:
            for(var i = this.pos.length - 1; i > 0; i--) {
                this.pos[i].x = this.pos[i - 1].x;
                this.pos[i].y = this.pos[i - 1].y;
            }
            this.pos[0].x++;
            if(this.pos[0].x > floor(width / drawSize) - 1) {
                this.pos[0].x = 0;
            }
            break;
    }
};
Snake.prototype.HitItself = function() {
    for(var i = 1; i < this.pos.length; i++) {
        if(this.pos[0].x === this.pos[i].x && this.pos[0].y === this.pos[i].y) {
            return true;
        }
    }
    return false;
};
Snake.prototype.WillEat = function(food) {
    switch(this.direction) {
        case UP:
            if((this.pos[0].y - 1 === food.pos.y || (this.pos[0].y === 0 && food.pos.y === height / drawSize - 1)) && this.pos[0].x === food.pos.x) {
                return true;
            }
            break;
        case DOWN:
            if((this.pos[0].y + 1 === food.pos.y || (this.pos[0].y === height / drawSize - 1 && food.pos.y === 0)) && this.pos[0].x === food.pos.x) {
                return true;
            }
            break;
        case LEFT:
            if((this.pos[0].x - 1 === food.pos.x || (this.pos[0].x === 0 && food.pos.x === width / drawSize - 1)) && this.pos[0].y === food.pos.y) {
                return true;
            }
            break;
        case RIGHT:
            if((this.pos[0].x + 1 === food.pos.x || (this.pos[0].x === width / drawSize - 1 && food.pos.x === 0)) && this.pos[0].y === food.pos.y) {
                return true;
            }
            break;
    }
    return false;
};
Snake.prototype.Eat = function(food) {
    this.pos.unshift(food.pos);
};

var Food = function() {
    this.pos = new Position(round(random(0, width / drawSize - 1)), round(random(0, height / drawSize - 1)));
};
Food.prototype.Draw = function() {
    fill(255, 0, 0);
    this.pos.Draw("food");
};
Food.prototype.RePos = function(snake) {
    var tempX;
    var tempY;
    var reRand = true;
    while(reRand) {
        tempX = round(random(0, floor(width / drawSize) - 1));
        while(tempX === this.pos.x) {
            tempX = round(random(0, floor(width / drawSize) - 1));
        }
        tempY = round(random(0, floor(height / drawSize) - 1));
        while(tempY === this.pos.y) {
            tempY = round(random(0, floor(height / drawSize) - 1));
        }
        reRand = false;
        for(var i = 0; i < snake.pos.length; i++) {
            if(tempX === snake.pos[i].x && tempY === snake.pos[i].y) {
                reRand = true;
            }
        }
    }
    this.pos = new Position(tempX, tempY);
};

var Button = function(text, x, y, fontType, fontSize, strokeNormal, fillNormal, strokeMouseOver, fillMouseOver, action, father) {
    textSize(fontSize);
    this.position = new Position(x, y);
    this.width = textWidth(text) * 1.5;
    this.height = (textAscent() + textDescent()) * 1.5;
    this.strokeNormal = strokeNormal;
    this.fillNormal = fillNormal;
    this.strokeMouseOver = strokeMouseOver;
    this.fillMouseOver = fillMouseOver;
    this.text = text;
    this.textFont = createFont(fontType, fontSize);
    this.Action = action;
    this.father = father;
};
Button.prototype.Draw = function() {
    rectMode(CENTER);
    textFont(this.textFont);
    textAlign(CENTER, CENTER);

    var strokeColor = color(127, 127, 127);
    var fillColor = this.fill;
    
    if(this.IsMouseOver()) {
        strokeColor = this.strokeMouseOver;
        fillColor = this.fillMouseOver;
    } else {
        strokeColor = this.strokeNormal;
        fillColor = this.fillNormal;
    }

    stroke(strokeColor);
    fill(fillColor);
    rect(this.position.x, this.position.y, this.width, this.height, 10);
    fill(strokeColor);
    text(this.text, this.position.x, this.position.y);
};
Button.prototype.IsMouseOver = function() {
    if(mouseX >= this.position.x - this.width / 2 && mouseX <= this.position.x + this.width / 2 && mouseY >= this.position.y - this.height / 2 && mouseY <= this.position.y + this.height / 2) {
        return true;
    }
    return false;
};

var stateMachine = {
    NULL: 0,
    START: 1,
    MENU: 2,
    PLAY: 3,
    PAUSE: 4,
    WIN: 5,
    LOSE: 6,
    RELOAD: 7
};

var GameController = function() {
    this.lastState = stateMachine.NULL;
    this.currentState = stateMachine.START;
    this.lastFrameRate = 0;
    this.currentFrameRate = 60;
};
GameController.prototype.GameStateMachine = function() {
    switch(this.currentState) {
        case stateMachine.NULL:
            this.SwitchState(stateMachine.RELOAD);
            break;
        case stateMachine.START:
            this.snake = new Snake();
            this.food = new Food();
            this.buttons = [
                new Button("Noob", width / 10, 11 * height / 16, "monospace", 3 * min(width, height) / 80, color(0, 0, 0), color(125, 125, 125), color(125, 125, 125), color(255, 255, 255), function() {this.father.SwitchFrameRate(2);}, this),
                new Button("Starter", width / 5, 61 * height / 80, "monospace", 3 * min(width, height) / 80, color(0, 0, 0), color(125, 125, 125), color(125, 125, 125), color(255, 255, 255), function() {this.father.SwitchFrameRate(3);}, this),
                new Button("Very Easy", 3 * width / 10, 67 * height / 80, "monospace", 3 * min(width, height) / 80, color(0, 0, 0), color(125, 125, 125), color(125, 125, 125), color(255, 255, 255), function() {this.father.SwitchFrameRate(4);}, this),
                new Button("Easy", 2 * width / 5, 61 * height / 80, "monospace", 3 * min(width, height) / 80, color(0, 0, 0), color(125, 125, 125), color(125, 125, 125), color(255, 255, 255), function() {this.father.SwitchFrameRate(5);}, this),
                new Button("Normal", width / 2, 11 * height / 16, "monospace", 3 * min(width, height) / 80, color(0, 0, 0), color(125, 125, 125), color(125, 125, 125), color(255, 255, 255), function() {this.father.SwitchFrameRate(6);}, this),
                new Button("Hard", 3 * width / 5, 61 * height / 80, "monospace", 3 * min(width, height) / 80, color(0, 0, 0), color(125, 125, 125), color(125, 125, 125), color(255, 255, 255), function() {this.father.SwitchFrameRate(7);}, this),
                new Button("Very Hard", 7 * width / 10, 67 * height / 80, "monospace", 3 * min(width, height) / 80, color(0, 0, 0), color(125, 125, 125), color(125, 125, 125), color(255, 255, 255), function() {this.father.SwitchFrameRate(8);}, this),
                new Button("Expert", 4 * width / 5, 61 * height / 80, "monospace", 3 * min(width, height) / 80, color(0, 0, 0), color(125, 125, 125), color(125, 125, 125), color(255, 255, 255), function() {this.father.SwitchFrameRate(9);}, this),
                new Button("Master", 9 * width / 10, 11 * height / 16, "monospace", 3 * min(width, height) / 80, color(0, 0, 0), color(125, 125, 125), color(125, 125, 125), color(255, 255, 255), function() {this.father.SwitchFrameRate(10);}, this),
                new Button("Main Menu", width / 4, 7 * height / 8, "monospace", min(width, height) / 16, color(0, 0, 0), color(255, 0, 0), color(125, 125, 125), color(255, 125, 125), function() {this.father.SwitchState(stateMachine.NULL);}, this),
                new Button("Play Again", 3 * width / 4, 7 * height / 8, "monospace", min(width, height) / 16, color(0, 0, 0), color(0, 255, 0), color(125, 125, 125), color(125, 255, 125), function() {this.father.SwitchFrameRate(this.father.lastFrameRate);this.father.SwitchState(stateMachine.RELOAD);}, this)
            ];
            this.SwitchFrameRate(60);
            this.SwitchState(stateMachine.MENU);
            break;
        case stateMachine.MENU:
            this.DrawMenuScreen();
            break;
        case stateMachine.PLAY:
            if(this.snake.HitItself()) {
                this.SwitchFrameRate(60);
                this.SwitchState(stateMachine.LOSE);
            } else if(this.snake.WillEat(this.food)) {
                this.SwitchState(stateMachine.WIN);
            } else {
                this.snake.Move();
            }
            this.DrawPlayScreen();
            break;
        case stateMachine.PAUSE:
            this.DrawPauseScreen();
            break;
        case stateMachine.WIN:
            this.snake.Eat(this.food);
            this.food.RePos(this.snake);
            this.DrawPlayScreen();
            this.SwitchState(stateMachine.PLAY);
            break;
        case stateMachine.LOSE:
            this.DrawLoseScreen();
            break;
        case stateMachine.RELOAD:
            this.snake = new Snake();
            this.food = new Food();
            switch(this.lastState) {
                case stateMachine.NULL:
                    this.SwitchState(stateMachine.MENU);
                    break;
                case stateMachine.LOSE:
                    this.SwitchState(stateMachine.PLAY);
                    break;
            }
    }
};
GameController.prototype.SwitchState = function(nextState) {
    this.lastState = this.currentState;
    this.currentState = nextState;
};
GameController.prototype.SwitchFrameRate = function(switchTo) {
    this.lastFrameRate = this.currentFrameRate;
    this.currentFrameRate = switchTo;
    frameRate(this.currentFrameRate);
};
GameController.prototype.DrawMenuScreen = function() {
    background(252, 252, 252);
    fill(0, 0, 0);
    textAlign(CENTER, CENTER);
    textFont("monospace", 3 * width / 16);
    text("Snake X", width/ 2, height / 4);
    textSize(width / 16);
    text("Choose the Difficult Level:", width / 2, height / 2);
    for(var i = 0; i < 9; i++) {
        this.buttons[i].Draw();
    }
};
GameController.prototype.DrawPlayScreen = function() {
    background(255, 255, 255);
    this.food.Draw();
    this.snake.Draw();
    if(this.snake.direction === false) {
        fill(0, 0, 0);
        textFont("monospace", width / 16);
        text("Press       to Start", width / 2, 73 * height / 80);
        textSize(width / 40);
        text("Use \"SPACE\" to Pause", width / 2, 39 * height / 40);
        image(getImage("space/plus"), width / 2 - 50, 337 * height / 400, width / 8, height / 8);
    }
};
GameController.prototype.DrawPauseScreen = function() {
    this.DrawPlayScreen();
    fill(0, 0, 0);
    textAlign(CENTER, CENTER);
    textFont("monospace", 3 * width / 16);
    textLeading(3 * height / 20);
    text("======\n||Paused||\n======", width / 2, 3 * height / 8);
    textSize(width / 16);
    text("Press \"SPACE\" to continue", width / 2, 5 * height / 8);
};
GameController.prototype.DrawLoseScreen = function() {
    background(252, 252, 252);
    fill(0, 0, 0);
    textAlign(CENTER, CENTER);
    textFont("monospace", 3 * width / 16);
    text("GAME\nOVER", width / 2, 3 * height / 8);
    textSize(width / 16);
    text("You've got " + (this.snake.pos.length - 2) + " point", width / 2, 11 * height / 16);
    for(var i = 9; i < 11; i++) {
        this.buttons[i].Draw();
    }
};

var gameController = new GameController();
gameController.SwitchFrameRate(60);

var draw = function() {
    gameController.GameStateMachine();
};

keyReleased = function () {
    switch(gameController.currentState) {
        case stateMachine.PLAY:
            switch(keyCode) {
                case UP:
                    if(gameController.snake.direction !== DOWN) {
                        gameController.snake.direction = keyCode;
                    }
                    break;
                case DOWN:
                    if(gameController.snake.direction !== UP) {
                        gameController.snake.direction = keyCode;
                    }
                    break;
                case LEFT:
                    if(gameController.snake.direction !== RIGHT) {
                        gameController.snake.direction = keyCode;
                    }
                    break;
                case RIGHT:
                    if(gameController.snake.direction !== LEFT) {
                        gameController.snake.direction = keyCode;
                    }
                    break;
                case 32:
                    gameController.SwitchState(stateMachine.PAUSE);
                    break;
            }
            break;
        case stateMachine.PAUSE:
            if(keyCode === 32) {
                gameController.SwitchState(stateMachine.PLAY);
            }
            break;
    }
};
mouseClicked = function() {
    switch(gameController.currentState) {
        case stateMachine.MENU:
            for(var i = 0; i < 9; i++) {
                if(gameController.buttons[i].IsMouseOver()) {
                    gameController.buttons[i].Action();
                    gameController.SwitchState(stateMachine.PLAY);
                }
            }
            break;
        case stateMachine.LOSE:
            for(var i = 9; i < 11; i++) {
                if(gameController.buttons[i].IsMouseOver()) {
                    gameController.buttons[i].Action();
                }
            }
            break;
    }
};