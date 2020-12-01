from _version import __version__
from pycoingecko import CoinGeckoAPI
import argparse

def main( ):

    FUNCTION_MAP = {'available-currencies' : list_available_currencies,
                    'available-vs-currencies' : list_available_vs_currencies,
                    'get-price' : get_current_price}

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

    get_price_parser = subparsers.add_parser("get-price",
                                        add_help=True,
                                        help="Get the current price of a defined crypto currency compared to another (crypto) currency")

    get_price_parser.add_argument("id", help="ID of the crypto currency")
    get_price_parser.add_argument('vs', metavar='vs', help="ID of the (crypto) currency to compare to")

    args = main_parser.parse_args()

    if args.command == None:
        main_parser.print_help()
    else:
        FUNCTION_MAP[args.command](args)

def list_available_currencies(args):
    cg = CoinGeckoAPI()    
    response = cg.get_coins_list()

    for i in response:
        print(i["name"] + " (ID: \"" + i["id"] + "\")")

def list_available_vs_currencies(args):
    cg = CoinGeckoAPI()    
    response = cg.get_supported_vs_currencies()

    for i in response:
        print(i)

def get_current_price(args):
    cg = CoinGeckoAPI()
    response = cg.get_price(args.id, args.vs)
    
    print("1 " + args.id + " = " + str(response[args.id][args.vs]) + " " + args.vs)

if __name__ == '__main__':
   main()