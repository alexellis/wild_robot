#include <Servo.h>
char msg[26];
char *ptr;
int cmds[6];

#define SERVO_1 0
#define SERVO_2 1
#define MOTOR_1 2
#define MOTOR_2 3
#define MOTOR_3 4
#define MOTOR_4 5

#define grip_pin 10
#define arm_pin 11
#define motor_enable_pin 2
#define IN1_L  3
#define IN2_L  5
#define IN3_R  6
#define IN4_R  9

Servo grip;
Servo arm;

void setup() {
  Serial.begin(9600);
  grip.attach(grip_pin);
  arm.attach(arm_pin);
  
  pinMode(IN1_L, OUTPUT);
  pinMode(IN2_L, OUTPUT);
  pinMode(IN3_R, OUTPUT);
  pinMode(IN4_R, OUTPUT);
  
  setGrip(90);
  setArm(90);
  enableMotors();
  setMotors();
}

void setGrip(int val) {
 grip.write(val); 
}
void setArm(int val) {
 arm.write(val);
}

void resetMsg() {
  for (int i = 0; i < 26;i++) {
    msg[i] = '\0';
  }
  for(int i=0;i<6;i++) {
    cmds[i]=-1; 
  }
  ptr = msg;
}
/*
#090,090,100,000,100,000
*/

int parseMsg() {
 char* reading = strtok(msg, ",");
 int count=0;
 
 while(reading != 0) {
   int value = atoi(reading);
   
   cmds[count++] = value;
   
   //Serial.print("Val: ");
   //Serial.print(reading);
   //Serial.print(" ");
   //Serial.println(value);
   reading = strtok(0, ",");
 }
 return count;
}
void enableMotors() {
 digitalWrite(motor_enable_pin, 1); 
}

void setMotors() {
  analogWrite(IN1_L, cmds[MOTOR_1]);
  analogWrite(IN2_L, cmds[MOTOR_2]);
   
  analogWrite(IN3_R, cmds[MOTOR_3]);
  analogWrite(IN4_R, cmds[MOTOR_4]);
}

void processMsg() {
// //Serial.print("SERVO_1: ");
 setArm(cmds[SERVO_1]);
// //Serial.println(cmds[SERVO_1]);
// //Serial.print("SERVO_2: ");
// //Serial.println(cmds[SERVO_2]);
 setGrip(cmds[SERVO_2]);
 for (int i = MOTOR_1;i <= MOTOR_4;i++){
   Serial.print("Motor");
   Serial.print(i);
   Serial.print(": ");
   Serial.println(cmds[i]);
 }

  setMotors();
}

void loop() {
  if(Serial.available() > 0) {
    char ch = Serial.read();
    if(ch == '#') {
      resetMsg();
      //Serial.write("New msg");
    }
    else {
       int len=strlen(msg);
       if(len < 23) {
        *ptr=ch;
        ptr++;
       }
       if(len==22) {
         //Serial.write(msg);
         //Serial.write("\n");
         
         int count = parseMsg();
         if(count == 6) {
           processMsg();
         } else {
           //Serial.println("Bad message");
         } 
       }
    }
  }
}
