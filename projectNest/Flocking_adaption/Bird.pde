class Bird {
  int currentNest, targetNest; 
  float x, y, targetX, targetY;
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
    if (inFlight) {
      flying();
    }
  }


  void changeNest(int nestNum) {
    if (currentNest == nestNum) {
      targetNest = int(random(0, 4.9));
      if (targetNest == currentNest) {
        targetNest = int(random(0, 4.9));
      }
      Nest myNest = (Nest) nests.get(targetNest);
      targetX = myNest.nestX();
      targetY = myNest.nestY();
    }
    inFlight = true;
    println("moving!");
  }
  
  void flying() {
  x= targetX+ random(-30, 30);
  y= targetY+ random(-30, 30);
  currentNest = targetNest;
  inFlight = false;
}
  
  
}


