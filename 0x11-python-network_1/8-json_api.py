#!/usr/bin/python3

"""
Script that takes in a letter (optional) and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter 'q'.

Displays user information ([id] <name>) for valid JSON responses
with 'id' and 'name' keys, or appropriate messages for errors.

- No argument: Searches with an empty query string.
- Invalid JSON: Indicates missing 'id' or 'name' keys or other parsing errors.
- Empty response: Indicates no user found for the search query.
- Request errors: Catches potential errors during the HTTP request.

You must use the packages requests and sys.
"""

import sys
import requests


def main():
    """
    Sends a POST request to the search API and processes the response.
    """

    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": letter}

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        response.raise_for_status()

        try:
            data = response.json()
            if data and "id" in data and "name" in data:
                print(f"[{data['id']}] {data['name']}")
            else:
                print("No result" if not data else "Not a valid JSON (missing 'id' or 'name')")

        except ValueError:
            print("Not a valid JSON (parsing error)")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

