#!/usr/bin/python3
"""
Script that takes in a letter as a command-line argument,
sends a POST request to a specified URL with the letter as a parameter,
and displays the response formatted as a simple user object.
"""

import sys
import requests


def main():
    """
    Sends a POST request to a specified URL with a letter as a parameter
    and displays the response formatted as a simple user object.
    """

    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": letter}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()

        try:
            data = response.json()
            if data:
                if "id" in data and "name" in data:
                    print(f"[{data['id']}] {data['name']}")
                else:
                    print("Not a valid JSON (missing 'id' or 'name')")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON (parsing error)")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
