"""Una puerta requiere 4 llaves (A, B, C y D) que pueden ser ON / OFF

La puerta abrira si se cumple alguna de las siguientes condiciones:

A y B son iguales
C es ON
C y D son distintos
A y D son ON
B y D son OFF
El programa recibe los cuatro estados y muestra si la puerta se abre o no."""

puerta_A=input("puerta A esta en off/on ? :")
puerta_B=input("puerta B esta en off/on ? :")
puerta_C=input("puerta C esta en off/on ? :")
puerta_D=input("puerta D esta en off/on ? :")

if puerta_A == puerta_B