#!/usr/bin/env perl

use strict;
my $file = "caret_m" unless $ARGV[0];
$file = $ARGV[0] unless not $ARGV[0];

open(CARETM, "< :crlf :encoding(cp1252)", $file);
open(NOCARETM, "> :utf8", "no_caret_m");

while (<CARETM>) {
	print NOCARETM $_;
}

close CARETM;
close NOCARETM;
