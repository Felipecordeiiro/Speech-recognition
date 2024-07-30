/* 
  Project: BioDatA in BioChallenge Brazil 2024
  Date: 2024-28-07
  Authors: Ermeson Alves, Felipe Cordeiro, Eduardo Monteiro
  Version: 1.0

  OBS: This code is based on https://electechoz.blogspot.com/2022/01/esp8266-webserver-controller-servo-motor.html?m=1 and examples
  for Generic ESP8266 Module.
*/

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <Servo.h>
#include <NTPClient.h>
#include <WiFiUdp.h>
#include "controlarm.h"
#define D1 5
#define D2 4
#define D3 0
#define D4 2
#define D5 14
#define D6 12
#define D7 13
#define ServoPIN1 D1
#define ServoPIN2 D2
#define ServoPIN3 D3
#define ServoPIN4 D4
#define ServoPIN5 D5


// Wifi setup
const char* ssid = "brisa-3464353";
const char* password = "mtm4xayu";
ESP8266WebServer server(80);

// Define NTP Client to get time
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org");

// Servos setup
Servo servo1; // base
Servo servo2;
Servo servo3;
Servo servo4; // garra
Servo servo5;

struct ArmStates currentStates;

void handleRoot() {
  String textoHTML;
  textoHTML = "Ola!! Aqui &eacute; o <b>ESP8266</b> falando! ";
  server.send(200, "text/html", textoHTML);
}

void handleNotFound(){
  String message = "Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET)?"GET":"POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i=0; i<server.args(); i++){
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
}

void handleCommand(){
  timeClient.update();
  String formattedTime = timeClient.getFormattedTime();
  time_t epochTime = timeClient.getEpochTime();
  String command;
  command += "\nArguments: ";
  command += server.args();
  command += "\n";
  String postBody = server.arg("plain");
  Serial.print("POST BODY:");
  Serial.print(postBody);
  Serial.print(" - ");
  Serial.print(epochTime);
  Serial.print(" | ");
  Serial.println(formattedTime);
  int moveID = postBody.toInt(); 
  currentStates = moveArm(moveID, servo1, servo2, servo3, servo4, servo5, currentStates);
  printArmStates(currentStates);

  // for (uint8_t i=0; i<server.args(); i++){
  //   command += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  //}
  server.send(200, "text/plain", command);

}

void setup(void){

  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print("Connecting...");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }

  // Initialize a NTPClient to get time
  timeClient.begin();
  timeClient.setTimeOffset(-10800);

  // HTTP routes
  server.on("/", handleRoot);
  server.on("/command", handleCommand);
  server.on("/inline", [](){
    server.send(200, "text/plain", "this works as well");
  });
  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("HTTP server started");

  // CONTROLE -----------------------------------
  // Definir as posições iniciais:
  currentStates.s1 = 0;
  currentStates.s2 = 0;
  currentStates.s3 = 0;
  currentStates.s4 = 0;
  currentStates.s5 = 0;

  servo1.attach(ServoPIN1);
  servo2.attach(ServoPIN2);
  servo3.attach(ServoPIN3);
  servo4.attach(ServoPIN4);
  servo5.attach(ServoPIN5);

  servo1.write(currentStates.s1);
  servo2.write(currentStates.s2);
  servo3.write(currentStates.s3);
  servo4.write(currentStates.s4);
  servo5.write(currentStates.s5);
  
}

void loop(void){
  server.handleClient();
  if(Serial.available()) // if there is data comming
  {
    int pos = Serial.readStringUntil('\n').toInt(); // read string until meet newline character
    servo1.write(pos);
    
  }
}
