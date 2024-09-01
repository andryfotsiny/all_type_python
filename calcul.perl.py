#!/usr/bin/perl
use strict;
use warnings;

# Saisie des deux nombres
print "Entrez le premier nombre : ";
my $nombre1 = <STDIN>;
chomp($nombre1);

print "Entrez le deuxième nombre : ";
my $nombre2 = <STDIN>;
chomp($nombre2);

# Calcul de la somme
my $somme = $nombre1 + $nombre2;

# Vérification de la somme
if ($somme > 10) {
    print "oui\n";
} else {
    print "non\n";
}