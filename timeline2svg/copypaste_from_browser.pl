#!/usr/bin/env perl

use strict;
use SVG;

my $svg1 = SVG->new(width=>200,height=>200);

my $y = $svg1->group(
	id => "group_y",
	style => { stroke=>"red", fill=>"green" }
);

$y->circle(cx=>100, cy=>100, r=>50, id=>"circle_in_group_y");

my $z = $svg1->tag("g",
	id => "group_z",
	style => {
		stroke => "rgb(100,200,50)",
		fill => "rgb(10,100,150)"
	}
);

#$tag = $svg1->tag($name, %attributes). Generic element generator. Creates the
#element named $name with the attributes specified in %attributes. This method
#is the basis of most of the explicit element generators.
$z->tag('circle', cx=>50, cy=>50, r=>100, id=>'circle_in_group_z');

my $k = $z->anchor(
	id => "anchor_k",
	-href => "http://www.com",
	target => "new_window_0",
)->rectangle(
		x => 20, y => 50,
		width => 20, height => 30,
		rx => 10, ry => 5,
		id => "rect_k_in_anchor_k_in_group_z",
	);

#print $svg1->xmlify;

my $svg = SVG->new(width=>200,height=>200);
my %hash;
$hash{width} = 200;
$hash{height} = 200;
$svg= SVG->new(%hash);
my %group_style = (
	'opacity'=>1,fill=>'red',
	'stroke'=>'green','fill-opacity'=>0.4,
	'stroke-opacity'=>'1');
$svg->comment('Draw a group with two circles that have url links');
$svg->comment('Define a child of $svg called $gp1');
my $gp1 = $svg->group(id=>'group_1',style=>\%group_style);
my $a1 = $gp1->anchor(-href=>'www.w3c.org');
$a1->circle(id=>'this_circle',cx=>170,cy=>100,r=>20);
$a1->circle(id=>'that_circle',cx=>100,cy=>170,r=>20);
# define a third circle with a separate style (stroke colour), overriding the
# group stroke colour definition.
$a1->circle(id=>'the_other_circle',cx=>180,cy=>160,r=>20,
	style=>{stroke=>'cyan'});

# add a second group, and give that group two text elements with cdata entries
$svg->comment('Draw a second group with two text entries One entry has an anchor');
my $gp2 = $svg->group(id=>'group_2');
$svg->comment('Here is one way to define text');
my $t1 = $gp2->text(x=>80,y=>20);
$t1->cdata('Tutorial');
$svg->comment('Here is another way to define text');
$gp2->text(x=>120,y=>20)->cdata('Two');
$gp2->anchor(-href=>'/SVG.html')
      ->text(x=>20,y=>40,fill=>'rgb(200,30,100)')
      ->cdata('Brought to you by the letters SVG and pm');
$svg->comment("Well, we're done here");



print $svg->xmlify;
