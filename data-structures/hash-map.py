class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]
        
t = HashTable()

############# Exercise One #############
print("")
print("############ Answers to Exercise One ################")
print("")

with open("./datas/nyc_weather.csv", "r") as file:
    temps = []
    
    for line in file:
        row = line.strip().split(',')
        try:
            temps.append(int(row[1]))
        except:
            pass

print(temps)

print(f"the average temperature in first week of Jan was: {sum(temps[:7])/len(temps[:7])}")

print (f"the max temperature in the first 10 days of Jan was: {max(temps[:10])}")

############# Exercise Two #############
print("")
print("############ Answers to Exercise Two ################")
print("")

with open("./datas/nyc_weather.csv", "r") as file:
    content = []
    
    for line in file:
        row = line.strip().split(',')
        content.append(row)
        
    for index, kv in enumerate(content):
        try:
            t[kv[0]] = int(kv[1])
        except:
            pass

            
for i in t.arr:
    print (i)
    
print(f"the temperature on Jan 9 was: {t['Jan 9']}")
print(f"the temperature on Jan 4 was: {t['Jan 4']}")


############# Exercise Three #############
print("")
print("############ Answers to Exercise Three ################")
print("")

word_count = {}
with open("./datas/poem.txt", "r") as f:
    poem = f.read().replace('\n', ' ')
    tokens = poem.split(' ')
    for token in tokens:
        token = token.replace(",", "").replace(";", "").replace("!", "").replace(".", "").replace("—", "")
        if token != "":
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1

# Print word count
for key, value in word_count.items():
    print(f"{key}: {value}")
