#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>
using namespace std;


int main()
{
ifstream infile;
infile.open("C:\Users\KIIT\Desktop\quizsystem\\trial.txt");
if(infile.fail())
{
	cerr<<"error"<<endl;
	exit(1);
	
}
string item;
int count=0;
while(!infile.eof())
{
	infile>>item;
	count++;
}
cout<<count;
}
