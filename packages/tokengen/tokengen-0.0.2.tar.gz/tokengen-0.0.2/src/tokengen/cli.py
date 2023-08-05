
from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(description="""
    Automate Tokens Generation
    """)
    parser.add_argument(
        "--vault", '-v',
        help='Azure keyvault name',
        nargs=1,
    )
    parser.add_argument(
        "--vault_url", '-vu',
        help='Keyvault URL',
        nargs=1,
    )
    parser.add_argument(
        "--secret", '-s',
        help='Secret name in the keyvault',
        nargs=1,
    )
    parser.add_argument(
        "--retailer", '-r',
        help='Retailer Name',
        nargs=1,
        default='morrisons-favourites',
        required=True
    )
    parser.add_argument(
        "--username", '-',
        help='Username of GitLab Registry',
        nargs=1,
        required=True
    )
    parser.add_argument(
        "--email", '-e',
        help='Email of GitLab Registry',
        nargs=1,
        required=True
    )
    parser.add_argument(
        "--password", '-p',
        help='Password of GitLab Registry',
        nargs=1,
        required=True
    )
   
    return parser


def main():
    from tokengen import source
    import logging
    import os
    import sys


    """Configure logger to stream to stdout"""
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger("tokengen")

    from tokengen import source


    args = create_parser().parse_args()

    
    """Generate the tokens and push to Azure keyvault"""
    source.generate_secret_value_and_push_to_azkeyvault(''.join(args.secret), ''.join(args.vault_url))

    """Use Pepper token and retailer to generate token"""
    source.generate_oasis_api_token(
        username=''.join(args.username),
        email=''.join(args.email),
        password=''.join(args.password), 
        retailer=''.join(args.retailer))

    print("AIFI_API_TOKEN: ", os.getenv("AIFI_API_TOKEN"))
    print("PEPPER: ", os.getenv("PEPPER"))

    print('All Processes completed!')


if __name__ == "__main__":
    import time

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()

    timeout = end_time - start_time
    print(f'It took {timeout :0.2f} second(s) to complete.')


