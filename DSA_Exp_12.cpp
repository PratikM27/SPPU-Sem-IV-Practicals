#include <iostream>
#include <fstream>

using namespace std;

struct Record {
    int id;
    char name[50];
    // Add more fields as needed
};

const int RECORD_SIZE = sizeof(Record);

void insertRecord(const char* fileName, const Record& record, int position) {
    ofstream outFile(fileName, ios::binary | ios::in | ios::out);
    if (!outFile) {
        cerr << "Error: Unable to open file!" << endl;
        return;
    }

    // Move to the correct position in the file
    outFile.seekp(position * RECORD_SIZE, ios::beg);

    // Write the record
    outFile.write(reinterpret_cast<const char*>(&record), sizeof(record));

    outFile.close();
}

void deleteRecord(const char* fileName, int position) {
    // Open the file for reading and writing
    fstream file(fileName, ios::binary | ios::in | ios::out);
    if (!file) {
        cerr << "Error: Unable to open file!" << endl;
        return;
    }

    // Move to the record to be deleted
    file.seekp(position * RECORD_SIZE, ios::beg);

    // Create a dummy record to overwrite the deleted one
    Record dummy;
    file.write(reinterpret_cast<const char*>(&dummy), sizeof(dummy));

    file.close();
}

int main() {
    const char* fileName = "records.dat";

    // Insertion example
    Record newRecord = {1, "John Doe"};
    int insertPosition = 0;
    insertRecord(fileName, newRecord, insertPosition);

    // Deletion example
    int deletePosition = 0; // Delete the record at position 0
    deleteRecord(fileName, deletePosition);

    return 0;
}


