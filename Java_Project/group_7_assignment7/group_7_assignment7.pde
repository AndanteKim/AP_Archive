// Andrew's part
// set up basic factors
ArrayList<Bullet> bullets;
ArrayList<Shield> shields;
int num_shield = 4;
int enemy_columns = 10;
int enemy_rows = 5;

// each enemy fields and shield and enemy's image
EnemyField enemy_range;
Shield each_shield;
PImage enemy_image;

//laura
Status status;
int score = 0;
int lives = 3;
int hitBullets = 0;
color rectColor;
boolean pressed = false;

//jaeho
int pixelsize = 4;
int gridsize  = pixelsize * 7 + 5;
Player player;
int direction = 1;
boolean incy = false;
PFont f;

void setup(){
  size(700, 750);
  player = new Player();
  enemy_image = loadImage("alien.png");
  enemy_range = new EnemyField(width/2, height/4, enemy_rows, enemy_columns, enemy_image);
  enemy_range.init();
  shields = new ArrayList<Shield>();
  bullets = new ArrayList<Bullet>();
  
  for(int i = 0; i < num_shield; i++){
    each_shield = new Shield(width*0.1+((width*0.8)/(num_shield-1)*i), height-150);
    shields.add(each_shield);
  }
  
  status = new Status(score, lives, num_shield, shields, bullets, enemy_range);
  

}
  

void draw(){
  background(0);

  if(!player.gameOver && !enemy_range.GameOver && !enemy_range.win){
    for(int i = bullets.size()-1; i>=0 ; i--){
      bullets.get(i).update();
      bullets.get(i).create();
      
      if(bullets.get(i).despawn()){
        bullets.remove(i);
      }
    }
    
    for(int i = 0; i < num_shield; i++){
      shields.get(i).render();
      shields.get(i).update(bullets);
    }
    
    enemy_range.update();
    player.score += enemy_range.EnemyHit(bullets);
    enemy_range.EnemyShoot(bullets);
    enemy_range.create();
    
    player.create();
    player.update();
    player.hit(bullets);
    
 }
 else if (!enemy_range.win && (player.gameOver || enemy_range.GameOver)){
   status.lose(player.score);
 }
 else if (enemy_range.win){
   status.win(player.score);
 }
}

void keyPressed() {
    switch(key) {
        case 'a':
        case 'A':
            player.moveLeft = true;
            break;
        case 'd':
        case 'D':
            player.moveRight = true;
            break;
            
        // spacebar is attack key
        case ' ':
            bullets.add(player.shoot());
            break;

    }
}

void keyReleased() {
    switch(key) {
        case 'a':
        case 'A':
            player.moveLeft = false;
            break;
        case 'd':
        case 'D':
            player.moveRight = false;
            break;
    }
}
