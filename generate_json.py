import json
alist_1 = [{"id": x, "name": "Test {}".format(x)} for x in range(1, 11)] +\
          [{"id": x, "name": "Test {}".format(x)} for x in range(31, 41)]
alist_2 = [{"id": x, "name": "Test {}".format(x)} for x in range(11, 21)] +\
          [{"id": x, "name": "Test {}".format(x)} for x in range(41, 51)]
alist_3 = [{"id": x, "name": "Test {}".format(x)} for x in range(21, 31)] +\
          [{"id": x, "name": "Test {}".format(x)} for x in range(51, 61)]
with open('data_1.json', 'w') as outfile:
    json.dump({"1": alist_1}, outfile)
with open('data_2.json', 'w') as outfile:
    json.dump({"2": alist_2}, outfile)
with open('data_3.json', 'w') as outfile:
    json.dump({"3":  alist_3}, outfile)
