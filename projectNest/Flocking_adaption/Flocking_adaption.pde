//Libaries

//Variables
float r1 = 1.0; // attract to eachother
float r2 = 0.8; //keep members seperate 
ArrayList <Nest> nests;
ArrayList <Bird> birds;
int totalNestCount = 5;
int maxBPN = 5;
PImage birdImg, nestImg; 
//Window size
int windowWidth = 500;
int windowHeight = 500;
int x;
int y;

//Setup
void setup() {
  size(windowWidth, windowHeight);
  nests = new ArrayList <Nest> ();
  birds = new ArrayList <Bird> ();
  frameRate(60);
  birdImg = loadImage("bird.png");
  nestImg = loadImage("nest.png");


  //Nest count
  for (int i = 0; i <= totalNestCount-1; i++) {
    if (i == 0) {
      x = 100;
      y = 100;
    }
    if (i == 1) {
      x=350;
      y=150;
    }
    if (i == 2) {
      x=150;
      y=250;
    }
    if (i == 3) {
      x=400;
      y=350;
    }
    if (i == 4) {
      x=250;
      y=400;
    }
    nests.add (new Nest(i, x, y));
    int birdCount = int(random(0, maxBPN));
    Nest myNest = (Nest) nests.get(i);
    myNest.updateBirdCount(birdCount);
    
    for (int k = 1; k <= birdCount; k++) {
      birds.add (new Bird(i, x, y));
    }
    println("birdCount" + birds.size());
  }
}




//Update
void draw() {
  background(180, 248, 255);
  for (int i = 0; i < nests.size (); i++) {
    Nest myNest = (Nest) nests.get(i);

    myNest.update();
    myNest.render();
  }

  for (int i = 0; i < birds.size (); i++) {
    Bird myBird = (Bird) birds.get(i);

    myBird.update();
    myBird.render();
  }
}

