"""Quick sanity check to make sure .env is loaded before opening notebooks."""

import os

from dotenv import load_dotenv


def main() -> None:
    """Load environment variables and report whether required keys exist."""
    load_dotenv()  # Reads .env into the current process
    has_key = bool(os.getenv("TINKER_API_KEY"))
    print("TINKER_API_KEY present:", has_key)


if __name__ == "__main__":
    main()
