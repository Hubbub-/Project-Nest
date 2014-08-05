class Bird {
  int currentNest, targetNest; 
  PVector location;
  PVector targetNestLocation;
  PVector velocity;
  PVector acceleration;
  float topspeed;
  boolean inFlight;


  Bird(int nestIn, float xIn, float yIn) {
    currentNest = nestIn;
    inFlight = false;
    location = new PVector(xIn+ random(-30, 30), yIn+ random(-30, 30));
    targetNestLocation = new PVector(location.x, location.y);
    velocity = new PVector(0, 0);
    topspeed = random(3, 5);
  }

  void render() {
    imageMode(CENTER);
    image(birdImg, location.x, location.y);
  }


  void update() {
    if (inFlight) {
      flying();
      reachedTargetNest();
    }
  }


  void changeNest(int nestNum) {
    if (currentNest == nestNum) {
      targetNest = int(random(0, 4.9));
      if (targetNest == currentNest) {
        targetNest = int(random(0, 4.9));
      }
      Nest myNest = (Nest) nests.get(targetNest);
//      myNest.updateBirdCount(1);
      targetNestLocation.set(myNest.nestX()+ random(-25, 25), myNest.nestY()+ random(-25, 25));
      PVector dir = PVector.sub(targetNestLocation, location);  // Find vector pointing towards mouse
      dir.normalize();     // Normalize
      dir.mult(random(.4, .6));       // Scale 
      acceleration = dir;  // Set to acceleration
      inFlight = true;
    }
  }

  void flying() {
    velocity.add(acceleration);
    velocity.limit(topspeed);
    location.add(velocity);
    currentNest = targetNest;
    //    inFlight = false;
  }

  void reachedTargetNest() {
    if (location.dist(targetNestLocation) <= 30) {
      inFlight = false;
    }
  }

  int nestNumber() {
    return currentNest;
  }
}

