#include <iostream>
using namespace std;

#ifndef NODE_HPP
#define NODE_HPP

class Node {
 private:
  int index;
  int value;
  Node *next;
  bool showIndex;

 public:
  Node();
  Node(Node &node);
  Node(int value);
  Node(int value, Node &next);
  Node(int value, int index);
  Node(int index, int value, Node &next);
  ~Node();

  void setValue(int value);
  int getValue();

  void setIndex(int index);
  int getIndex();

  void resetNextPtr();
  void setNextPtr(Node &newNext);
  Node *getNextPtr();

  void setShowIndex(bool newShowIndex);

  void print();
  friend ostream &operator<<(ostream &os, const Node &node);
};

ostream &operator<<(ostream &os, const Node &node) {
  if (node.index != -1 && node.showIndex) {
    os << "[" << node.index << "] ";
  }

  os << node.value;

  return os;
}

#endif  // NODE_HPP