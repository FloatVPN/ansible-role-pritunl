import sys, re, json

profiles = []

for line in sys.stdin:
        #pattern = re.compile("[a-z0-9]{32}")
        #print(pattern.search(line))

        if (re.search(r"[a-z0-9]{32}", line)):
                line_split = list(filter(lambda item: item, [x.strip() for x in line.split('|')]))
                #print(line_split)
                item = dict(id=line_split[0],name=line_split[1],status=line_split[2],server=line_split[3],ip=line_split[4])
                profiles.append(item)

print(json.dumps(profiles))