class Bullet {
  // set x and y coordinates
  float x;
  float y;
  // width, height, and speed for a plane
  int w;
  int h;
  int speed;
  boolean player;
  
  Bullet(float position_x, float position_y, boolean player){
    x = position_x;
    y = position_y;
    
    w = 5;
    h = 10;
    speed = 8;
    this.player = player;
    
  }
    
  void create() {
    rectMode(CENTER);
    noStroke();
        
    if(this.player) {
        fill(0,255,0);
    }
    else {
        fill(255);
    }    
    rect(x, y, w, h);
  }
    
  void update(){
    if(this.player){
        y -= speed;
    } 
    else{
        y += speed * 0.5 ;
    }
  }
    
  boolean despawn(){
    if(this.player) {
       if(y < -h) {
           return true;
       }
    }
    else {
       if(y > height + h) {
           return true;
       }
    } 
    return false;
  }
}
