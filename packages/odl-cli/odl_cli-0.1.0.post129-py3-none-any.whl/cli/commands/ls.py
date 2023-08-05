from commands.cmdbase import CmdBase
from commands.const import DSDL_CLI_DATASET_NAME
from commons.argument_parser import EnvDefaultVar
from rich import print as rprint
from rich.pretty import pprint
from tabulate import tabulate
from utils import admin


class Ls(CmdBase):
    """Show all the available datasets and its storage path.

    Args:
        CmdBase (_type_): _description_
    """
    def init_parser(self, subparsers):
        """_summary_

        Args:
            subparsers (_type_): _description_
        """
        
        status_parser = subparsers.add_parser('ls', help = 'Show available datasets')
        status_parser.add_argument('-s',
                                   '--skip-header', 
                                   help = 'toggle display for headers',
                                   action = 'store_true',
                                   required = False)
        status_parser.add_argument('-v',
                                   '--verbose',
                                   action = 'count',
                                   default = 0,
                                   help = 'display detailed dataset info',
                                   required = False)
        return status_parser
    
    def get_dataset_df(self):
        db_client = admin.DBClient()
        dataset_list = db_client.get_sqlite_dict_list('select * from dataset')
        datasplit_list = db_client.get_sqlite_dict_list('select * from split')
        return dataset_list, datasplit_list
    
    def datalist_trim(self, dataset_list, datasplit_list):
        dataset_list_trim = []
        datasplit_list_trim = []
        dataset_verbose_list = ['created_time','updated_time','dataset_path']
        datasplit_verbose_list = ['created_time','updated_time']
        for idx, elem in enumerate(dataset_list):
            dataset_list_trim.append({key:dataset_list[idx][key] for key in dataset_list[idx] if key not in dataset_verbose_list})
            
        for idx, elem in enumerate(datasplit_list):
            datasplit_list_trim.append({key:datasplit_list[idx][key] for key in datasplit_list[idx] if key not in datasplit_verbose_list})
        
        return dataset_list_trim, datasplit_list_trim
    
    def cmd_entry(self, cmdargs, config):
        """
        Entry point for the command.

        Args:
            self:
            args:
            config:

        Returns:

        """
        
        dataset_list, datasplit_list = self.get_dataset_df()
        dataset_list_trim, datasplit_list_trim = self.datalist_trim(dataset_list, datasplit_list)

        # default display no argument is given
        if not (cmdargs.skip_header or cmdargs.verbose):
            rprint(tabulate(dataset_list_trim, headers='keys', tablefmt='plain'))
            
        if cmdargs.verbose:
            if cmdargs.verbose >= 1:
                # verbose and skip head
                if cmdargs.skip_header:
                    rprint(tabulate(dataset_list, tablefmt='plain'))
                # verbose but not skip head
                else:
                    rprint(tabulate(dataset_list, headers = 'keys', tablefmt='plain'))
                    
        if cmdargs.skip_header:
            # not verbose but skip head
            if not cmdargs.verbose:
                rprint(tabulate(dataset_list_trim, tablefmt='plain'))