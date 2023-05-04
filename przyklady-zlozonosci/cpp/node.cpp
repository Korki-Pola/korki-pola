#include <iostream>
using namespace std;

#include "node.hpp"

// constructors
Node::Node() {
  index = -1;
  value = 0;
  next = nullptr;
  showIndex = true;
}

Node::Node(Node &node) {
  index = node.index;
  value = node.value;
  next = node.next;
  showIndex = true;
}

Node::Node(int providedValue) {
  index = -1;
  value = providedValue;
  next = nullptr;
  showIndex = true;
}

Node::Node(int providedValue, Node &providedNext) {
  index = -1;
  value = providedValue;
  next = &providedNext;
  showIndex = true;
}

Node::Node(int providedValue, int providedIndex) {
  index = providedIndex;
  value = providedValue;
  next = nullptr;
  showIndex = true;
}

Node::Node(int providedIndex, int providedValue, Node &providedNext) {
  index = providedIndex;
  value = providedValue;
  next = &providedNext;
  showIndex = true;
}

// destructors
Node::~Node() { delete next; }

// setters and getters
void Node::setValue(int newValue) { value = newValue; }

int Node::getValue() { return value; }

void Node::setIndex(int newIndex) { index = newIndex; }

int Node::getIndex() { return index; }

Node *Node::getNextPtr() { return next; }

void Node::resetNextPtr() { next = nullptr; }

void Node::setNextPtr(Node &newNext) { next = &newNext; }

void Node::setShowIndex(bool newShowIndex) { showIndex = newShowIndex; }

// other funcs
void Node::print() {
  if (index != -1 && showIndex) {
    cout << "[" << index << "] ";
  }

  cout << value << endl;
}