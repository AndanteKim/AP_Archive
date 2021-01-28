class EnemyField{
  
  // set basic coordinates
  float x;
  float y;
  int rows;
  int columns;

  // set basic speed about shot and dead to determine win and game over
  float speed = 0.1;
  float speed_rate = 0.05;
  //alienShootRate
  float EnemyShoot_speed = 0.001;
  //shootRate
  float shoot_speed;
  int dead;
  boolean GameOver;
  boolean win;

  ArrayList<ArrayList<Enemy>> enemies;
  ArrayList<Enemy> row_enemies;
  int enemy_size = 30;
  float enemy_space = 1.3;
  PImage enemy_image;
  boolean edge;
  Enemy enemy;
  
  
  EnemyField(float position_x, float position_y, int rows, int columns, PImage enemy_image){
    x = position_x;
    y = position_y;
    this.rows = rows;
    this.columns = columns;
    dead = 0;
    GameOver = false;
    win = false;
    this.enemy_image = enemy_image;
  }
  
  void init(){
    enemies = new ArrayList<ArrayList<Enemy>>();
    row_enemies = new ArrayList<Enemy>();
    
    for (int ro = 0; ro < this.rows; ro++){
      for (int col = 0; col < this.columns; col++){
        //the parentheses doesn't make sense here so fix the parentheses for the calculation
        //add(index, Object)
        Enemy each_enemy = new Enemy(((x - (this.columns * (enemy_size * enemy_space)) * 0.5
        + ((enemy_size * enemy_space) * col))), (y - (this.rows * (enemy_size * enemy_space)) * 0.75)
        + (enemy_size * enemy_space) * ro, enemy_size, enemy_image);
        row_enemies.add(each_enemy);
        //enemies.get(ro).set(col, each_enemy);
      }
      enemies.add(row_enemies);
    }
    shoot_speed = EnemyShoot_speed / ( this.rows * this.columns );
  }

  void create(){
    for (int ro = 0; ro < enemies.size(); ro++){
      for (int col = 0; col < enemies.get(ro).size(); col++){
        enemies.get(ro).get(col).create();
      }
    }
  }
  
  void update(){
    edge = false;
    
    shoot_speed = EnemyShoot_speed / ((this.rows * this.columns) - dead);
    if (dead == (this.rows * this.columns)){
      win = true;
    }
    
    for(int ro = 0; ro < enemies.size(); ro++){
      for(int col = 0; col < enemies.get(ro).size(); col++){
        enemies.get(ro).get(col).x += speed;
        if((enemies.get(ro).get(col).y + enemies.get(ro).get(col).size) > (height - player.size * 1.5)){
          GameOver = true;
        }
        else if(enemies.get(ro).get(col).y + enemies.get(ro).get(col).size > (height - player.size * 1.5) && ((enemies.get(ro).get(col).x + enemies.get(ro).get(col).size > width) || (enemies.get(ro).get(col).x - enemies.get(ro).get(col).size < 0))){
          GameOver = true;
        }
        else if(enemies.get(ro).get(col).x - enemy_size < 0 || enemies.get(ro).get(col).x + enemy_size > width){
          if(((enemies.get(ro).get(col).y + enemy_size > height - player.size * 1.5))){
            GameOver = true;
          }
        }
        else if(enemies.get(ro).get(col).x - enemy_size < 0 || enemies.get(ro).get(col).x + enemy_size > width){
          GameOver = true;
        }
        if(((enemies.get(ro).get(col).x + enemies.get(ro).get(col).size) > width - 40 || ( enemies.get(ro).get(col).x - enemies.get(ro).get(col).size ) < 30) && (enemies.get(ro).get(col).hit == false)){
          edge = true;
          enemies.get(ro).get(col).hit = true;
        }
      }
      
    }
     // when enemies hit the edge,
     if(edge == true){
      
      for(int row = 0; row < enemies.size(); row++){
        for(int col = 0; col < enemies.get(row).size(); col++){
          enemies.get(row).get(col).y += enemy_size;
        }
      }
      speed *= -1;
      y += enemy_size;
      
    }
    x += speed;
  }
  
// need to review this part
  void EnemyShoot(ArrayList <Bullet> bullets){
    for (int ro = 0; ro < enemies.size(); ro++){
      for (int col = 0; col < enemies.get(ro).size(); col++){
        if(!enemies.get(ro).get(col).hit){
          enemies.get(ro).get(col).shoot(bullets, EnemyShoot_speed/4);
        }
      }
    }
  }
  
  int EnemyHit(ArrayList <Bullet> bullets){
    for(int ro = enemies.size() - 1; ro >= 0; ro--){
      for(int col = enemies.get(ro).size() - 1; col >= 0; col--){
        for(int cnt = (bullets.size())-1; cnt >= 0; cnt--){
          if(bullets.get(cnt).player){
            if (((bullets.get(cnt).x + bullets.get(cnt).w * 0.5) >= ( enemies.get(ro).get(col).x - enemies.get(ro).get(col).size * 0.5) && 
                ((bullets.get(cnt).x - bullets.get(cnt).w * 0.5) <= ( enemies.get(ro).get(col).x + enemies.get(ro).get(col).size * 0.5))) && 
                ((bullets.get(cnt).y + bullets.get(cnt).h * 0.5) <= ( enemies.get(ro).get(col).y + enemies.get(ro).get(col).size * 0.5) && 
                (bullets.get(cnt).y - bullets.get(cnt).h * 0.5) >= ( enemies.get(ro).get(col).y - enemies.get(ro).get(col).size * 0.5))){
              enemies.get(ro).remove(col); //enemies[1][2] => delete enemies second column in first row.
              
              ++dead;
              if (speed < 0){
                speed -= 0.3*speed_rate;
              }
              else{
                speed += 0.3*speed_rate;
              }
              bullets.remove(cnt);
              return 10;
            }
          }
        }
      }
    }
    return 0;
  }
  
  void reset(float position_x, float position_y, int rows, int columns, PImage enemy_image){
    x = position_x;
    y = position_y;
    
    this.rows = rows;
    this.columns = columns;
    
    speed = 1;
    
    enemies = new ArrayList<ArrayList<Enemy>>();
    enemy_size = 30;
    this.enemy_image = enemy_image;
    GameOver = false;
    dead = 0;
    win = false;
    
    init();
  }
}
