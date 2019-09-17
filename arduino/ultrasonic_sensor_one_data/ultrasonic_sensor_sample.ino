#define echoPin 2 // Echo Pin
#define trigPin 3 // Trigger Pin

double Duration = 0; //受信した間隔
short int Distance = 0; //距離
char incomingByte = 0;
void setup() {
Serial.begin( 9600 );
pinMode( echoPin, INPUT );
pinMode( trigPin, OUTPUT );
}
void loop() {
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2); 
  digitalWrite( trigPin, HIGH ); //超音波を出力
  delayMicroseconds( 10 ); //
  digitalWrite( trigPin, LOW );
  Duration = pulseIn( echoPin, HIGH ,50000); //センサからの入力
  //Serial.println(Duration);
  if (Duration > 0) {
    Duration = Duration/2; //往復距離を半分にする
    Distance = Duration*340*100/1000000; // 音速を340m/sに設定
    //Serial.println(Distance);
  }

  if (Serial.available() > 0){
    incomingByte = Serial.read();
    if (incomingByte == '1'){
      //Serial.print(100);
      //Serial.write(100);
      Serial.println(Distance);
    }
  }
  delay(500);
}
