class Nest {
  //Variables
  float x, y;
  float nestWidth = 100;
  float nestRad = nestWidth/2;
  int nestNum, birdCount;
  //Constructor
  Nest(int nestNumIn, float xIn, float yIn) {
    nestNum = nestNumIn;
    x= xIn;
    y= yIn;
  }

  void render() {
    fill(59, 144, 216);
    noStroke();
    ellipseMode(CENTER);
    ellipse(x, y, nestWidth*1.5, nestWidth*1.5);
    imageMode(CENTER);
    image(nestImg, x, y, 40, 30);
  }

  void update() {
    byeByeBirds();
    println("#" + nestNum +  " Birds: " +birdCount );
  }

  void updateBirdCount(int i) {
    birdCount = birdCount+i;
  }

  void byeByeBirds() {
    if (mouseX >= x - nestRad && mouseX <= x + nestRad && mouseY >= y - nestRad && mouseY <= y+ nestRad) {
      for (int i = 0; i < birds.size (); i++) {
        Bird myBird = (Bird) birds.get(i);

        myBird.changeNest(nestNum);
      }
      birdCount=0;
    }
  }

  float nestX() {
    return x;
  }

  float nestY() {
    return y;
  }

  void tooManyBirds() {
    for (int i = 0; i < birds.size (); i++) {
      Bird myBird = (Bird) birds.get(i);
    }
  }
}

