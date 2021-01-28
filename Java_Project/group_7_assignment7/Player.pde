class Player{
    int size;
    float x;
    float y;
    int h;
    int lives;
    int score;
    
    int speed;
    
    boolean moveLeft;
    boolean moveRight;
    
    boolean gameOver;
    
    Player() {
      size = 30;
      x = width/2;
      y = height - (70 + size);
      h = 10;
      lives = 3;
      score = 0;
      speed = 5;
      moveLeft = false;
      moveRight = false;
      gameOver = false;
    }
    
    void create(){
        rectMode(CENTER);
        
        fill(0, 255, 0);
        noStroke();
        rect(x, y, size, h);
        rect(x, y-6, 5, 5);
        
        pushMatrix();
        translate(width/2, height/2);
        stroke(255, 0, 0);
        fill(255, 0, 0);
        for (int i = 0; i < this.lives; i ++) {
          beginShape();
            for (float a = 0; a < TWO_PI; a += 0.01){
             float x = 16 * pow(sin(a), 3) - 300;
             float y = -1 * (13 * cos(a) - 5 * cos(2*a) - 2*cos(3*a) - cos(4 * a)) + 300;
             vertex(x + i * (this.size +10), y + 20);
            }
           endShape(); 
          }
         popMatrix();
        
    textAlign(BASELINE);
    fill(255);
    textSize(20);
    text("Score: " + score, 15, 50); 
    }
    

    void update() {
        if(moveLeft) {
            move(-1);
        } else if(moveRight) {
            move(1);
        }
        
        if(x < 0) {
            x = width;
        }
        
        if(x > width) {
            x = 0;
        }
        
        if(lives <= 0) {
            gameOver = true;
        }
    }
    
    void move(int speedMult) {
        x += (speed*speedMult);
    }
    
    Bullet shoot() {
      
      Bullet bullet = new Bullet(x, y, true); 
      return bullet;
    }
    
    void hit(ArrayList<Bullet> bullets) {
        for(int i = bullets.size()-1; i >= 0; i--) {
            if(!bullets.get(i).player) {
                if((bullets.get(i).x > x-size/2 && bullets.get(i).x < x+size/2) && (bullets.get(i).y > y-h/2 && bullets.get(i).y < y+h/2)) {
                    bullets.remove(i);
                    lives--;
                }
            }
        }
    }
    
    void reset() {
        size = 30;
        x = width/2;
        y = height-(70 + size);
        h = 10;
        lives = 3;
        score = 0;
    
        speed = 5;
    
        moveLeft = false;
        moveRight = false;
        
        gameOver = false;
        bullets.clear();
    }
} 
