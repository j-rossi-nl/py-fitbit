import base64
import hashlib
import json
import os
import secrets
import string
import threading
import webbrowser
from dataclasses import dataclass
from dataclasses import field
from urllib.parse import urlencode

import cherrypy
from dotenv import dotenv_values
from dotenv import load_dotenv

from fitbit.api import AuthApi


load_dotenv(os.path.expanduser("~/.ssh/fitbit-api"))


@dataclass
class SimpleHttp:
    host: str = "127.0.0.1"
    port: int = 5000

    success_html: str = """
        <h1>You are now authorized to access the Fitbit API!</h1>
        <br/><h3>You can close this window</h3>"""
    failure_html: str = (
        """<h1>ERROR: %s</h1><br/><h3>You can close this window</h3>%s"""
    )

    thread: threading.Thread = field(init=False)
    fitbit_response: str = field(default="", init=False)
    _response: threading.Event = field(init=False)

    def __post_init__(self):
        cherrypy.config.update(
            {"server.socket_host": self.host, "server.socket_port": self.port}
        )

        self.thread = threading.Thread(target=cherrypy.quickstart, args=(self,))
        self._response = threading.Event()

    def __enter__(self):
        self.thread.start()
        return self

    def __exit__(self, type, value, traceback):
        self._response.wait()
        cherrypy.engine.exit()

    @cherrypy.expose
    def index(self, state=None, code=None, error=None):
        """
        Receive a Fitbit response containing a verification code. Use the code
        to fetch the access_token.
        """
        self.fitbit_response = code
        self._response.set()
        return f"<h1>The code: {code}</h1>"


UNRESERVED = string.ascii_letters + string.digits + "-._~"


def main():
    code_verifier = "".join(secrets.choice(UNRESERVED) for _ in range(64))
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode("utf-8")).digest()
    ).decode("utf-8")[:-1]

    params = {
        "client_id": os.environ["FITBIT_CLIENT_ID"],
        "response_type": "code",
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
        "scope": "location activity heartrate",
    }

    authorization_url = "https://www.fitbit.com/oauth2/authorize?" + urlencode(params)
    print(authorization_url)

    if input("Continue (y/n): ").lower() != "y":
        return

    with SimpleHttp() as callback:
        webbrowser.open(authorization_url)

    print(f"Fitbit Response: {callback.fitbit_response}")

    auth = AuthApi()
    auth.oauth_token(
        client_id=os.environ["FITBIT_CLIENT_ID"],
        code=callback.fitbit_response,
        code_verifier=code_verifier,
        grant_type="authorization_code",
        authorization="Basic "
        + base64.b64encode(
            f'{os.environ["FITBIT_CLIENT_ID"]}:{os.environ["FITBIT_SECRET"]}'.encode()
        ).decode("utf-8"),
    )

    auth_data = json.loads(auth.api_client.last_response.data)
    with open("auth_data.txt", "w") as out:
        json.dump(auth_data, out)


if __name__ == "__main__":
    main()
