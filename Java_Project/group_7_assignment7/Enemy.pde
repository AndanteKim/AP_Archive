class Enemy{
  float x;
  float y;
  int size;
  boolean hit;
  PImage enemy_image;
  Enemy(float position_x, float position_y, int size, PImage enemy_image){
    x = position_x;
    y = position_y;
    this.size = size;
    hit = false;
    this.enemy_image = enemy_image;
  }
  
  void create(){
    imageMode(CENTER);
    image(enemy_image, x, y, this.size, this.size);
  }
  
  void shoot(ArrayList <Bullet> bullets, float shootRate){
    if (random(0, 1) < shootRate){
      
      Bullet each_bullet = new Bullet(x, y, false);
      bullets.add(each_bullet);
    }
  }
  
}
