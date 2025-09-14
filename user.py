"""
Store node / user variables and functions, handle validation and encryption of messages
"""

'''
for self

public_bytes_raw()
Allows serialization of the key to raw bytes.
convenience shortcut for calling public_bytes() with Raw encoding and Raw format.

private_bytes(encoding, format, encryption_algorithm)
Allows serialization of the key to bytes. Encoding ( PEM, DER, or Raw) and format ( PKCS8, OpenSSH or Raw ) are chosen to define the exact serialization.
'''

from os import path, urandom
from datetime import datetime
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from network_node import NetworkNode


class User(NetworkNode):
    """
    Handle user actions and data
    """
    def __init__(self, mode: str, target: str, username: str, savefile: str):
        """
        mode- establish, link, configure
        target- ip address, LATER session id
        username- name to use for session
        savefile- file to save correspondence to
        """
        self.mode: str = mode # only for launching
        self.target: str = target # another peer...
        self.username: str = username
        self.savefile: str | bool = savefile

        self._key_prv = Ed25519PrivateKey.generate()
        self.key_pub = Ed25519PrivateKey.public_key(self._key_prv)

        def __str__(self):
            return str(self.mode + self.target + self.username + self.savefile)

    #TODOS: username check and filename check. rest in the future
    def validate(self) -> None:
        """
        Validate user properties:
            - Prevent username duplicates
            - Prevent savefile duplicates, handle save directory and file name
            - Make sure target session exists or create new session (according to `mode`)
            - Verify public and private keys corrospond
        """
        self._validate_username()
        self._validate_savefile()
        self._validate_target()
        self._validate_keys()

        self._validated = True

        print("Validation complete")

    def _validate_username(self) -> None:
        if False: #_is_username_registered(self.username):
            print("Username", self.username, "already registered. Changing")
            tmp_name:str = self.username
            i = 1
            while False: #_is_username_registered(tmp_name):
                tmp_name = self.username + str(i)
                i += 1
            self.username = tmp_name

        print("Username registered as", self.username)

    def _validate_savefile(self) -> None:
        if not self.savefile:
            self.savefile = False
        elif isinstance(self.savefile, str): # get rid of warning (if reached here savefile is str)
            # strip path of extension and split into directory and file name, then expand relative
            save_dir, save_name = path.split(self.savefile)
            save_dir = path.abspath(save_dir)
            save_name = path.splitext(save_name)[0]

            # fix directory and file name if needed - new directories will not be created
            if not save_dir or not path.isdir(save_dir):
                save_dir = path.join(path.expanduser("~"), "Downloads") # todo later load from config
            if not save_name:
                save_name = "secmsg_session-" + self.username + "-" + datetime.now().strftime("%d/%m/%Y-%H:%M")
                # todo add pubkey start instead of date- add_end wont be needed

            self.savefile = path.join(save_dir, save_name)

            # add ending if name exists
            if path.isfile(self.savefile + ".txt"):
                print("file", self.savefile + ".txt", "already exists. Changing")
                tmp_savefile:str = self.savefile
                i = 1
                while path.isfile(tmp_savefile + ".txt"):
                    tmp_savefile = self.savefile + str(i)
                    i += 1
                self.savefile = tmp_savefile

            self.savefile += ".txt"
            print("Save file set to", self.savefile)
            # todo later check if file/dir writable

        else:
            raise ValueError("Savefile must be a string or empty, bro idk how u got this error tbh")

    def _validate_target(self) -> None:
        if self.mode == "link":
            if not self.target:
                raise ValueError("Target must be provided in link mode.")
            else:
                ... # todo ping node of `target`
            # todo later check if target exists
        elif self.mode == "establish":
            if self.target:
                raise ValueError("Target must not be provided in establish mode.")
            else:
                # todo generate session id from Session
                self.target = ""
        else:
            raise ValueError("Unknown mode.")

    def _validate_keys(self) -> None:
        data = urandom(32)
        signed = self._key_prv.sign(data)
        self.key_pub.verify(signed, data)

#aw man
