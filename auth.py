#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from mastodon import Mastodon
from getpass import getpass
from os import path
from bs4 import BeautifulSoup
# import re

api_base_url = "https://botsin.space"
scopes = ["read:statuses", "read:accounts", "read:follows", "write:statuses"]

if not path.exists("clientcred.secret"):

    print("No clientcred.secret, registering application")
    Mastodon.create_app("moviepun", api_base_url=api_base_url, to_file="clientcred.secret", scopes=scopes, website="https://github.com/Lynnesbian/moviepun")

if not path.exists("usercred.secret"):
    print("No usercred.secret, registering application")
#    email = input("Email: ")
#    password = getpass("Password: ")
    client = Mastodon(client_id="clientcred.secret", api_base_url=api_base_url)
#    client.log_in(email, password, to_file="usercred.secret")
    print("Visit this url:")
    print(client.auth_request_url(scopes=scopes))
    client.log_in(code=input("Secret: "), to_file="usercred.secret", scopes=scopes)

print("Done! Have a nice day!")
