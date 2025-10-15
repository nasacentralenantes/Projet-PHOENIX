#include <Servo.h>

//Initialisation des Pins (Numéros à définir)
const int LED_seq_actif = 1;
const int LED_act_actif = 2;

const int Decl = 9;
const int Info_Decl = 3;
const int Jack_Deco = 4;

float T = 17.5;       // Instant déclenchement prévue (en s)
float T1 = 0.80*T;    // Instant avant lequel on ne peut pas déclencher (en s)
float T2 = 1.20*T;    // Instant de déclenchement obligatoire (en s)

bool Deco = 0;        // Bool qui vaut 0 si on a pas décollé, 1 si on a décollé
unsigned long T_Deco = 0; // Instant de décollage (millis)
unsigned long T_Vol = 0; // Durée depuis le décollage

Servo servoMotor;

void Initialisation_Declenchement(){
  servoMotor.attach(Decl);
  servoMotor.write(0);
  digitalWrite(LED_act_actif, LOW);
}

void Declenchement_parachute(){
  servoMotor.write(180);
  digitalWrite(LED_act_actif, HIGH);
}

void setup() {
  pinMode(LED_seq_actif, OUTPUT);
  pinMode(LED_act_actif, OUTPUT);

  pinMode(Info_Decl, INPUT_PULLUP);
  pinMode(Jack_Deco, INPUT_PULLUP);

  Initialisation_Declenchement();
  digitalWrite(LED_seq_actif, LOW);
}

void loop() {
  
  if(digitalRead(Jack_Deco) && !Deco){
    Deco = 1;
    T_Deco = millis();
    digitalWrite(LED_seq_actif, HIGH);
  }

  if(Deco){
    T_Vol = millis() - T_Deco;
    if((!digitalRead(Info_Decl) && T_Vol >= 1000*T1) || T_Vol >= 1000*T2){
      Declenchement_parachute();
    }

  }

}
