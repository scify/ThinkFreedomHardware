const int Button =4;
int State_before;

void setup() {

  pinMode(Button, INPUT);
  Keyboard.begin();
}

void loop() {
  int State = digitalRead(Button);
  //if the button is pressed
  if(State==HIGH && State_before==LOW){
    
    Keyboard.write('a');
  }
  State_before=State;
}

