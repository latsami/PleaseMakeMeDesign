#!/usr/bin/awk -f

# returns a random word from /usr/share/dict/words

BEGIN {
	srand()
	choice = int(98569 * rand())
}

(NR == choice) {
		print
}
