/*--------------------------------------------------------------*
               TableCurve 3D C Code Output
            To modify generated output, edit C.TCL
*--------------------------------------------------------------*/

#include <math.h>
#include <stdio.h>

double eqn27792396(double x, double y);

void main(void)
{
  double x,y,z;
  char str[80];
  while(1){
    printf("Enter x: ");
    gets(str);
    if(!*str) break;
    sscanf(str,"%lg",&x);
    printf("Enter y: ");
    gets(str);
    if(!*str) break;
    sscanf(str,"%lg",&y);
    z=eqn27792396(x,y);
    printf("      z=%.15lg\n",z);
    }
}


/*--------------------------------------------------------------*/
double eqn27792396(double x, double y)
/*--------------------------------------------------------------*
   TableCurve 3D
   File Source= c:\program files (x86)\tablecurve3dv4.0\109.prn
   Date= Dec 8, 2021
   Time= 12:24:08 PM
   Data Set= 109.prn, X , Y , Z 
   X= 
   Y= 
   Z= 
   Eqn#= 27792396
   Eqn= z=a+be^(x/wx)+cx/lnx+dx^(0.5)+e/y^(0.5)+f/y+g/y^(1.5)+hlny/y^2
   r2=0.951905255717241
   r2adj=0.9402459237699055
   StdErr=8.212631551312692
   Fstat=96.1339930679534
   a= 1229.571485010218
   b= -425.6036523678946
   c= 0.248400071705563
   d= -9.351219662620949
   e= -20413.22079131021
   f= 494054.5109638379
   g= -6270543.761250133
   h= 6611563.457691532
 *--------------------------------------------------------------*/
{
  double z;
  double f1,f2,f3,f4,f5,f6,f7;
  f1=exp(x/-9006.167679834849);
  f2=x/log(x);
  f3=sqrt(x);
  f4=1.0/sqrt(y);
  f5=1.0/y;
  f6=1.0/(y*sqrt(y));
  f7=log(y)/(y*y);
  z=1229.571485010218-425.6036523678946*f1
    +0.2484000717055630*f2-9.351219662620949*f3
    -20413.22079131021*f4+494054.5109638379*f5
    -6270543.761250133*f6+6611563.457691532*f7;
  return z;
}
