#!/usr/bin/env perl

use strict;
use Net::Identica;
use Data::Dumper;

my $flag = "public timeline" unless $ARGV[0];
$flag = "query" unless not $ARGV[0];

my $nt = Net::Identica->new(
	decode_html_entities => 1,
	username => "palabras",
	password => "simple",
);

my $r;

if ($flag eq "query") {
	my $search_term = "confused";
	$r = $nt->search($search_term);
}
if ($flag eq "public timeline") {
	$r = $nt->public_timeline();
}

print Dumper $r;
