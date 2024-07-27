char cmd;                     //Define a variável dos comandos seriais

void setup() {
  Serial.begin(9600);         //Inicia o Monitor Serial
  pinMode(2, OUTPUT);         //Define o pino como saída
  digitalWrite(2, LOW);
}

void loop() {
  cmd = Serial.read(); // Lê o comando do Python
  // Serial.print("Recebi: "); // Responde ao comando
  Serial.println(cmd);
  if (cmd == 'l') {           //Se o comando for "l", liga o led
    digitalWrite(2, HIGH); 
  }

  else if (cmd == 'd') {      //Se o comando for "d", desliga o led
    digitalWrite(2, LOW);
  }
}