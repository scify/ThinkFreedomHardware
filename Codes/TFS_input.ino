
const int Button1 = 9;
const int Button2 = 8;
int State2_before;
int State1_before;

void setup(){
pinMode(Button1, INPUT);
pinMode(Button2, INPUT);

Serial.begin(9600);
}

void loop(){
  
  int State1 = digitalRead(Button1);
  int State2 = digitalRead(Button2);

//Serial.println(State2);
  
      if (State2==HIGH && State2_before==LOW){
       Serial.println("a");
        delay(200);
         }
      if (State1==HIGH && State1_before==LOW){
       Serial.println("a");
        delay(200);
     
      }
     State2_before=State2;
     State1_before=State1;
    }
