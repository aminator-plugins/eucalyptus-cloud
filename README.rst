Eucalyptus Cloud Plugin for NetflixOSS Aminator
===========================================

This Aminator plugin allows you to provision an EMI in a 
`Eucalyptus <http://www.eucalyptus.com>`__ cloud. 

Examples
--------

Sample environment
:: 
    
    euca_apt_linux:
        cloud: euca
        distro: debian
        provisioner: apt
        volume: virtio
        blockdevice: virtio
        finalizer: tagging_ebs_euca

::

    $ sudo aminate -e euca_apt_linux --ec2-endpoint <clc-ip> -B emi-CD544111 apache2

Documentation
-------------

Its on the wiki:
https://github.com/aminator-plugins/eucalyptus-cloud/wiki
