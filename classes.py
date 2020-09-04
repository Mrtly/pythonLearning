#!/usr/bin/env python3

class Duck:
    sound = "Quackie quackie"
    move = "Walks like a duck"

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.move)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
