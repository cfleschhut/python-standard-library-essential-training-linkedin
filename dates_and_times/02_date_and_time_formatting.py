import datetime

now = datetime.datetime.now()

print(now.strftime("%a, %A, %w, %d"))
print(now.strftime("%b, %B, %m"))
print(now.strftime("%H, %I, %M, %S, %p"))
print(now.strftime("%c"))
print(now.strftime("%X"))

print(now.strftime("%m/%d/%y"))
print(now.strftime("%A %d, %B %Y"))
print(now.strftime("%m/%d/%y, %I:%M %p"))
