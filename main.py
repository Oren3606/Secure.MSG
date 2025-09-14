"""
Program launching and flow control
"""
from user import User
from cli import cli_args

user: User | None = None
if __name__ == "__main__":
    # todo implement launch type check (cli or calls)
    print(cli_args)
    user = User(cli_args.mode, cli_args.target, cli_args.username, cli_args.savefile)
    print(user, user.key_pub)
    user.validate()
    print(user, user._key_prv)
