
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
    from tokengen.source import (
        generate_secret_value_and_push_to_azkeyvault,
        generate_oasis_api_token
    )
    import logging
    import os
    import sys


    """Configure logger to stream to stdout"""
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger("tokengen")

    args = create_parser().parse_args()

    
    """Generate the tokens and push to Azure keyvault"""
    generate_secret_value_and_push_to_azkeyvault(''.join(args.secret), ''.join(args.vault_url))

    """Use Pepper token and retailer to generate token"""
    def inject_registry_credentials():
        if os.getenv("username") and os.getenv("email") and os.getenv("password") and os.getenv("retailer"):
            logger.info("Using GitLab Credentials from Environment Variables")
            generate_oasis_api_token(
                username=''.join(os.getenv("username")),
                email=''.join(os.getenv("email")),
                password=''.join(os.getenv("password")), 
                retailer=''.join(os.getenv("retailer"))
            )
        else:
            logger.info("Using GitLab Credentials from CLI input values"),
            generate_oasis_api_token(
                username=''.join(args.username),
                email=''.join(args.email),
                password=''.join(args.password), 
                retailer=''.join(args.retailer))

    # Inject GitLab Credentials from Environmental variables else, use input from CLI 
    inject_registry_credentials()

    print("AIFI_API_TOKEN: ", os.getenv("AIFI_API_TOKEN"))
    print("PEPPER: ", os.getenv("PEPPER"))

    print('All Processes completed!')



