/*--------------------------------------------------------------*
               TableCurve 3D C Code Output
            To modify generated output, edit C.TCL
*--------------------------------------------------------------*/

#include <math.h>
#include <stdio.h>

double eqn6276(double x, double y);

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
    z=eqn6276(x,y);
    printf("      z=%.15lg\n",z);
    }
}


/*--------------------------------------------------------------*/
double eqn6276(double x, double y)
/*--------------------------------------------------------------*
   TableCurve 3D
   File Source= c:\program files (x86)\tablecurve3dv4.0\109.prn
   Date= Dec 8, 2021
   Time= 12:32:31 PM
   Data Set= 109.prn, X , Y , Z 
   X= 
   Y= 
   Z= 
   Eqn#= 6276
   Eqn= z=a+bx^2+cx^3+de^(x/wx)
   r2=0.9347733868190943
   r2adj=0.9173796233041861
   StdErr=10.00471855636471
   Fstat=76.432882529222
   a= -13.28930495227476
   b= 0.001114714856481364
   c= -8.397940946547142E-06
   d= 14.23762656838414
 *--------------------------------------------------------------*/
{
  double z;
  double f1,f2,f3;
  f1=x*x;
  f2=x*x*x;
  f3=exp(x/111.0542057672787);
  z=-13.28930495227476+0.001114714856481364*f1
    -8.397940946547142E-06*f2+14.23762656838414*f3;
  return z;
}
