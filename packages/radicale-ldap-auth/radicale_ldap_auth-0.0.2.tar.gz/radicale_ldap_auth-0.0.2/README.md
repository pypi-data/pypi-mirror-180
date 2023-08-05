# Radicale IMAP authentication plugin

LDAP authentication plugin for [Radicale](http://radicale.org/).

## Installation

    python3 -m pip install radicale_ldap_auth

## Configuration

    [auth]
    type = radicale_ldap_auth
    ldap_url = ldap://examle.com
    ldap_port = 389
    ldap_user_postfix = examle.com

## License

[GPL-3.0](LICENSE)
