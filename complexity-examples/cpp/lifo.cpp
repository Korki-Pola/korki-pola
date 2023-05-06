#include <iostream>
using namespace std;

#include "lifo.hpp"

// constructors
Lifo::Lifo() {
  head = nullptr;
  tail = nullptr;
  index = -1;
};

Lifo::Lifo(bool showIndex) { this->showIndex = showIndex; }

// destructors
Lifo::~Lifo() {
  Node *walker = head;

  while (head != nullptr) {
    walker = head->getNextPtr();
    delete head;
    head = walker;
  }

  tail = nullptr;
};

// other funcs
// protected
void Lifo::_append(Node &node) {
  if (head == nullptr) {
    head = &node;
    tail = head;
    _fixIndexes();

    return;
  }

  tail->setNextPtr(node);
  tail = tail->getNextPtr();
  _fixIndexes();
}

void Lifo::_fixIndexes() {
  index = -1;
  Node *walker = head;

  while (walker != nullptr) {
    walker->setIndex(++index);
    walker->setShowIndex(showIndex);
    walker = walker->getNextPtr();
  }
}

// public
void Lifo::append(Node &node) {
  int nodeIndex = node.getIndex();
  if (nodeIndex == -1 || nodeIndex <= index) {
    node.setIndex(++index);
  }

  _append(node);
}

void Lifo::append(int value) {
  Node *node = new Node(value, ++index);

  _append(*node);
}

Node *Lifo::popNode() {
  if (tail == nullptr || head == nullptr) {
    throw runtime_error("No more elements to pop");
  }

  if (head == tail) {
    Node *temp = head;
    head = nullptr;
    tail = nullptr;
    temp->resetNextPtr();
    return temp;
  }

  Node *temp = tail;
  Node *walker = head;
  while (walker->getNextPtr() != temp) {
    walker = walker->getNextPtr();
  }

  tail = walker;
  tail->resetNextPtr();
  temp->resetNextPtr();
  return temp;
}

int Lifo::popValue() { return popNode()->getValue(); }