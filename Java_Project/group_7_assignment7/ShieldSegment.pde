class ShieldSegment{
  float x, y;
  int size;
  boolean hit;
  
  ShieldSegment(float x, float y, int size){
     this.x = x;
     this.y = y;
     this.size = size;
     hit = false;
    }
    
    void render(){
     if (!hit){
       fill(0, 255, 0);
       stroke(0, 255, 0);
       rectMode(CENTER);
       rect(this.x, this.y, this.size, this.size);
     }
    }
    
    void checkHit(ArrayList <Bullet> bullets, float x, float y){
      if(!hit){
       for (int count = bullets.size() - 1; count >= 0; count --){
         if(!bullets.get(count).player){
          if((bullets.get(count).x >= (x+this.x)-this.size/2 && 
          bullets.get(count).x <= (x+this.x)+this.size/2) && 
          (bullets.get(count).y+bullets.get(count).h >= (y+this.y) - this.size/2 && 
          bullets.get(count).y-bullets.get(count).h <= (y+this.y) + this.size/2)) {
            hit = true;
            bullets.remove(count);
         }
      }
    }
      
      }
    }
}
