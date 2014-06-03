Quick Start
=======
 
* Download ```saiku-server-2.5.tar.gz``` and copy to ```~/rpmbuild/SOURCES```
* Copy ```saiku-server``` init script to ```~/rpmbuild/SOURCES```
* Build RPM ```$ rpmbuild -ba saiku-server.spec```
* Install RPM ```$ yum install ~/rpmbuild/RPMS/noarch/saiku-server-2.5-1.el6.noarch.rpm```
* Start Service ```$ /etc/init.d saiku-server start```
* Enable on Reboot ```$ chkconfig saiku-server on```
