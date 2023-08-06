"""Email address utility class."""

from __future__ import annotations

import email.utils
import re
from typing import Any, TYPE_CHECKING, cast

import idna

import netaddr

if (TYPE_CHECKING):
    from collections.abc import Sequence


class InvalidAddressError(Exception):
    """Exception for invalid email addresss."""

    def __init__(self, value: str) -> None:
        super().__init__(f'Invalid email address: {value}')


class InvalidLocalPartError(Exception):
    """Exception for invalid email address local parts."""

    def __init__(self, value: str) -> None:
        super().__init__(f'Invalid email address local part: {value}')


class InvalidDomainError(Exception):
    """Exception for invalid domain names."""

    def __init__(self, value: str) -> None:
        super().__init__(f'Invalid domain name: {value}')


DOT_STRING_VALID_RE = re.compile("^[a-zA-Z0-9\u0080-\U0010FFFF.!#$%&'*+/=?^_`{|}~-]+$")
QUOTED_STRING_VALID_RE = re.compile('''^[a-zA-Z0-9\u0080-\U0010FFFF\t.!#$%&'*+/=?^_`{|}~ "(),:;<>@\\[\\\\\\]-]+$''')
ESCAPE_RE = re.compile(r'\\[\\"]')


class EmailAddress:
    """Parse and manipulate email addresses."""

    display_name: (str | None)
    _local_part: str
    _domain: (str | None)
    _domain_address: (netaddr.IPAddress | None)

    def __init__(self, value: (str | EmailAddress)) -> None:
        self.parse(value)

    def _split_display_name(self, value: str) -> tuple[(str | None), str]:
        display, address = email.utils.parseaddr(value)
        return (display if (display) else None, address)

    def _parse_local_part(self, local_part: str) -> None:
        def unescape(match: re.Match) -> str:
            return match.group(0)[1]

        local_part = local_part.strip()
        if (local_part.startswith('"') and local_part.endswith('"')):  # quoted string
            local_part = local_part[1:-1]
            local_part = ESCAPE_RE.sub(unescape, local_part)
            if (not QUOTED_STRING_VALID_RE.match(local_part)):
                raise InvalidLocalPartError(local_part)
        else:  # dot string
            if (not DOT_STRING_VALID_RE.match(local_part)):
                raise InvalidLocalPartError(local_part)
            if (local_part.startswith('.') or local_part.endswith('.') or ('..' in local_part)):
                raise InvalidLocalPartError(local_part)
        if (64 < len(local_part)):
            raise InvalidLocalPartError(local_part)

        self._local_part = local_part

    def _parse_domain(self, domain: str) -> None:
        domain = domain.strip()
        if (domain.startswith('[') and domain.endswith(']')):
            try:
                if (domain.lower().startswith('[ipv6:')):
                    self._domain_address = netaddr.IPAddress(domain[6:-1])
                else:
                    self._domain_address = netaddr.IPAddress(domain[1:-1])
                self._domain = None
                return
            except Exception:
                raise InvalidDomainError(domain)

        self._domain = self.normalize_domain(domain)
        self._domain_address = None

    def parse(self, value: (str | EmailAddress)) -> None:
        """Parse an email address, raises exceptions if invalid."""
        value = str(value)
        display_name, value = self._split_display_name(value)
        if ('@' not in value):
            raise InvalidAddressError(value)

        self.display_name = display_name
        local_part, domain = value.split('@', 1)
        self._parse_local_part(local_part)
        self._parse_domain(domain)

    def __eq__(self, other: Any) -> bool:
        """Compare to other."""
        if (isinstance(other, str)):
            try:
                other = EmailAddress(other)
            except Exception:
                return False
        if (isinstance(other, EmailAddress)):
            return ((self._local_part == other._local_part)
                    and (self._domain == other._domain)
                    and (self._domain_address == other._domain_address))
        return False

    def __lt__(self, other: Any) -> bool:
        """Compare to other."""
        if (isinstance(other, str)):
            try:
                other = EmailAddress(other)
            except Exception:
                return False
        if (isinstance(other, EmailAddress)):
            return (self.address < other.address)
        return (self.address < other)

    def __hash__(self) -> int:
        """Get hash value of email address."""
        return hash(str(self))

    def __bool__(self) -> bool:
        """Test if empty."""
        return bool(self._local_part and (self._domain or self._domain_address))

    @classmethod
    def normalize_domain(cls, value: str) -> str:
        """Normalize a domain name, converts punycode to unicode."""
        value = value.strip().rstrip('.').lower()
        try:
            return idna.decode(value)
        except Exception:
            raise InvalidDomainError(value)

    @classmethod
    def punycode_domain(cls, value: str) -> str:
        """Normalize a domain name, converts unicode to punycode."""
        value = value.strip().rstrip('.').lower()
        try:
            return idna.encode(value).decode('ascii')
        except Exception:
            raise InvalidDomainError(value)

    @property
    def quoted(self) -> bool:
        """True if local part must be quoted."""
        return (DOT_STRING_VALID_RE.match(self._local_part) is None)

    def _quoted(self, value: str) -> str:
        if (DOT_STRING_VALID_RE.match(value) is None):
            return f'"{value}"'
        return value

    @property
    def local_part(self) -> str:
        """Get local part."""
        return self._quoted(self._local_part)

    @local_part.setter
    def local_part(self, value: str) -> None:
        self._parse_local_part(value)

    def local_part_base(self, delim: str = '+') -> str:
        """Return local part without tags."""
        if (delim in self._local_part):
            return self._quoted(self._local_part.split(delim)[0])
        return self._quoted(self._local_part)

    def tags(self, delim: str = '+') -> Sequence[str]:
        """Return list of tags in local part."""
        return self._local_part.split(delim)[1:]

    @property
    def domain(self) -> str:
        """Get domain."""
        if (self._domain_address):
            if (4 == self._domain_address.version):
                return f'[{self._domain_address}]'
            return f'[IPv6:{self._domain_address.format(netaddr.ipv6_compact)}]'
        return self._domain or ''

    @domain.setter
    def domain(self, value: str) -> None:
        self._parse_domain(value)

    @property
    def domain_punycode(self) -> str:
        """Get domain as punycode."""
        if (self._domain_address):
            if (4 == self._domain_address.version):
                return f'[{self._domain_address}]'
            return f'[IPv6:{self._domain_address.format(netaddr.ipv6_compact)}]'
        return self.punycode_domain(self._domain or '')

    @property
    def domain_address(self) -> (netaddr.IPAddress | None):
        """Return domain as IPAddress."""
        return self._domain_address

    @domain_address.setter
    def domain_address(self, address: (str | netaddr.IPAddress)) -> None:
        """Set domain address."""
        if (isinstance(address, netaddr.IPAddress)):
            self._domain_address = address
            self._domain = None
        else:
            self.domain = address

    def __str__(self) -> str:
        """Convert to string."""
        if (self.display_name):
            return f'{self._quoted(self.display_name)} <{self.local_part}@{self.domain}>'
        return f'{self.local_part}@{self.domain}'

    @property
    def punycode(self) -> str:
        """Convert to string as punycode."""
        if (self.display_name):
            return f'{self._quoted(self.display_name)} <{self.local_part}@{self.domain_punycode}>'
        return f'{self.local_part}@{self.domain_punycode}'

    @property
    def address(self) -> str:
        """Convert only address portion to string."""
        return f'{self.local_part}@{self.domain}'

    @property
    def address_punycode(self) -> str:
        """Convert only address portion to string as punycode."""
        return f'{self.local_part}@{self.domain_punycode}'

    def __repr__(self) -> str:
        """Debug representation."""
        lines: list[str] = []
        if (self.display_name):
            lines.append(f'Display name: {repr(self.display_name)}')
        lines.append(f'Local part: {repr(self.local_part)}')
        lines.append(f'Domain: {repr(self.domain)}')
        return super().__repr__() + '\n' + '\n'.join([('  ' + line) for line in lines])


class DisplayEmailAddress(EmailAddress):
    """
    Email address subclass that only has a display name.

    Useful as to: or cc: that displays in received email but doesn't send.
    """

    def __init__(self, display_name: str) -> None:
        self.display_name = display_name
        self._local_part = ''
        self._domain = None
        self._domain_address = None

    def __str__(self) -> str:
        """Convert to string."""
        return f'{self._quoted(cast(str, self.display_name))} <>'

    @property
    def punycode(self) -> str:
        """Convert to string as punycode."""
        return f'{self._quoted(cast(str, self.display_name))} <>'

    @property
    def address(self) -> str:
        """Convert only address portion to string."""
        return ''

    @property
    def address_punycode(self) -> str:
        """Convert only address portion to string as punycode."""
        return ''

    def __repr__(self) -> str:
        """Debug representation."""
        lines: list[str] = []
        lines.append(f'Display name: {repr(self.display_name)}')
        return super().__repr__() + '\n' + '\n'.join([('  ' + line) for line in lines])
