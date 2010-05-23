#!/usr/bin/perl

# MakeCharList.pl

our $Version = "3.0";	# 2005-10-15 bh
#	Added -f and -r options
# Version 2: 21 Sep 05 jw v2 modified layout of output file
# Version 1: 16 Aug 05  bb

use Getopt::Std;
use open ':encoding(utf8)';
binmode(STDOUT, ":utf8");

our ($opt_f, $opt_r);
getopts('fr');

die <<"eof" unless $#ARGV >= 0;
Usage:
    MakeCharList.pl [-f] [-r]  infile > outfile

Given a legacy text file, count the number of times each character occurs.
Print out the count, also giving the decimal equivalent of each character.
The characters themselves are printed twice, so that in Word, one column 
can be left in Courier, and the other can be converted to a legacy font,
for easy review.

-f sort by frequency

-r reverse sort order

Version $Version
eof

my %count;
while (my $line = <>) {
	chomp $line;
	my @line_chars = split(//, $line);
	for ($i=0; $i<=$#line_chars; $i++) {
		next if ($line_chars[$i] =~ /\s/);
		$count{$line_chars[$i]}++;
	}
}

my @characters = keys %count;
my @characters_hex;
foreach (@characters) { push @characters_hex, ord($_) };
@characters_hex = sort { $a <=> $b } @characters_hex;

print "Hex\tChar\tCount\n";
foreach (@characters_hex) {
	if (chr($_)) {
		printf "x%04X\t%s\t%5g\n", $_, chr($_), $count{chr($_)};
	}
}
