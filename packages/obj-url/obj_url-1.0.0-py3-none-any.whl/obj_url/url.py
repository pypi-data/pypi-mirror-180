"""URL utility class."""

from __future__ import annotations

import copy
from typing import Any, TYPE_CHECKING, overload
from urllib import parse as url_parse

import idna

import netaddr

if (TYPE_CHECKING):
    from collections.abc import Mapping, Sequence


class InvalidDomainError(Exception):
    """Exception for invalid domain names."""

    def __init__(self, domain: str) -> None:
        super().__init__(f'Invalid domain name: {domain}')


class InvalidPortError(Exception):
    """Exception for invalid port value."""

    def __init__(self, error: str) -> None:
        super().__init__(f'Invalid port value: {error}')


DEFAULT_PORTS = {
    'ftp': 21,
    'fish': 22,
    'sftp': 22,
    'ssh': 22,
    'telnet': 23,
    'dns': 53,
    'gopher': 70,
    'finger': 79,
    'http': 80,
    'pop': 110,
    'nntp': 119,
    'smb': 137,
    'imap': 143,
    'snmp': 161,
    'ldap': 389,
    'https': 443,
    'afp': 548,
    'ldaps': 636,
    'acap': 674,
    'rsync': 873,
    'imaps': 993,
    'ircs': 994,
    'pops': 995,
    'h323': 1720,
    'dict': 2628,
    'stun': 3478,
    'turn': 3478,
    'aaa': 3868,
    'aaas': 3868,
    'iax': 4569,
    'sip': 5060,
    'sips': 5061,
    'xmpp': 5222,
    'stuns': 5349,
    'turns': 5349,
    'coap': 5683,
    'coaps': 5684,
    'vnc': 5900,
    'irc': 6667,
    'mumble': 64738,
}


class URL:
    """Parse and manipulate URLs."""

    _scheme: (str | None)
    username: (str | None)
    password: (str | None)
    _hostname: (str | None)
    _host_address: (netaddr.IPAddress | None)
    _port: (int | None)
    _path: str
    _query: dict[str, list[str]]
    _fragment: (str | None)

    def __init__(self, value: (str | URL | None) = None) -> None:
        self.parse(value)

    def parse(self, value: (str | URL | None) = None) -> None:
        """Parse string."""
        parts = url_parse.urlsplit(str(value or ''))
        self.scheme = parts.scheme
        self.username = parts.username
        self.password = parts.password
        self.host = parts.hostname
        try:
            self.port = parts.port
        except ValueError as error:
            raise InvalidPortError(str(error))
        self.path = parts.path
        self.query_string = parts.query
        self.fragment = parts.fragment

    def __eq__(self, other: Any) -> bool:
        """Compare to other."""
        if (isinstance(other, str)):
            try:
                other = URL(other)
            except Exception:
                return False
        if (isinstance(other, URL)):
            return ((self._scheme == other._scheme)
                    and (self.username == other.username)
                    and (self.password == other.password)
                    and (self._hostname == other._hostname)
                    and (self._host_address == other._host_address)
                    and (self.port == other.port)
                    and (self.path == other.path)
                    and (self._query == other._query)
                    and (self._fragment == other._fragment))
        return False

    def __hash__(self) -> int:
        """Get hash value of URL."""
        return hash(str(self))

    def __bool__(self) -> bool:
        """Test if empty."""
        return '' != str(self)

    @classmethod
    def _decode_domain_label(cls, label: str) -> str:
        # allow ascii outside letters, digits and hyphen
        try:
            return idna.decode(label)
        except Exception:  # noqa: S110
            pass
        if ((0 == len(label)) or (63 < len(label))):
            raise InvalidDomainError(label)
        try:
            label.encode('ascii')
            return label
        except Exception:
            raise InvalidDomainError(label)

    @classmethod
    def _encode_domain_label(cls, label: str) -> str:
        # allow ascii outside letters, digits and hyphen
        try:
            return idna.encode(label).decode('ascii')
        except Exception:  # noqa: S110
            pass
        if ((0 == len(label)) or (63 < len(label))):
            raise InvalidDomainError(label)
        try:
            label.encode('ascii')
            return label
        except Exception:
            raise InvalidDomainError(label)

    @classmethod
    def normalize_domain(cls, value: (str | None)) -> (str | None):
        """Normalize a domain name, converts punycode to unicode."""
        value = value.strip().rstrip('.').lower() if (value) else None
        if (not value):
            return None
        try:
            return '.'.join([cls._decode_domain_label(label) for label in value.split('.')])
        except Exception:
            raise InvalidDomainError(value)

    @classmethod
    def punycode_domain(cls, value: (str | None)) -> (str | None):
        """Normalize a domain name, converts unicode to punycode."""
        value = value.strip().rstrip('.').lower() if (value) else None
        if (not value):
            return None
        try:
            return '.'.join([cls._encode_domain_label(label) for label in value.split('.')])
        except Exception:
            raise InvalidDomainError(value)

    @property
    def scheme(self) -> (str | None):
        """Get scheme."""
        return self._scheme

    @scheme.setter
    def scheme(self, value: (str | None) = None) -> None:
        self._scheme = (value.strip().rstrip(':').lower() or None) if (value) else None

    def _netloc(self, hostname: (str | None)) -> (str | None):
        """Network location helper."""
        output = ''
        if (self.username is not None):
            if (self.password is not None):
                output += f'{self.username}:{self.password}@'
            else:
                output = f'{self.username}@'
        if (self._host_address is not None):
            if (6 == self._host_address.version):
                output += f'[{self._host_address.format(netaddr.ipv6_compact)}]'
            else:
                output += str(self._host_address)
        elif (hostname is not None):
            output += hostname
        if (self.port is not None):
            output += f':{self.port}'
        return output if (output) else None

    @property
    def netloc(self) -> (str | None):
        """Get network location."""
        return self._netloc(self._hostname)

    @property
    def netloc_punycode(self) -> (str | None):
        """Get network location as punycode."""
        return self._netloc(self.hostname_punycode)

    @property
    def host(self) -> (str | None):
        """Get host name or address."""
        if (self._host_address is not None):
            return self._host_address.format(netaddr.ipv6_compact)
        return self._hostname

    @host.setter
    def host(self, value: (str | None) = None) -> None:
        """Set host name or address."""
        try:
            self._host_address = netaddr.IPAddress(value)
            self._hostname = None
        except Exception:
            self._hostname = self.normalize_domain(value)
            self._host_address = None

    @property
    def host_punycode(self) -> (str | None):
        """Get host name as punycode or address."""
        if (self._host_address is not None):
            return self._host_address.format(netaddr.ipv6_compact)
        return self.hostname_punycode

    @property
    def hostname(self) -> (str | None):
        """Return hostname if specified and is not an IP address."""
        return self._hostname

    @hostname.setter
    def hostname(self, value: (str | None) = None) -> None:
        """Set hostname."""
        self.host = value

    @property
    def hostname_punycode(self) -> (str | None):
        """Return hostname in punycode if specified and is not an IP address."""
        return self.punycode_domain(self._hostname) if (self._hostname) else None

    @property
    def host_address(self) -> (netaddr.IPAddress | None):
        """Return host as IPAddress."""
        return self._host_address

    @host_address.setter
    def host_address(self, address: (str | netaddr.IPAddress | None) = None) -> None:
        """Set host address."""
        if (isinstance(address, netaddr.IPAddress)):
            self._host_address = address
            self._hostname = None
        else:
            self.host = address

    @property
    def port(self) -> (int | None):
        """Get port."""
        if ((self.scheme in DEFAULT_PORTS) and (DEFAULT_PORTS[self.scheme] == self._port)):
            return None
        return self._port

    @port.setter
    def port(self, value: (str | int | None) = None) -> None:
        """Set port."""
        self._port = int(value) if (value) else None

    @property
    def path(self) -> str:
        """Get path."""
        return '/' if ((not self._path) and (self.host or self.scheme)) else self._path

    @path.setter
    def path(self, value: (str | None) = None) -> None:
        """Set path."""
        self._path = (value or '')

    @property
    def query(self) -> (dict[str, list[str]] | None):
        """Get query arguments, this is a copy, not a live object."""
        return copy.deepcopy(self._query) if (self._query) else None

    @query.setter
    def query(self, query: (Mapping[str, (str | Sequence[str])] | None) = None) -> None:
        """Set query."""
        self._query = {}
        for name, values in (query or {}).items():
            self._query[name] = [values] if (isinstance(values, str)) else list(values)

    @property
    def query_string(self) -> (str | None):
        """Get query as string."""
        return url_parse.urlencode(self._query, doseq=True) if (self._query) else None

    @query_string.setter
    def query_string(self, value: (str | None) = None) -> None:
        """Set query from string."""
        self._query = url_parse.parse_qs(value, encoding='utf-8', keep_blank_values=True) if (value) else {}

    @overload
    def query_value(self, name: str) -> (str | None): ...  # noqa: E704
    @overload
    def query_value(self, name: str, default: str) -> str: ...  # noqa: E704
    def query_value(self, name: str, default: (str | None) = None) -> (str | None):  # noqa: E301
        """Get first value for a query argument."""
        if (name in self._query):
            return self._query[name][0]
        return default

    @overload
    def query_values(self, name: str) -> (Sequence[str] | None): ...  # noqa: E704
    @overload
    def query_values(self, name: str, default: Sequence[str]) -> Sequence[str]: ...  # noqa: E704
    def query_values(self, name: str, default: (Sequence[str] | None) = None) -> (Sequence[str] | None):  # noqa: E301
        """Get all values for a query argument, this is a copy, not a live object."""
        if (name in self._query):
            return list(self._query[name])
        return default

    def set_query_value(self, name: str, value: str) -> None:
        """Set query argument to a single value."""
        self._query[name] = [value]

    def set_query_values(self, name: str, values: Sequence[str]) -> None:
        """Set all values for a query argument."""
        self._query[name] = list(values)

    def add_query_value(self, name: str, value: str) -> None:
        """Add a value to a query argument."""
        if (name in self._query):
            self._query[name].append(value)
        else:
            self._query[name] = [value]

    def remove_query_value(self, name: str, value: str) -> None:
        """Remove a value from a query argument."""
        if (name in self._query):
            self._query[name].remove(value)
            if (not self._query[name]):
                del self._query[name]

    def remove_query_values(self, name: str) -> None:
        """Remove all values of a query argument."""
        if (name in self._query):
            del self._query[name]

    @property
    def fragment(self) -> (str | None):
        """Get fragment."""
        return self._fragment

    @fragment.setter
    def fragment(self, value: (str | None) = None) -> None:
        self._fragment = value if (value) else None

    def __str__(self) -> str:
        """Convert to string."""
        return url_parse.urlunsplit((self.scheme or '', self.netloc or '', self.path,
                                     self.query_string or '', self.fragment or ''))

    @property
    def punycode(self) -> str:
        """Convert to string as punycode."""
        return url_parse.urlunsplit((self.scheme or '', self.netloc_punycode or '', self.path,
                                     self.query_string or '', self.fragment or ''))

    def append(self, other: (str | URL)) -> None:
        """Join another URL to this one."""
        self.parse(url_parse.urljoin(str(self), str(other)))

    def join(self, other: (str | URL)) -> URL:
        """Return a version joined to another URL, does not alter self."""
        return URL(url_parse.urljoin(str(self), str(other)))

    def root(self) -> URL:
        """Return a version with / path and without query or fragment."""
        root = copy.deepcopy(self)
        root.path = '/'
        root.query = None
        root.fragment = None
        return root

    def base(self) -> URL:
        """Return a version without query or fragment."""
        base = copy.deepcopy(self)
        base.query = None
        base.fragment = None
        return base

    def __repr__(self) -> str:
        """Debug representation."""
        lines: list[str] = []
        if (self.scheme):
            lines.append(f'Scheme: {repr(self.scheme)}')
        if (self.username is not None):
            lines.append(f'Username: {repr(self.username)}')
        if (self.password is not None):
            lines.append(f'Password: {repr(self.password)}')
        if (self.host is not None):
            lines.append(f'Host: {repr(self.host)}')
        if (self.port is not None):
            lines.append(f'Port: {repr(self.port)}')
        lines.append(f'Path: {repr(self.path)}')
        if (self._query):
            lines.append('Query:')
            for name, values in self._query.items():
                for value in values:
                    lines.append(f'  {repr(name)}: {repr(value)}')
        if (self.fragment):
            lines.append(f'Fragment: {repr(self.fragment)}')
        return super().__repr__() + '\n' + '\n'.join([('  ' + line) for line in lines])
