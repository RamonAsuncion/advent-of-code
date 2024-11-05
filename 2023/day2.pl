use strict;
use warnings;

use constant MAX_RED => 12;
use constant MAX_GREEN => 13;
use constant MAX_BLUE => 14;

my @arr = ();
while (<STDIN>) {
  /\S/ or last; # break on empty
  chomp;
  push @arr, $_;
}

my $t = 0;
my @v;
my $id;
foreach my $str (@arr) {
  @v = ();

  # current game
  if ($str =~ /Game (\d+)/) {
    $id = $1;
  }

  $str =~ s/Game \d+: //; # remove game

  # game sets
  @v = split /;/, $str;

  my $valid = 1;

  # follow guidline on max
  foreach my $i (@v) {
    if ($i =~ /(\d+) blue/) {
      if ($1 > MAX_BLUE) {
        $valid = 0;
        last;
      }
    }

    if ($i =~ /(\d+) red/) {
      if ($1 > MAX_RED) {
        $valid = 0;
        last;
      }
    }

    if ($i =~ /(\d+) green/) {
      if ($1 > MAX_GREEN) {
        $valid = 0;
        last;
      }
    }
  }

  if ($valid) {
    $t += $id;
  }
}

print "$t\n";
