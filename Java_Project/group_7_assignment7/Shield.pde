class Shield {
  float x, y;
  int rows, cols, segmentSize;
  ShieldSegment[][] segments;
    
  Shield(float x, float y){
     this.x = x;
     this.y = y;
     rows = 5;
     cols = 10;
     segmentSize = 5;
     segments = new ShieldSegment[rows][cols];
     for (int r = 0; r < rows; r++){
       for (int c = 0; c < cols; c++){
        segments[r][c] = new ShieldSegment(c * segmentSize, r * segmentSize, segmentSize); 
       }
     }
    }
    
    void init(){
      segments = new ShieldSegment[rows][cols];
      for (int r = 0; r < this.rows; r++){
       for (int c = 0; c < this.cols; c++){
        segments[r][c] = new ShieldSegment(c * segmentSize, r * segmentSize, segmentSize); 
       }
     }
    }
    
    void render(){
      push();
      translate(this.x-(this.cols*segmentSize)/2, this.y - (this.rows*segmentSize)/2);
        for(int r = 0; r < rows; r++) {
            for(int c = 0; c < cols; c++) {
                segments[r][c].render();
            }
        }
      pop();
      
    }
    

    void update(ArrayList <Bullet> bullets){
      for(int r = 0; r < rows; r++) {
            for(int c = 0; c < cols; c++) {
                segments[r][c].checkHit(bullets, this.x - (this.cols*segmentSize)/2, this.y - (this.rows*segmentSize)/2);
            }
        }
    }
    
    void reset(){
      for(int r = 0; r < rows; r++) {
            for(int c = 0; c < cols; c++) {
                segments[r][c].hit = false;
            }
        }
    }
}
