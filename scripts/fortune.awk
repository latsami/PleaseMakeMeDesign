#!/usr/bin/awk -f

# returns a random word from /usr/share/dict/words
# MYWORD=`./fortune.awk /usr/share/dict/words` && ./myscript.sh | grep $MYWORD

BEGIN {
	srand()
	choice = int(98569 * rand())
}

(NR == choice) {
		print
}
