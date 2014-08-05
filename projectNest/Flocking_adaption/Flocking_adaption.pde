//Libaries

//Variables
Cell[][] grid;
float r1 = 1.0; // attract to eachother
float r2 = 0.8; //keep members seperate 
ArrayList <Nest> nests;
int totalNestCount = 5;
PImage birdImg, nestImg; 
//Window size
int windowWidth = 400;
int windowHeight = 400;

int cols = 3;
int rows = 3;



//Setup
void setup() {
  size(windowWidth, windowHeight);
  nests = new ArrayList <Nest> ();
  frameRate(60);
  birdImg = loadImage("bird.png");
  nestImg = loadImage("nest.png");

  grid = new Cell[cols][rows];
  for (int i = 0; i < cols; i++) {
    for (int j = 0; j < rows; j++) {
      // Initialize each object
      grid[i][j] = new Cell(i*20, j*20, 20, 20);
    }
  }
  //Nest count
  for (int i = 1; i <= totalNestCount; i++) {
    nests.add (new Nest(random(0, width), random(0, height)));
  }
}




//Update
void draw() {
  background(180, 248, 255);
  for (int i = 0; i < nests.size (); i++) {
    Nest myNest = (Nest) nests.get(i);
    println("yes"); 
    myNest.update();
    myNest.render();
  }
  for (int i = 0; i < cols; i++) {
    for (int j = 0; j < rows; j++) {
      // Oscillate and display each object
      grid[i][j].render();
    }
  }

  //r1 = Pull to center of flock
}

