class Bird {
  int currentNest, targetNest; 
  float x, y;
  boolean inFlight;


  Bird(int nestIn, float xIn, float yIn) {
    currentNest = nestIn;
    inFlight = false;
    x= xIn+ random(-30, 30);
    y= yIn+ random(-30, 30);
  }

  void render() {
    imageMode(CENTER);
    image(birdImg, x, y);
  }


  void update() {
    flying();
  }


void changeNest(int nestNum) {
  if (currentNest == nestNum) {
    targetNest = int(random(1, 5.9));
    if (targetNest == currentNest) {
      targetNest = int(random(1, 5.9));
    }
    inFlight = true;
    println("moving!");
  }
}
void flying() {
  
}

}


