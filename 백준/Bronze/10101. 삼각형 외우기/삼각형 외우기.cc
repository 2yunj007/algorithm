#include <iostream>
using namespace std;

int main()
{
    int A,B,C;
    
    cin >>A>>B>>C;
    
    if((A+B+C)!=180)
        cout <<"Error";
    else if(A==B && B==C)
        cout <<"Equilateral";
    else if(A==B || A==C || B==C)
        cout  <<"Isosceles";
    else
        cout <<"Scalene";
    
    return 0;
}