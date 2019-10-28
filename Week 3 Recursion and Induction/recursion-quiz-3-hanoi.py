#!/usr/bin/env python3


count = 0


def move(start, final):
	print('Move block from tower {} to tower {}'.format(start, final))


def hanoi(n, start, aux, final):
	global count

	if n == 1:
		count += 1
		move(start, final)
		return

	hanoi(n-1, start, final, aux)
	hanoi(1, start, aux, final)
	hanoi(n-1, aux, start, final)


def main():
	blocks = int(input('Enter the number of blocks in the Tower of Hanoi: '))
	print()
	
	hanoi(blocks, 'A', 'B', 'C')
	print('\nIt took {} moves to solve the puzzle\n'.format(count), end='')


if __name__ == '__main__':
	main()
