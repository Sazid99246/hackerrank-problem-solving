#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Student
{
private:
    int age;
    string first_name;
    string last_name;
    int standard;

public:
    void set_age(int a)
    {
        age = a;
    }
    void set_first_name(string firstName)
    {
        first_name = firstName;
    }
    void set_last_name(string lastName)
    {
        last_name = lastName;
    }
    void set_standard(int studentStandard)
    {
        standard = studentStandard;
    }

    int get_age()
    {
        return age;
    }
    string get_first_name()
    {
        return first_name;
    }
    string get_last_name()
    {
        return last_name;
    }
    int get_standard()
    {
        return standard;
    }
};

int main()
{
    Student student;
    int age;
    cin >> age;
    student.set_age(age);

    string first_name;
    cin >> first_name;
    student.set_first_name(first_name);

    string last_name;
    cin >> last_name;
    student.set_last_name(last_name);

    int standard;
    cin >> standard;
    student.set_standard(standard);

    cout << student.get_age() << endl
         << student.get_last_name() + ", " + student.get_first_name() << endl
         << student.get_standard() << endl
         << endl
         << student.get_age() << "," << student.get_first_name() << "," << student.get_last_name() << "," << student.get_standard() << endl;

    return 0;
}
