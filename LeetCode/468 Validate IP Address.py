# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

# A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

# 1 <= xi.length <= 4
# xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
# Leading zeros are allowed in xi.
# For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        version = None

        if '.' in queryIP:
            version = 'v4'
        elif ':' in queryIP:
            version = 'v6'
        else:
            return "Neither"

        if version == 'v4':
            arr = queryIP.split('.')
            if len(arr) != 4: return "Neither"
            for IP in arr:
                if not IP.isdigit() or (len(IP)>1 and IP[0] == '0') or int(IP) < 0 or int(IP) > 255:
                    return "Neither"
            return "IPv4"

        if version == 'v6':
            arr = queryIP.split(':')
            if len(arr) != 8: return "Neither"
            alnums = 'abcdefABCDEF0123456789'

            for IP in arr:
                if len(IP) > 4 or len(IP) < 1: return "Neither"
                for c in IP:
                    if c not in alnums: return "Neither"
            return 'IPv6'