#ifndef _MODERATE_EXAMPLE_H
#define _MODERATE_EXAMPLE_H

#include "./subfolder/moderate_example_subfolder.h"

extern "C" {
	__declspec( dllexport )void foo1();
	__declspec( dllexport )int foo2();
	__declspec( dllexport )float foo3();
	__declspec( dllexport )double foo4();
	__declspec( dllexport )char foo5();
}
extern "C" {
	__declspec( dllexport )void* foo6();
	__declspec( dllexport )int* foo7();
	__declspec( dllexport )float* foo8();
	__declspec( dllexport )double* foo9();
	__declspec( dllexport )char* foo10();
}
extern "C" {
	__declspec( dllexport )void* foo11(void* param);
	__declspec( dllexport )int* foo12(int* param, int param2);
	__declspec( dllexport )float* foo13(float* param, float param2);
	__declspec( dllexport )double* foo14(double* param, double param2);
	__declspec( dllexport )char* foo15(char* param, char param2);
}
#endif