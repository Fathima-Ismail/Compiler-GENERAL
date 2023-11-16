//PROGRAM 2
//Count number of vowels and consonants

//header files
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

//main function
int main()
{
    //variable initialization and declaration
    string inputstring;
    int vowels = 0, consonants = 0, digits = 0, spaces = 0;



    // Create and open a text file
    ofstream MyFile("textfile.txt");

    // Check if the file was opened successfully
    if (!MyFile) {
        cerr << "Error opening the file." << endl;
        return 1;
    }

    // Get input string from the user
    cout << "Enter a string: ";
    getline(cin, inputstring);

    // Write the input string to the file
    MyFile << inputstring;

    // Close the file
    MyFile.close();
    
    //To notify user of successful saving of file content
    cout << endl << "String successfully saved to textfile.txt" << endl << endl;
    


    // Open the file for reading
    ifstream inputFile("textfile.txt"); 

    //Checking whether file successfully got opened or not
    if (!inputFile) {
        cerr << "Error opening the file." << endl;
        return 1;
    }

    string content;
    string line;

    // Read the file line by line and store the content in content
    while (getline(inputFile, line)) {
    content += line + "\n";
    }
    // Close the file
    inputFile.close(); 

    // Now the file content is stored in the variable content
    
    //Using a for loop to iterate through string 'content'
    //The null character (\0) is used to mark the end of a character array, or a string
    for(int i = 0; content[i]!='\0'; i++)
    {
        
        //To check for vowels in content
        if(content[i]=='a' || content[i]=='e' || content[i]=='i' || content[i]=='o' || content[i]=='u' || content[i]=='A' ||
           content[i]=='E' || content[i]=='I' || content[i]=='O' || content[i]=='U')
        {
            vowels++;
        }
        
        //To check for consonants in content
        else if((content[i]>='a'&& content[i]<='z') || (content[i]>='A'&& content[i]<='Z'))
        {
            consonants++;
        }
        
        //To check for digits in content
        else if(content[i]>='0' && content[i]<='9')
        {
            digits++;
        }
        
        //To check for whitespaces in content
        else if (content[i]==' ')
        {
            spaces++;
        }
    }

    //showing results to user
    cout << "\nVowels: " << vowels << endl;
    cout << "Consonants: " << consonants << endl;
    cout << "Digits: " << digits << endl;
    cout << "White spaces: " << spaces << endl << endl;

    return 0;
}
//end of program
