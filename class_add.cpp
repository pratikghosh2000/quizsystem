#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

class question
{
	float marks;
	char qs[100];
	public:
		question(){ }
		void getqs();
		void dispqs(int);
};

void question::getqs()
{
cout<<"enter the question"<<endl;
cin.getline(qs,100);
cout<<"enter marks"<<endl;
cin>>marks;
}

void question::dispqs(int n)
{
cout<<"question number"<<n;
cout<<qs<<". ";
cout<<"marks="<<marks<<endl;
}

int main()
{
	int a;
	cout<<"enter number of questions to be added";
	cin>>a;
	question q[a];
	fstream file;
	int i;
	file.open("qsn.txt",ios::out);
	cout<<"enter the questions"<<endl;
	cout<<"press any number to cintinue"<<endl;
	cout<<"enter -1 to exit in between"<<endl;
	int c=1;
	cin>>c;
	if(c==-1)
	{
		file.close();
		exit(1);
	}
	else
	{
		for(i=0;i<a;i++)
		{
			q[i].getqs();
			file.write((char*)&q[i],sizeof(q[i]));
			
		}
		file.close();
		
	}
	int j=i+1;
	file.open("qsn.txt",ios::in);
	cout<<"questions added"<<endl;
	for(i=0;i<j-1;i++)
	{
		file.read((char*)&q[i],sizeof(q[i]));
		q[i].dispqs(i+1);
		
	}
	file.close();
	return 0;
	
	
}
