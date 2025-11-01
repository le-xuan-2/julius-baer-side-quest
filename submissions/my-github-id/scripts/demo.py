"""Demo script showing how to use the BankingClient."""
from banking_client.client import BankingClient
from banking_client.auth import JWTAuthenticator


def main():
    auth = JWTAuthenticator()
    try:
        token = auth.get_token()
    except Exception:
        token = None

    with BankingClient() as client:
        try:
            res = client.transfer("ACC1000", "ACC1001", 10.0, auth_token=token)
            print("Transfer result:", res)
        except Exception as e:
            print("Transfer failed:", e)


if __name__ == "__main__":
    main()
