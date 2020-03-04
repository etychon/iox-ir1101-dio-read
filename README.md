# Read digital IO (Alarm) status on Cisco IR1101 using Cisco IOx with Python

## Prerequisites

* Cisco IR1101 with the SPMI expansion module. This module has 4 general-purpose input/output (GPIO) ports.
* Development machine with Docker, ioxclient, and internet access.

## How this works?

Cisco IR1101 GPIO ports are usable in Cisco IOS-XE for example using the Embedded Event Manager (EEM), however to be usable with Cisco IOx the ports will need to tbe exposed to IOx CAF framework using this configuration command in Cisco IOS-XE:

    SPARROW-UUT1# config terminal
    SPARROW-UUT1(config)# alarm contact attach-to-iox
    SPARROW-UUT1(config)# end
