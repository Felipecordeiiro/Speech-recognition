#ifndef ARMCONTROL_H
#define ARMCONTROL_H

int standardAngulation = 30;

// Estrutura para armazenar os estados dos servos do braço robótico
struct ArmStates {
    int s1;
    int s2;
    int s3;
    int s4;
    int s5;
};


#endif