float vout,vout1,temp;
int motion=0;

void setup() {
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(A1,INPUT);
  pinMode(A0,INPUT);
  pinMode(4,INPUT);
  pinMode(7,OUTPUT);
  pinMode(13,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  vout=analogRead(A0);
  vout1=(vout/1023)*5000;
  temp=(vout1-500)/10;
  motion=digitalRead(4);
  
  int ldrStatus = analogRead(A1);

  if (ldrStatus <= 500)
  {
    digitalWrite(2, HIGH);
    Serial.print("Its Dark, Turn on the LED:");
    Serial.println(ldrStatus);

  }
  else
  {
    digitalWrite(2, LOW);
    Serial.print("Its Bright, Turn off the LED:");
    Serial.println(ldrStatus);
  }

  
  Serial.print("Current Temperature: ");
  Serial.print(temp);
  Serial.println();
  
  if(temp>60){
    digitalWrite(7,HIGH);
    digitalWrite(13,HIGH);
  }
  else{
    digitalWrite(7,LOW);
    digitalWrite(13,LOW);
  }
  
  if(motion == HIGH){
    digitalWrite(7,HIGH);
    digitalWrite(13,HIGH);
    Serial.println("Motion is detected");
  }
  else{
     digitalWrite(7,LOW);
     digitalWrite(13,LOW);
     Serial.println("Motion is not detected");
}
  delay(1000);
}
