var Properties = {
    FRAME_RATE: 60,
    DRAW_SIZE: 20,
    Images: {
        FOOD: getImage("avatars/spunky-sam-red")
    },
    Colors: {
        HEAD: color(255, 121, 0),
        BLACK: color(0, 0, 0),
        RED: color(255, 0, 0),
        GREEN: color(0, 255, 0),
        WHITE: color(255, 255, 255)
    }
};

var CellType = {
    EMPTY: "CellType.EMPTY",
    FOOD: "CellType.FOOD",
    Snake: {
        HEAD: "CellType.Snake.HEAD",
        BODY: "CellType.Snake.BODY",
        TAIL: "CellType.Snake.TAIL"
    }
};

var Direction = {
    NONE: 32,
    UP: UP,
    DOWN: DOWN,
    LEFT: LEFT,
    RIGHT: RIGHT,
};

var Rotation = {
    NONE: "Rotation.NONE",
    CLOCKWISE: "Rotation.CLOCKWISE",
    COUNTERCLOCKWISE: "Rotation.COUNTERCLOCKWISE",

    getRotation: function(lastFacing, newFacing) {
        switch(lastFacing) {
            case Direction.NONE:
                return this.NONE;
            case Direction.UP:
                if(newFacing === Direction.RIGHT) {
                    return this.CLOCKWISE;
                } else if(newFacing === Direction.LEFT) {
                    return this.COUNTERCLOCKWISE;
                } else {
                    return this.NONE;
                }
                break;
            case Direction.DOWN:
                if(newFacing === Direction.LEFT) {
                    return this.CLOCKWISE;
                } else if(newFacing === Direction.RIGHT) {
                    return this.COUNTERCLOCKWISE;
                } else {
                    return this.NONE;
                }
                break;
            case Direction.LEFT:
                if(newFacing === Direction.UP) {
                    return this.CLOCKWISE;
                } else if(newFacing === Direction.DOWN) {
                    return this.COUNTERCLOCKWISE;
                } else {
                    return this.NONE;
                }
                break;
            case Direction.RIGHT:
                if(newFacing === Direction.DOWN) {
                    return this.CLOCKWISE;
                } else if(newFacing === Direction.UP) {
                    return this.COUNTERCLOCKWISE;
                } else {
                    return this.NONE;
                }
                break;
        }
    }
};

var Margin = {
    TOP_LEFT: "Margin.TOP_LEFT",
    TOP: "Margin.TOP",
    TOP_RIGHT: "Margin.TOP_RIGHT",
    LEFT: "Margin.LEFT",
    NONE: "Margin.NONE",
    RIGHT: "Margin.RIGHT",
    BOTTON_LEFT: "Margin.BOTTON_LEFT",
    BOTTON: "Margin.BOTTON",
    BOTTON_RIGHT: "Margin.BOTTON_RIGHT"
};

var Speed = {
    NOOB: 2,
    STARTER: 3,
    VERY_EASY: 4,
    EASY: 5,
    NORMAL: 6,
    HARD: 7,
    VERY_HARD: 8,
    EXPERT: 9,
    MASTER: 10
};

var Cell = function(row, col) {
    this.ROW = row;
    this.COL = col;

    this.cellType = CellType.EMPTY;
    this.facing = Direction.NONE;
    this.rotation = Rotation.NONE;

    this.getCellType = function() {
        return this.cellType;
    };

    this.setCellType = function(cellType) {
        this.cellType = cellType;
    };

    this.getFacing = function() {
        return this.facing;
    };

    this.setFacing = function(facing) {
        this.facing = facing;
    };

    this.getRotation = function() {
        return this.rotation;
    };

    this.setRotation = function(rotation) {
        this.rotation = rotation;
    };

    this.transform = function() {
        switch(this.facing) {
            case Direction.NONE:
                translate(this.COL * Properties.DRAW_SIZE, this.ROW * Properties.DRAW_SIZE);
                break;
            case Direction.UP:
                translate(this.COL * Properties.DRAW_SIZE, (this.ROW + 1) * Properties.DRAW_SIZE);
                rotate(-90);
                break;
            case Direction.DOWN:
                translate((this.COL + 1) * Properties.DRAW_SIZE, this.ROW * Properties.DRAW_SIZE);
                rotate(90);
                break;
            case Direction.LEFT:
                translate((this.COL + 1) * Properties.DRAW_SIZE, (this.ROW + 1) * Properties.DRAW_SIZE);
                rotate(180);
                break;
            case Direction.RIGHT:
                translate(this.COL * Properties.DRAW_SIZE, this.ROW * Properties.DRAW_SIZE);
                break;
        }
    };

    this.animateHead = function(step) {
        switch(this.rotation) {
            case Rotation.NONE:
                translate(Properties.DRAW_SIZE * step, 0);
                break;
            case Rotation.CLOCKWISE:
                translate(sin(90 * step) * Properties.DRAW_SIZE, (1 - cos(90 * step)) * Properties.DRAW_SIZE);
                rotate(90 * step);
                break;
            case Rotation.COUNTERCLOCKWISE:
                rotate(-90 * step);
                break;
        }
    };

    this.animateTail = function(step, rotation) {
        switch(rotation) {
            case Rotation.NONE:
                translate(Properties.DRAW_SIZE * step, 0);
                break;
            case Rotation.CLOCKWISE:
                translate((sin(90 * step) + 1) * Properties.DRAW_SIZE, (1 - cos(90 * step)) * Properties.DRAW_SIZE);
                rotate(90 * step);
                translate(-Properties.DRAW_SIZE, 0);
                break;
            case Rotation.COUNTERCLOCKWISE:
                translate(Properties.DRAW_SIZE, 0);
                rotate(-90 * step);
                translate(-Properties.DRAW_SIZE, 0);
                break;
        }
    };

    this.drawFood = function() {
        image(Properties.Images.FOOD, 0, 0, Properties.DRAW_SIZE, Properties.DRAW_SIZE);
    };

    this.drawHead = function() {
        fill(Properties.Colors.RED);
        beginShape();
        vertex(0.4 * Properties.DRAW_SIZE, 0.45 * Properties.DRAW_SIZE);
        vertex(0.9 * Properties.DRAW_SIZE, 0.45 * Properties.DRAW_SIZE);
        vertex(0.85 * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE);
        vertex(0.9 * Properties.DRAW_SIZE, 0.55 * Properties.DRAW_SIZE);
        vertex(0.4 * Properties.DRAW_SIZE, 0.55 * Properties.DRAW_SIZE);
        endShape();

        fill(Properties.Colors.HEAD);
        arc(0, 0.5 * Properties.DRAW_SIZE, Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE, -90, 90);

        fill(Properties.Colors.WHITE);
        ellipse(0.25 * Properties.DRAW_SIZE, 0.4 * Properties.DRAW_SIZE, 0.1 * Properties.DRAW_SIZE, 0.15 * Properties.DRAW_SIZE);
        ellipse(0.25 * Properties.DRAW_SIZE, 0.6 * Properties.DRAW_SIZE, 0.1 * Properties.DRAW_SIZE, 0.15 * Properties.DRAW_SIZE);

        fill(Properties.Colors.BLACK);
        ellipse(0.27 * Properties.DRAW_SIZE, 0.4 * Properties.DRAW_SIZE, 0.05 * Properties.DRAW_SIZE, 0.05 * Properties.DRAW_SIZE);
        ellipse(0.27 * Properties.DRAW_SIZE, 0.6 * Properties.DRAW_SIZE, 0.05 * Properties.DRAW_SIZE, 0.05 * Properties.DRAW_SIZE);
    };

    this.drawBody = function(step, rotation) {
        fill(Properties.Colors.HEAD);

        switch(this.rotation) {
            case Rotation.NONE:
                if(step < 0.5) {
                    rect(Properties.DRAW_SIZE * step, 0.25 * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE);
                } else {
                    rect(Properties.DRAW_SIZE * step, 0.25 * Properties.DRAW_SIZE, (1 - step) * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE);
                }
                break;
            case Rotation.CLOCKWISE:
                if(step < 0.5) {
                    arc(Properties.DRAW_SIZE, Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 90 * step + 180, 90 * step + 225);
                } else {
                    arc(Properties.DRAW_SIZE, Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 90 * step + 180, 270);
                }
                break;
            case Rotation.COUNTERCLOCKWISE:
                if(step < 0.5) {
                    arc(Properties.DRAW_SIZE, 0, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 135 - 90 * step, 180 - 90 * step);
                } else {
                    arc(Properties.DRAW_SIZE, 0, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 90, 180 - 90 * step);
                }
                break;
        }

        fill(Properties.Colors.BLACK);

        switch(this.rotation) {
            case Rotation.NONE:
                if(step < 0.5) {
                    rect((step + 0.5) * Properties.DRAW_SIZE, 0.25 * Properties.DRAW_SIZE, (0.5 - step) * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE);
                }
                break;
            case Rotation.CLOCKWISE:
                if(step < 0.5) {
                    arc(Properties.DRAW_SIZE, Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 90 * step + 225, 270);
                }
                break;
            case Rotation.COUNTERCLOCKWISE:
                if(step < 0.5) {
                    arc(Properties.DRAW_SIZE, 0, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 90, 135 - 90 * step);
                }
                break;
        }

        fill(Properties.Colors.GREEN);

        switch(this.rotation) {
            case Rotation.NONE:
                break;
            case Rotation.CLOCKWISE:
                ellipse(Properties.DRAW_SIZE, Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE);
                break;
            case Rotation.COUNTERCLOCKWISE:
                ellipse(Properties.DRAW_SIZE, 0, 0.5 * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE);
                break;
        }

        
        fill(Properties.Colors.BLACK);

        switch(rotation) {
            case Rotation.NONE:
                if(step < 0.5) {
                    rect(Properties.DRAW_SIZE, 0.25 * Properties.DRAW_SIZE, Properties.DRAW_SIZE * step, 0.5 * Properties.DRAW_SIZE);
                } else {
                    rect((step + 0.5) * Properties.DRAW_SIZE, 0.25 * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE);
                }
                break;
            case Rotation.CLOCKWISE:
                if(step < 0.5) {
                    arc(Properties.DRAW_SIZE, Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 270, 90 * step + 270);
                } else {
                    arc(Properties.DRAW_SIZE, Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 90 * step + 225, 90 * step + 270);
                }
                break;
            case Rotation.COUNTERCLOCKWISE:
                if(step < 0.5) {
                    arc(Properties.DRAW_SIZE, 0, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 90 - step * 90, 90);
                } else {
                    arc(Properties.DRAW_SIZE, 0, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 90 - step * 90, 135 - step * 90);
                }
                break;
        }

        fill(Properties.Colors.HEAD);

        switch(rotation) {
            case Rotation.NONE:
                if(step >= 0.5) {
                    rect(Properties.DRAW_SIZE, 0.25 * Properties.DRAW_SIZE, (step - 0.5) * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE);
                }
                break;
            case Rotation.CLOCKWISE:
                if(step >= 0.5) {
                    arc(Properties.DRAW_SIZE, Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 270, 90 * step + 225);
                }
                break;
            case Rotation.COUNTERCLOCKWISE:
                if(step >= 0.5) {
                    arc(Properties.DRAW_SIZE, 0, 1.5 * Properties.DRAW_SIZE, 1.5 * Properties.DRAW_SIZE, 135 - step * 90, 90);
                }
                break;
        }

        fill(Properties.Colors.GREEN);

        switch(rotation) {
            case Rotation.NONE:
                break;
            case Rotation.CLOCKWISE:
                ellipse(Properties.DRAW_SIZE, Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE);
                break;
            case Rotation.COUNTERCLOCKWISE:
                ellipse(Properties.DRAW_SIZE, 0, 0.5 * Properties.DRAW_SIZE, 0.5 * Properties.DRAW_SIZE);
                break;
        }
    };

    this.drawTail = function() {
        fill(Properties.Colors.HEAD);
        beginShape();
        vertex(Properties.DRAW_SIZE, 0.25 * Properties.DRAW_SIZE);
        bezierVertex(0, 0.4 * Properties.DRAW_SIZE, 0, 0.6 * Properties.DRAW_SIZE, Properties.DRAW_SIZE, 0.75 * Properties.DRAW_SIZE);
        endShape();

        fill(Properties.Colors.BLACK);
        quad(Properties.DRAW_SIZE, 0.25 * Properties.DRAW_SIZE, Properties.DRAW_SIZE, 0.75 * Properties.DRAW_SIZE, 0.6 * Properties.DRAW_SIZE, 0.68 * Properties.DRAW_SIZE, 0.6 * Properties.DRAW_SIZE, 0.32 * Properties.DRAW_SIZE);
    };

    this.draw = function(step, rotation, board) {
        noStroke();
        pushMatrix();

        this.transform();

        switch(this.cellType) {
            case CellType.FOOD:
                this.drawFood();
                break;
            case CellType.Snake.HEAD:
                this.animateHead(step);
                this.drawHead();
                break;
            case CellType.Snake.BODY:
                this.drawBody(step, rotation);
                break;
            case CellType.Snake.TAIL:
                this.animateTail(step, rotation);
                this.drawTail();
                break;
        }

        popMatrix();

        if(this.facing === Direction.NONE) {
            return;
        }

        var margin = board.checkMargin(this);

        if(margin === Margin.NONE) {
            return;
        }

        var cell = new Cell(this.ROW, this.COL);

        cell.setCellType(this.getCellType());
        cell.setFacing(this.getFacing());
        cell.setRotation(this.getRotation());

        switch(this.facing) {
            case Direction.UP:
                if(/TOP/.test(margin)) {
                    cell.ROW = board.ROW_COUNT;
                    cell.draw(step, rotation, board);
                }
                break;
            case Direction.DOWN:
                if(/BOTTON/.test(margin)) {
                    cell.ROW = -1;
                    cell.draw(step, rotation, board);
                }
                break;
            case Direction.LEFT:
                if(/LEFT/.test(margin)) {
                    cell.COL = board.COL_COUNT;
                    cell.draw(step, rotation, board);
                }
                break;
            case Direction.RIGHT:
                if(/RIGHT/.test(margin)) {
                    cell.COL = -1;
                    cell.draw(step, rotation, board);
                }
                break;
        }
    };
};

var Board = function() {
    this.ROW_COUNT = floor(height / Properties.DRAW_SIZE);
    this.COL_COUNT = floor(width / Properties.DRAW_SIZE);

    this.cells = [];
    for(var row = 0; row < this.ROW_COUNT; row++) {
        this.cells.push([]);
        for(var col = 0; col < this.COL_COUNT; col++) {
            this.cells[row].push(new Cell(row, col));
        }
    }

    this.getCenterCell = function() {
        return this.cells[floor(this.ROW_COUNT / 2 - 1)][floor(this.COL_COUNT / 2 - 1)];
    };

    this.cellsCount = function() {
        return this.ROW_COUNT * this.COL_COUNT;
    };

    this.checkMargin = function(cell) {
        switch(cell.ROW) {
            case 0:
                switch(cell.COL) {
                    case 0:
                        return Margin.TOP_LEFT;
                    case this.COL_COUNT - 1:
                        return Margin.TOP_RIGHT;
                    default:
                        return Margin.TOP;
                }
                break;
            case this.ROW_COUNT - 1:
                switch(cell.COL) {
                    case 0:
                        return Margin.BOTTON_LEFT;
                    case this.COL_COUNT - 1:
                        return Margin.BOTTON_RIGHT;
                    default:
                        return Margin.BOTTON;
                }
                break;
            default:
                switch(cell.COL) {
                    case 0:
                        return Margin.LEFT;
                    case this.COL_COUNT - 1:
                        return Margin.RIGHT;
                    default:
                        return Margin.NONE;
                }
                break;
        }
    };

    this.generateFood = function() {
        var row;
        var col;

        do {
            row = floor(random(0, this.ROW_COUNT));
            col = floor(random(0, this.ROW_COUNT));
        } while(this.cells[row][col].getCellType() !== CellType.EMPTY);

        this.cells[row][col].setCellType(CellType.FOOD);

        return this.cells[row][col];
    };

    this.getNextCell = function(cell, direction) {
        var row = cell.ROW;
        var col = cell.COL;

        switch(direction) {
            case Direction.UP:
                row = (row - 1 < 0)? this.ROW_COUNT - 1 : row - 1;
                break;
            case Direction.DOWN:
                row = (row + 1) % this.ROW_COUNT;
                break;
            case Direction.LEFT:
                col = (col - 1 < 0)? this.COL_COUNT - 1 : col - 1;
                break;
            case Direction.RIGHT:
                col = (col + 1) % this.COL_COUNT;
                break;
        }

        return this.cells[row][col];
    };

    this.draw = function() {
        fill(Properties.Colors.GREEN);
        rect(0, 0, this.COL_COUNT * Properties.DRAW_SIZE, this.ROW_COUNT * Properties.DRAW_SIZE);
    };
};

var Snake = function(board) {
    this.body = [];
    this.direction = Direction.NONE;

    this.body.push(board.getCenterCell());
    this.body[0].setCellType(CellType.Snake.HEAD);
    this.body[0].setFacing(Direction.LEFT);

    this.body.push(board.getNextCell(this.body[0], Direction.RIGHT));
    this.body[1].setCellType(CellType.Snake.TAIL);
    this.body[1].setFacing(Direction.LEFT);

    this.getHead = function() {
        return this.body[0];
    };

    this.getTail = function() {
        return this.body[this.body.length - 1];
    };

    this.size = function() {
        return this.body.length;
    };

    this.getDirection = function() {
        return this.direction;
    };

    this.setDirection = function(direction) {
        this.direction = direction;
        this.getHead().setRotation(Rotation.getRotation(this.getHead().getFacing(), this.direction));
    };

    this.grow = function(food) {
        this.getHead().setCellType(CellType.Snake.BODY);
        this.getHead().setRotation(Rotation.getRotation(this.getHead().getFacing(), this.direction));
        this.getHead().setFacing(this.direction);

        food.setCellType(CellType.Snake.HEAD);
        food.setFacing(this.direction);

        this.body.unshift(food);
    };

    this.move = function(nextCell) {
        this.getHead().setCellType(CellType.Snake.BODY);
        this.getHead().setRotation(Rotation.getRotation(this.getHead().getFacing(), this.direction));
        this.getHead().setFacing(this.direction);

        this.getTail().setCellType(CellType.EMPTY);
        this.getTail().setRotation(Rotation.NONE);
        this.getTail().setFacing(Direction.NONE);

        nextCell.setCellType(CellType.Snake.HEAD);
        nextCell.setFacing(this.direction);

        this.body.unshift(nextCell);
        this.body.pop();

        this.getTail().setCellType(CellType.Snake.TAIL);
    };

    this.isMoving = function() {
        return this.direction !== Direction.NONE;
    };

    this.draw = function(step, board) {
        var rotation = Rotation.NONE;

        for(var i = 0; i < this.body.length; i++) {
            this.body[i].draw(step, rotation, board);

            rotation = this.body[i].getRotation();
        }
    };
};

var Game = function(speed) {
    this.board = new Board();
    this.snake = new Snake(this.board);
    this.food = this.board.generateFood();
    this.lastUpdateFrame = 0;
    this.deltaFrames = 0;
    this.framesToUpdate = Properties.FRAME_RATE / speed;

    this.setSnakeDirection = function(direction) {
        this.snake.setDirection(direction);
    };

    this.update = function() {
        this.deltaFrames = frameCount - this.lastUpdateFrame;

        if(this.deltaFrames < this.framesToUpdate) {
            return;
        } else {
            this.lastUpdateFrame = frameCount;
            this.deltaFrames = 0;
        }

        var nextCell = this.board.getNextCell(this.snake.getHead(), this.snake.getDirection());

        switch(nextCell.getCellType()) {
            case CellType.Snake.BODY:
                this.snake.setDirection(Direction.NONE);
                break;
            case CellType.FOOD:
                this.snake.grow(nextCell);

                if(this.snake.size() < this.board.cellsCount()) {
                    this.food = this.board.generateFood();
                } else {
                    this.food = null;
                }
                break;
            default:
                if(this.snake.isMoving()) {
                    this.snake.move(nextCell);
                }
                break;
        }
    };

    this.draw = function() {
        var step;

        if(this.snake.isMoving()) {
            step = this.deltaFrames / this.framesToUpdate;
        } else {
            step = 0;
        }

        this.board.draw();

        if(this.food) {
            this.food.draw();
        }

        this.snake.draw(step, this.board);
    };
};

frameRate(Properties.FRAME_RATE);

var game = new Game(Speed.NORMAL);

var draw = function() {
    game.update();
    background(255, 255, 255);
    game.draw();
};

keyReleased = function() {
    game.setSnakeDirection(keyCode);
};
