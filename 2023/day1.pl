use strict;
use warnings;

# hash w/ vals to do sum
my %words = (
  one   => 1,
  two   => 2,
  three => 3,
  four  => 4,
  five  => 5,
  six   => 6,
  seven => 7,
  eight => 8,
  nine  => 9,
);

my @arr = ();
while (<STDIN>) {
  /\S/ or last; # break on empty
  push @arr, $_;
}

# two1nine
# two | 1 | nine (all matching)
# 2 1 9 -> 29

my $t = 0;
my @v;
foreach my $str (@arr) {
  @v = (); # reset

  # fixme: this is not working as intended.
  # digit and word should know each other existance.

  if ($str =~ /(\d)/) { # first
    push @v, $1;
  }

  # my @m = $str =~ /(\d+)/g;
  foreach my $word (keys %words ) {
    if ($str =~ /$word/) {
      push @v, $words{$word};
    }
  }

  if ($str =~ /(\d)$/) { # last
    push @v, $1;
  }

  # only one can go first.
  if (@v) {
    my $r = $v[0] . $v[-1];
    $t += int($r);
  }

  #if (@m) {
  #  my $r = $m[0] . $m[-1];
  #  $t += int($r);
  #}
}

print "$t\n";

