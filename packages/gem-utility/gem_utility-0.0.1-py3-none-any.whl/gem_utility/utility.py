import os
import sys
import base64
import logging
import datetime
import traceback
from Crypto.Cipher import DES
from configparser import RawConfigParser


class UtilityMethods:
    # Method 1 - Global Initialization in the class
    def __init__(self):
        # Base directory path for Whole project
        self.base_dir_path = os.getcwd()
        self.log_dir_name = "logs"
        self.job_name = "default"
        self.log_handler = None
        self.log_file_path = None

    # Function for Getting warnings
    def get_warnings(self, message, filename):
        # Method to get warning messages.
        self.log_handler.warning("\t" + str(message) + " in this '" + str(filename) + "'.\n")

    def fn_create_log_dir(self, log_dir_name=None, job_name=None):
        try:
            if log_dir_name is not None:
                self.log_dir_name = log_dir_name

            if job_name is not None:
                self.job_name = job_name

            # Assign log dir path with log dir name
            log_dir_path = self.base_dir_path + "/" + str(self.log_dir_name)

            # Check for log directory path if not exists create new one
            if not os.path.exists(log_dir_path):
                os.makedirs(log_dir_path)

            log_file_path = str(log_dir_path) + "/" + str(self.job_name) + ".log"
            self.log_file_path = log_file_path

            # Check the log file present
            if os.path.isfile(log_file_path):
                rename_current_time = datetime.datetime.now().strftime('%m-%d-%Y_%H-%M-%S')
                rename_logfile_name = str(self.job_name) + "_" + str(rename_current_time) + ".log"
                rename_log_file_path = str(log_dir_path) + "/" + rename_logfile_name
                # Rename the old file with new file name
                os.rename(log_file_path, rename_log_file_path)
            return log_file_path
        except Exception as error:
            traceback.print_exc()
            print("ERROR : (format_config_parameters method) : " + str(error) + " \n")
            self.log_handler.error("\t\t\t ERROR : (format_config_parameters method) : " + str(error) + " \n")

    # Function for creating log functions
    def fn_create_logger(self, log_file_path):
        """ A method to create a log file. """
        try:
            log_level = "INFO"
            log_format = "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s"
            log_dateformat = "%Y-%m-%d %H:%M:%S"
            log_levels = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARNING, 'error': logging.ERROR, 'critical': logging.CRITICAL}
            level_set = log_levels[log_level.lower()]
            logger = logging.getLogger(self.job_name)
            logger.setLevel(level_set)

            # Creating the logging file handler
            fh = logging.FileHandler(str(log_file_path))
            formatter = logging.Formatter(log_format, datefmt=log_dateformat)
            fh.setFormatter(formatter)

            # Add Handler to logger object
            logger.addHandler(fh)
            return logger
        except Exception as e:
            traceback.print_exc()
            print("\tERROR : ( Log File Creation) : " + str(e) + " \n")
            sys.exit(1)

    def fn_get_config_parser(self, config_file):
        """ A method to create a log file. """
        try:
            # instantiate
            config_read_parser = RawConfigParser()
            # parse existing config file
            config_read_parser.read(config_file)
            return config_read_parser
        except Exception as e:
            self.log_handler.error("\t\t\t( fn_get_config_parser method ) : " + str(e) + " \n")
            print("\t\t\t ERROR : ( fn_get_config_parser method ) : " + str(e) + " \n")

    # Function for getting the configuration files
    def fn_read_get_config_file_value(self, config_file, config_segment, config_key):
        """ A method to read and get the values from the config file """
        try:
            ''' Read the  config_key parameter and config_segment from config_file. '''
            config_parser = RawConfigParser()
            config_parser.read(config_file)
            config_value = config_parser.get(config_segment, config_key)
            return config_value
        except Exception as e:
            self.log_handler.error("\t\t\t( fn_get_config_file_value method ) : " + str(e) + " \n")
            print("\t\t\t ERROR : ( fn_get_config_file_value method ) : " + str(e) + " \n")

    # Function for Decrypting the encrypted values in config files
    def fn_des_decrypted_process(self, pp_secret_key, inside_encrypted_string):
        try:
            padding = b'{'
            DecodeDES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(padding)
            iv = b"yLitpA@a"
            cipher = DES.new(key=str(pp_secret_key).encode(), mode=DES.MODE_CBC, IV=iv)
            decoded_encrypted_string = DecodeDES(cipher, inside_encrypted_string)
            return decoded_encrypted_string.decode()
        except Exception as e:
            print("\t\t\t ERROR : (fn_DES_decrypted_process method) : ", str(e), " \n")
            self.log_handler.error("\t\t\t ERROR : (fn_DES_decrypted_process method) : ", str(e), " \n")
