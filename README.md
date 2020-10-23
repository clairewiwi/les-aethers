# les-aethers
installation les aethers 2019-2020

 UTILISATION ------------------------------------------------------------------------------------------------------------------------

Demarage du path : 
$ cd /home/eusapia/Documents/
$ python3  Ether.py


Accordage Cordes : 
    • aller dans l’onglet «Cordes » 
    • decocher « [ ] Radio on Cordes »
    • pour chaque corde et chaque harmonique cocher  case « amplitude x » et ajuster la fréquence pour avoir le maximum d’amplitude visuellement sur les cordes.
 
les fréquences sont enregistrées dans /home/eusapia/Documents/Gnu Radio/Harmonic_frequencies
faire des sauvegardes régulières de ce fichier


Bookmarks des fréquences Radios
Création : 
Dans GQRX
Export : 
	home/.config/gqrx/bookmarks.csv



INSTALLATION ------------------------------------------------------------------------------------------------------------------------

Installation Ubuntu 
sudo apt-get update

Installation Carte Son
elle est directement reconnue, pas besoin d’installation 

Installation Geany pour avoir editeur python
sudo apt install geany

Instalation Gnu Radio companion : 
	Avec GQRX
gnuradio-companion est déjà installé avec GQRX avec en plus ce qu’il faut pour le recepteur radio 
https://gqrx.dk/download/install-ubuntu

sudo add-apt-repository -y ppa:bladerf/bladerf
sudo add-apt-repository -y ppa:myriadrf/drivers
sudo add-apt-repository -y ppa:myriadrf/gnuradio
sudo add-apt-repository -y ppa:gqrx/gqrx-sdr
sudo apt-get update
sudo apt-get install gqrx-sdr

par contre il faut corriger un bug de gnuradio lorsque l’on veut utiliser des variable sauvegardées

créer un fichier  /usr/lib/python3/dist-packages/ConfigParser.py avec dedans :
from configparser import *
