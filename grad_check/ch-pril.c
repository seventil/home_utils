/*--------------------------------------------------------------*
               TableCurve 3D C Code Output
            To modify generated output, edit C.TCL
*--------------------------------------------------------------*/

#include <math.h>
#include <stdio.h>

double eqn302(double x, double y);

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
    z=eqn302(x,y);
    printf("      z=%.15lg\n",z);
    }
}


/*--------------------------------------------------------------*/
double eqn302(double x, double y)
/*--------------------------------------------------------------*
   TableCurve 3D
   File Source= c:\program files (x86)\tablecurve3dv4.0\2.prn
   Date= Nov 27, 2021
   Time= 9:00:53 AM
   Data Set= 2.prn, X , Y , Z 
   X= 
   Y= 
   Z= 
   Eqn#= 302
   Eqn= z=a+blnx+cy+d(lnx)^2+ey^2+fylnx
   r2=0.9439440132466403
   r2adj=0.9393989332396112
   StdErr=27.43856279715298
   Fstat=252.5896165381655
   a= 1001.51477802372
   b= -103.6464965501158
   c= 5.087545624466923
   d= -0.1849006563812434
   e= -0.0001750450380706807
   f= -0.4704503715376256
 *--------------------------------------------------------------*/
{
  double z;
  x=log(x);
  z=1001.514778023720+
    x*(-103.6464965501158+x*(-0.1849006563812434))+
    y*(5.087545624466923+y*(-0.0001750450380706807))+
    x*y*(-0.4704503715376256);
  return z;
}
