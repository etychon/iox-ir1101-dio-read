#!/usr/bin/env python

# Made for Python 2.

import os
import sys
import time
import serial
import logging
import serial.tools.list_ports

if __name__ == "__main__":

    # Location of the directory to store log file, otherwise use /tmp
    log_file_dir = os.getenv("CAF_APP_LOG_DIR", "/tmp")
    log_file_path = os.path.join(log_file_dir, "iox-dio.log")

    # set up logging to file 
    logging.basicConfig( 
        filename=log_file_path,
        level=logging.INFO, 
        format='[%(asctime)s]{%(pathname)s:%(lineno)d}%(levelname)s- %(message)s', 
        datefmt='%H:%M:%S'
    ) 

    # set up logging to console 
    console = logging.StreamHandler() 
    console.setLevel(logging.DEBUG) 

    # set a format which is simpler for console use 
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter) 

    # add the handler to the root logger 
    logging.getLogger('').addHandler(console) 
    logger = logging.getLogger(__name__)

    logger.info('Starting application...')

    ports = serial.tools.list_ports.comports()
    logger.info('Checking dio ports available:\n')
    
    dio_port_list = [1,2,3,4]

    # Triage all the dio ports that are working

    while (True):
        output = "";
        for dio_port in dio_port_list:
            logger.info("+ GPIO port " + str(dio_port))
            try:
                with open("/dev/dio-"+str(dio_port), "r+b", 0) as c:
                    c_read = c.read()
                    output = output+c_read
                    logger.info("  value ->" + c_read)
            except:
                output = output+'-'
                logger.info(str(dio_port) + "  -> N/A")
                pass

        logger.info("GPIO port " + "".join(str(x) for x in dio_port_list) + " = " + output)

        time.sleep(2)
                    
    logger.info("All done. Goodbye!\n")
