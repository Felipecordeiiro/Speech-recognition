// Struct de estados dos servos (usados para verificar se o movimento é permitido ou controla-los)


ArmStates moveArm(int moveID, Servo& servo1, Servo& servo2, Servo& servo3, Servo& servo4, Servo& servo5, ArmStates& currentStates) {
  if (moveID == 0) {
    currentStates = leftFunction(servo1, servo2, servo3, servo4, servo5, currentStates);
  }
  else if (moveID == 1) {
    currentStates = rightFunction(servo1, servo2, servo3, servo4, servo5, currentStates);
  }
  else if (moveID == 2) {
    currentStates = downFunction(servo1, servo2, servo3, servo4, servo5, currentStates);
  }
  else if (moveID == 3) {
    currentStates = upFunction(servo1, servo2, servo3, servo4, servo5, currentStates);
  }
  else if (moveID == 4) {
    currentStates = openClaw(servo1, servo2, servo3, servo4, servo5, currentStates);
  }
  else if (moveID == 5) {
    currentStates = closeClaw(servo1, servo2, servo3, servo4, servo5, currentStates);
  }
  else if (moveID == 6) {
    currentStates = brushing(servo1, servo2, servo3, servo4, servo5, currentStates);
  }

  return currentStates;
}


// Movimentos: -----------------------------------------------------------------------


// Controle do servo1, que corresponde a base
ArmStates leftFunction(Servo& servo1, Servo& servo2, Servo& servo3, Servo& servo4, Servo& servo5, ArmStates& currentStates) {
  int pos1 = currentStates.s1 + standardAngulation;
  // caso a posição tenha angulação maior que 180, o estado não é alterado
  // OOOU ===> setar para 180
  if (pos1 > 180) {
    return currentStates;
  }
  else {
    Serial.println("VOU MOVER O BRAÇO PARA A ESQUERDA...");
    servo1.write(pos1); // movimento pra esquerda -> s1 + angulo padrão (mais)
  }

  currentStates.s1 = pos1;

  return currentStates;
} 



// Controle do servo1, que corresponde a base
ArmStates rightFunction(Servo& servo1, Servo& servo2, Servo& servo3, Servo& servo4, Servo& servo5, ArmStates& currentStates) {
  int pos1 = currentStates.s1 - standardAngulation;
  // caso a posição tenha angulação menor que 0, o estado não é alterado
  // OOOU ===> setar para 0 
  if (pos1 < 0) {
    return currentStates;
  }
  else {
    Serial.println("VOU MOVER O BRAÇO PARA A DIREITA...");
    servo1.write(pos1); // movimento pra direita -> s1 - angulo padrão (menos)
  }

  currentStates.s1 = pos1;

  return currentStates;
}



ArmStates downFunction(Servo& servo1, Servo& servo2, Servo& servo3, Servo& servo4, Servo& servo5, ArmStates& currentStates) {
  return currentStates;
}



ArmStates upFunction(Servo& servo1, Servo& servo2, Servo& servo3, Servo& servo4, Servo& servo5, ArmStates& currentStates) {
  return currentStates;
}



ArmStates openClaw(Servo& servo1, Servo& servo2, Servo& servo3, Servo& servo4, Servo& servo5, ArmStates& currentStates) {
  return currentStates;
}



ArmStates closeClaw(Servo& servo1, Servo& servo2, Servo& servo3, Servo& servo4, Servo& servo5, ArmStates& currentStates) {
  return currentStates;
}



ArmStates brushing(Servo& servo1, Servo& servo2, Servo& servo3, Servo& servo4, Servo& servo5, ArmStates& currentStates) {
  return currentStates;
}



void printArmStates(const ArmStates& states) {
    Serial.print("s1: ");
    Serial.println(states.s1);
    Serial.print("s2: ");
    Serial.println(states.s2);
    Serial.print("s3: ");
    Serial.println(states.s3);
    Serial.print("s4: ");
    Serial.println(states.s4);
    Serial.print("s5: ");
    Serial.println(states.s5);
}