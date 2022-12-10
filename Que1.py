
import re

phone_regex = '^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$'
phone_number = input()
if re.search(phone_regex, phone_number):
    print("Valid")

else:
    print("invalid")

# ● 2124567890
# ● 212-456-7890
# ● (212)456-7890
# ● (212)-456-7890
# ● 212.456.7890
# ● 212 456 7890
# ● +12124567890
# ● +12124567890
# ● +1 212.456.7890
# ● +212-456-7890 (Thiśone is showing Invalid and EVeryone is valid!)
# ● 1-212-456-7890