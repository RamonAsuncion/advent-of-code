use strict;
use warnings;

my @arr = ();
while (<STDIN>) {
  /\S/ or last; # break on empty
  chomp;
  push @arr, $_;
}

foreach my $str (@arr) {
  print "$str\n";
}
