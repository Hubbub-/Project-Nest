class Nest {
  //Variables
  float x, y;
  //Constructor
  Nest(float xIn, float yIn) {
    x= xIn;
    y= yIn;
  }

  void render() {
    fill(59, 144, 216);
    noStroke();
    ellipseMode(CENTER);
    ellipse(x, y, 60, 60);
    imageMode(CENTER);
    image(nestImg, x, y, 40, 30);
  }


  void update() {
  }
}

