//heart display for lives inspired by: https://github.com/CodingTrain/website/blob/main/CodingChallenges/CC_134_Heart_Curve_1/Processing/CC_134_Heart_Curve_1/CC_134_Heart_Curve_1.pde

class Status {
  int score, lives;
  float x, y;
  float a = 0;
  int size = 30;
  int rectX, rectY;
  int num_shield;
  EnemyField enemy;
  ArrayList<Shield> shields;
  ArrayList<Bullet> bullets;
  
  void display_restart(){
    }
  Status(int score, int lives, int num_shield, ArrayList<Shield> shields, ArrayList<Bullet> bullets, EnemyField enemy){
   this.score = score;
   this.lives = lives;
   this.num_shield = num_shield;
   this.shields = shields;
   this.bullets = bullets;
   this.enemy = enemy;

  }
  
  void restart() {
    player.reset();
    enemy.reset(width/2, height/4, enemy.rows, enemy.columns, enemy.enemy_image);
    
    for(int i = 0; i < num_shield; i++) {
        shields.get(i).reset();
    }
    
    bullets = new ArrayList<Bullet>();
   
    enemy.speed = 0.01;
    }
    
  
  void restart_display() {
    fill(255, 0, 0);
    rectMode(CENTER);
    rect(width/2, height/2 + 130, 150, 70);
    fill(255);
    textSize(25);
    text("RESTART", width/2, height/2 + 130);

  }
  
  boolean restart_pressed(){
    if (mousePressed){
    if (mousePressed) {   if (mouseX >= 275 && mouseX <= 525 && 
        mouseY >= 470 && mouseY <= 540) {
         restart();
        } 
      }}
      return false;
  }
  
  void win(int player_score){
    textSize(width/10);
        fill(255);
        textAlign(CENTER, CENTER);
        text("Winner!", width/2, height/2-width/10);
        text("Score: " + player_score, width/2, height/2);
        restart_display();
        restart_pressed();
  }
  void lose(int player_score){
    textSize(width/10);
        fill(255);
        textAlign(CENTER, CENTER);
        text("Game Over!", width/2, height/2-width/10);
        text("Score: " + player_score, width/2, height/2);
        restart_display();
        restart_pressed();
  }
  
}
