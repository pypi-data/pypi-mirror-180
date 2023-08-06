"""Email address utility class."""

from .email_address import (
    DisplayEmailAddress,
    EmailAddress,
    InvalidAddressError,
    InvalidDomainError,
    InvalidLocalPartError,
)

__all__ = (
    'DisplayEmailAddress',
    'EmailAddress',
    'InvalidAddressError',
    'InvalidDomainError',
    'InvalidLocalPartError',
)
