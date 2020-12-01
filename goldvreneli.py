from _version import __version__
from pycoingecko import CoinGeckoAPI
import argparse

def main( ):

    FUNCTION_MAP = {'available-currencies' : list_available_currencies,
                    'available-vs-currencies' : list_available_vs_currencies }

    main_parser = argparse.ArgumentParser(
    prog='Goldvreneli',
    description='An automated bot for trading with crypto-currencies',
    epilog='Go and get a million Goldvrenelis!')

    main_parser.add_argument('-v', '--version', action='version', version='%(prog)s {version}'.format(version=__version__))

    subparsers = main_parser.add_subparsers(title="CoinGecko API", help="Calls to the CoinGecko API", metavar='', dest="command")
    subparsers.add_parser("available-currencies",
                                        add_help=False,
                                        help="List all available crypto-currencies")
    subparsers.add_parser("available-vs-currencies",
                                        add_help=False,
                                        help="List all currencies and crypto currencies that can be used for comparison")

    #parser_create.add_argument("--name", help="name of the environment")
    #parser_update = subparsers.add_parser("update",
    #                                    add_help=False,
    #                                    description="The update parser",
    #                                    help="update the orbix environment")

    args = main_parser.parse_args()

    if args.command == None:
        main_parser.print_help()
    else:
        FUNCTION_MAP[args.command]()

def list_available_currencies():
    cg = CoinGeckoAPI()    
    response = cg.get_coins_list()

    for i in response:
        print(i["name"] + " (ID: \"" + i["id"] + "\")")

def list_available_vs_currencies():
    cg = CoinGeckoAPI()    
    response = cg.get_supported_vs_currencies()

    for i in response:
        print(i)

if __name__ == '__main__':
   main()