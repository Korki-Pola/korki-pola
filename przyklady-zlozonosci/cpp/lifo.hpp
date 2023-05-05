#include "node.hpp"

#ifndef LIFO_HPP
#define LIFO_HPP

class Lifo {
 private:
  Node *head;
  Node *tail;
  int index;
  bool showIndex;

 protected:
  // helper funcs
  void _append(Node &node);
  void _fixIndexes();

 public:
  // constructors & destructors
  Lifo();
  Lifo(bool showIndex);
  ~Lifo();

  // other funcs
  void append(Node &node);
  void append(int value);
  Node *popNode();
  int popValue();

  // overloads
  friend ostream &operator<<(ostream &os, const Lifo &lifo);
};

ostream &operator<<(ostream &os, const Lifo &lifo) {
  Node *walker = lifo.head;

  os << "[";
  while (walker != nullptr) {
    os << *walker;
    if (walker->getNextPtr() != nullptr) {
      os << ", ";
    }
    walker = walker->getNextPtr();
  }
  os << "]";

  return os;
}

#endif  // LIFO_HPP