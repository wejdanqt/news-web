from django.core.validators import RegexValidator
from django.utils.translation import ngettext, ugettext_lazy as _


class NationalIdValidator(RegexValidator):
    regex = r"\b[12]\d{9}\b"
    message = _(
        'Enter a valid national ID'
    )
    flags = 0


class PhoneNumberValidator(RegexValidator):
    regex = r"(?:\+?0*?966)?0?5[0-9]{8}"
    message = _(
        'Enter a valid phone number'
    )
    flags = 0
