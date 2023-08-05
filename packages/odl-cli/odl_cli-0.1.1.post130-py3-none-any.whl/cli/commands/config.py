import json
import os
import sys

from commons.exceptions import CLIException, ExistCode
from commons.stdio import print_stdout
from loguru import logger
from rich import print as rprint
from rich.console import Console
from rich.pretty import pprint
from rich.syntax import Syntax
from tabulate import tabulate

from .cmdbase import CmdBase
from .const import (DEFAULT_CLI_CONFIG_FILE, DEFAULT_CONFIG_DIR,
                    DEFAULT_LOCAL_STORAGE_PATH, PROG_NAME, SQLITE_DB_PATH)


class Config(CmdBase):
    """Set dsdl configuration {file path, user login info}.

    Args:
        CmdBase (_type_): _description_
    """
    def init_parser(self, subparsers):
        """_summary_

        _extended_summary_

        Args:
            subparsers (_type_): _description_
        """

        # config_parser = subparsers.add_parser('config', help='set dsdl configuration.', example='config.example')
        config_parser = subparsers.add_parser('config', help='set dsdl configuration.')
        config_parser.add_argument('-k',
                                   '--keys',
                                   action = 'store_true',
                                   help = 'show all the available keys',
                                   required = False)
        config_parser.add_argument('-l',
                                   '--list',
                                   action = 'count',
                                   help = 'show all key value pairs',
                                   required = False)

        
        sub_config_parser = config_parser.add_subparsers(dest = 'command')
        repo_parser = sub_config_parser.add_parser('repo', help = 'set dsdl repo configuration')
        repo_parser.add_argument('--repo-name',
                                 help = 'set repo name',
                                 required = True)
        repo_parser.add_argument('--repo-username', 
                                 help = 'set repo user name')
        repo_parser.add_argument('--repo-userpswd', 
                                 help = 'set repo user password')
        repo_parser.add_argument('--repo-service', 
                                 help = 'set repo service url')
        repo_parser.add_argument('--repo-remove',
                                 action = 'store_true',
                                 help = 'remove specific configuration',
                                 required = False)
        
        storage_parser = sub_config_parser.add_parser('storage', help = 'set dsdl storage configuration')
        storage_parser.add_argument('--storage-name', 
                                    help = 'set storage name', 
                                    required = True)
        storage_parser.add_argument('--storage-path',
                                    help = 'set storage path',
                                    required = True)
        storage_parser.add_argument('--storage-credentials',
                                    action = 'append',
                                    nargs = 2,
                                    help = 'set credentials',
                                    required = False)
        storage_parser.add_argument('--storage-endpoint',
                                    help = 'set storage endpoint',
                                    default = '',
                                    required = False)
        storage_parser.add_argument('--storage-remove',
                                    action = 'store_true',
                                    help = 'remove specific storage configuration',
                                    required = False)
        return config_parser

    @logger.catch
    def cmd_entry(self, args, config):
        """
        Entry point for the command.

        Args:
            self:
            args:
            config:

        Returns:

        """
        # if not args.repo_name:
        #             logger.exception('Please name a repo using {} before you can set is info'.format('--repo-name'))
        if args.command:
            # repo command handler
            if args.command == 'repo':
                if args.repo_remove:
                    try:
                        self.__repo_delete(config, args)
                        self.__config_writter(config)
                        print_stdout('REPO config for {} was removed !'.format(args.repo_name))
                        logger.info('REPO config for {} was removed !'.format(args.repo_name))
                    except KeyError as err:
                        print_stdout('No repo named {}!'.format(args.repo_name))
                        logger.exception('No repo named {}'.format(args.repo_name))
                elif (not args.repo_remove) & (args.repo_name not in config['repo'].keys()):
                    # new repo
                    self.__repo_new(config, args)
                    print_stdout('Your repo config for {} success !'.format(args.repo_name))
                    logger.info('REPO: {} config success !'.format(args.repo_name))
                    self.__config_writter(config)
                else:
                    print_stdout('REPO config for {} already exists, please remove and re-configure it !'.format(args.repo_name))
                    logger.error('REPO config for {} already exists, please remove and re-configure it !'.format(args.repo_name))
                    
            elif args.command == 'storage':
                if args.storage_remove:
                    try:
                        self.__storage_delete(config, args)
                        self.__config_writter(config)
                        print_stdout('STORAGE config for {} was removed !'.format(args.storage_name))
                        logger.info('STORAGE config for {} was removed !'.format(args.storage_name))
                    except KeyError as err:
                        print_stdout('No storage named {} !'.format(args.storage_name))                      
                        logger.exception('No storage named {} !'.format(args.storage_name))
                    
                # new storage entry
                elif (not args.storage_remove) & (args.storage_name not in config['storage'].keys()):
                    self.__storage_new(config, args)
                    self.__config_writter(config)
                # old storage update
                else:
                    print_stdout('STORAGE config for {} already exists, please remove and re-configure it !'.format(args.storage_name))
                    logger.error('STORAGE config for {} already exists, please remove and re-configure it !'.format(args.storage_name))

        
                    
        if args.keys:
            snippet_keys = """
            The available keys are:
                repo-name               # set repo name
                repo-username           # set repo username
                repo-userpswd           # set repo password
                repo-service            # set repo service url
            
                storage-name            # storage name
                storage-path            # storage path
                storage-credentials     # storage credentials (password, ssh-key, access-key, secret-key)
                storage-endpoint        # storage endpoint
            """
            rprint(snippet_keys)
        
        if args.list:
            if args.list == 1:
                pprint(config)
            else:
                pprint(config, expand_all = True)
        
    def __config_writter(self, config):    
        with open(DEFAULT_CLI_CONFIG_FILE, 'w') as file:
            return json.dump(config,file, indent=4)

    def __repo_new(self, config, args):
        config['repo'][args.repo_name] = {}
        if args.repo_username:
            config['repo'][args.repo_name]['user'] = args.repo_username
        if args.repo_userpswd:
            config['repo'][args.repo_name]['passwd'] = args.repo_userpswd
        if args.repo_service:
            config['repo'][args.repo_name]['service'] = args.repo_service

    def __repo_delete(self, config, args):
        del config['repo'][args.repo_name]
    
    def __storage_new(self, config, args):
        config['storage'][args.storage_name] = {}
        
        if args.storage_path[:2] not in ['s3','sf']:
            config['storage'][args.storage_name]['path'] = args.storage_path
            print_stdout('Remote storage only support s3 and sftp, Your local storage was switched to {} !'.format(args.storage_path))
            logger.info('Remote storage only support s3 and sftp, Your local storage was switched to {} !'.format(args.storage_path))
            
        elif args.storage_path[:2] == 's3':
            config['storage'][args.storage_name]['ak'] = args.storage_credentials[0][0]
            config['storage'][args.storage_name]['sk'] = args.storage_credentials[0][1]
            config['storage'][args.storage_name]['path'] = args.storage_path
            config['storage'][args.storage_name]['endpoint'] = args.storage_endpoint
            print_stdout('Yours3 config for {} success !'.format(args.storage_name))
            logger.info('STORAGE S3: {} config success !'.format(args.storage_name))
            
        elif args.storage_path[:4] == 'sftp':
            config['storage'][args.storage_name]['user'] = args.storage_credentials[0][0]
            config['storage'][args.storage_name]['password'] = args.storage_credentials[0][1]
            config['storage'][args.storage_name]['path'] = args.storage_path
            print_stdout('Your sftp config for {} success !'.format(args.storage_name))
            logger.info('STORAGE STFP: {} config success !'.format(args.storage_name))
    
    def __storage_delete(self, config, args):
        del config['storage'][args.storage_name]
