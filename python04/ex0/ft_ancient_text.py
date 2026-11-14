#!/usr/bin/env python3

import sys
import typing

def main() -> None:
	if len(sys.argv) < 2:
		print(f"Usage: {sys.argv[0]} <file>")
		return
	file = sys.argv[1]
	if len(file) > 1:
		print("=== Cyber Archives Recovery ===")
		print(f"Accessing file '{file}'")
		try:
			open('file', 'r')
			print("---")
			print(file.read(), end="")
			print(f"File '{file}' closed.")
		except:
			print(f"Error opening file '{file}'"
				f"[Errno 2] No such file or directory: '{file}'"
			)

if __name__ == "__main__":
	main()