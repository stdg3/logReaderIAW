

ss = "25/10/2021 09:42:46:  Oscar Martinez..............25.10.2021 09:42:46...........CheckIn"
print(ss)
def standartize(s):
    for _ in range(2):
        startt = s.find("....")
        endd = None
        for c in range(startt, len(s)):
            if s[c] != ".":
                endd = c
                break
        s = s.replace(s[startt: endd], " ")
    return s

# print(standartize(ss))
# print(ss)

def isintmi(line):
    checkIndex = line.find("  ")
    if line[checkIndex + 2].isnumeric():
        return True
    return False

print(isintmi(ss))

"""
25/10/2021 06:43:18:  Dwight Schrute 25.10.2021 06:43:11 CheckIn
25/10/2021 07:00:25:  Michael Scott 25.10.2021 07:00:25 CheckIn
25/10/2021 07:22:29:  Jim Halpert 25.10.2021 07:22:23 CheckIn
25/10/2021 07:25:34:  Pam Beesly 25.10.2021 07:25:34 CheckIn
25/10/2021 07:25:40:  Pam Beesly 25.10.2021 07:25:35 CheckIn
25/10/2021 07:52:26:  Ryan Howard 25.10.2021 07:52:20 CheckIn
25/10/2021 08:12:59:  Andy Bernard 25.10.2021 08:12:59 CheckIn
25/10/2021 08:16:50:  Angela Martin 25.10.2021 08:16:44 CheckIn
25/10/2021 08:29:53:  Kelly Kapoor 25.10.2021 08:29:54 CheckIn
25/10/2021 08:30:00:  Toby Flenderson 25.10.2021 08:29:48 CheckIn
25/10/2021 08:52:16:  Creed Bratton 25.10.2021 08:52:16 CheckIn
25/10/2021 09:12:02:  Darryl Philbin 25.10.2021 09:12:02 CheckIn
25/10/2021 09:33:35:  Kevin Malone 25.10.2021 09:33:35 CheckIn
25/10/2021 09:33:53:  Meredith Palme 25.10.2021 09:33:53 CheckIn
25/10/2021 09:42:46:  Oscar Martinez 25.10.2021 09:42:46 CheckIn
25/10/2021 10:14:17:  Phyllis Vance 25.10.2021 10:14:18 CheckIn
25/10/2021 10:33:13:  Stanley Hudson 25.10.2021 10:33:14 CheckIn
25/10/2021 11:56:54:  Pam Beesly 25.10.2021 11:56:55 CheckOut
25/10/2021 12:26:40:  Pam Beesly 25.10.2021 12:26:34 CheckIn
25/10/2021 13:55:23:  Meredith Palme 25.10.2021 13:55:23 CheckOut
25/10/2021 14:43:31:  Stanley Hudson 25.10.2021 14:43:32 CheckOut
25/10/2021 15:14:23:  Michael Scott 25.10.2021 15:14:24 CheckOut
25/10/2021 15:18:33:  Stanley Hudson 25.10.2021 15:18:34 CheckIn
25/10/2021 15:20:02:  Dwight Schrute 25.10.2021 15:19:56 CheckOut
25/10/2021 15:59:09:  Michael Scott 25.10.2021 15:59:10 CheckIn
25/10/2021 16:06:20:  Jim Halpert 25.10.2021 16:06:14 CheckOut
25/10/2021 16:17:28:  Phyllis Vance 25.10.2021 16:17:29 CheckOut
25/10/2021 16:22:38:  Andy Bernard 25.10.2021 16:22:39 CheckOut
25/10/2021 16:23:52:  Pam Beesly 25.10.2021 16:23:46 CheckOut
25/10/2021 16:51:29:  Ryan Howard 25.10.2021 16:51:23 CheckOut
25/10/2021 16:51:36:  Angela Martin 25.10.2021 16:51:29 CheckOut
25/10/2021 17:05:37:  Kelly Kapoor 25.10.2021 17:05:38 CheckOut
25/10/2021 17:29:19:  Meredith Palme 25.10.2021 17:29:19 CheckOut
25/10/2021 17:34:34:  Creed Bratton 25.10.2021 17:34:34 CheckOut
25/10/2021 17:51:22:  Darryl Philbin 25.10.2021 17:51:23 CheckOut
25/10/2021 18:24:28:  Michael Scott 25.10.2021 18:24:28 CheckOut
25/10/2021 18:30:44:  Toby Flenderson 25.10.2021 18:30:38 CheckOut
25/10/2021 19:34:56:  Oscar Martinez 25.10.2021 19:34:57 CheckOut
25/10/2021 19:36:13:  Stanley Hudson 25.10.2021 19:36:14 CheckOut
25/10/2021 20:30:54:  Meredith Palme 25.10.2021 20:30:55 CheckOut
25/10/2021 20:31:00:  Kevin Malone 25.10.2021 20:30:57 CheckOut
"""
q = "25/10/2021 20:" , "25/10/2021 20:", "25/10/2022 20:"

print(q[:10])
date = q[:10]

d = {}

if date in d:
    pass
else:
    d[date] = "a"

print(d)
