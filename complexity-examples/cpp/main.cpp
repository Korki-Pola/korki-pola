#include <iostream>

#include "lifo.cpp"
#include "node.cpp"

using namespace std;

int main() {
  Lifo* lifo = new Lifo();

  for (int i = 0; i < 10; i++) {
    lifo->append(i + 1);
  }

  for (int i = 0; i < 11; i++) {
    cout << *lifo << endl;
    try {
      lifo->popValue();
    } catch (exception& e) {
      cout << e.what() << endl;
    }
  }

  lifo->append(13);
  cout << *lifo << endl;

  return 0;
}