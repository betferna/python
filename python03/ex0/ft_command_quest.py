#!/usr/bin/env python3

import sys

def main():
    print("=== Command Quest ===")

    # Program name first argument
    print(f"Program name: {sys.argv[0]}")

    # Arguments received (excluding the program name itself)
    args = sys.argv[1:]

    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv)-1}")
        for i in range(1, len(sys.argv)):
              print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {len(sys.argv)}")

if __name__ == "__main__":
    main()
    
