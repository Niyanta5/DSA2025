class HashMap:
    def __init__(self):
        self.map = []
        
        
    def put(self, key, value):
        """insert or update a keyvalue pair"""
        for pair in self.map:
            if pair[0] == key:
                pair[1] = value
                return
            
        self.map.append([key, value])
        
    def get(self,key):
        for pair in self.map:
            if pair[0] == key:
                return pair[1]
        return None

        
hashmap = HashMap()
hashmap.put("name", "Alice")
result = hashmap.get("name")
print(result)

    
    
    
    
    
    
    