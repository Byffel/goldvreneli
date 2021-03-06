from _version import __version__
import argparse

def main( ):

    FUNCTION_MAP = {'available-currencies' : list_available_currencies }

    main_parser = argparse.ArgumentParser(
    prog='Goldvreneli',
    description='An automated bot for trading with crypto-currencies',
    epilog='Go and get a million Goldvrenelis!')

    main_parser.add_argument('-v', '--version', action='version', version='%(prog)s {version}'.format(version=__version__))

    subparsers = main_parser.add_subparsers(title="CoinGecko API", help="Calls to the CoinGecko API", metavar='', dest="command")
    parser_create = subparsers.add_parser("available-currencies",
                                        add_help=False,
                                        help="List all available crypto-currencies")

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
    print("list available!")

if __name__ == '__main__':
   main()