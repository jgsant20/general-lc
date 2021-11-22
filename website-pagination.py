items = [
  ['item1', '10', '15'], 
  ['item2', '3', '4'],
  ['item3', '17', '8']
]
sortParameter = 1
sortOrder = 0
itemsPerPage = 2
pageNumber = 1

reverse = True if 0 else False
sortedItems = sorted(items, key=lambda x: int(x[sortParameter]), reverse=reverse)

print(sortedItems[itemsPerPage * pageNumber: itemsPerPage * pageNumber + itemsPerPage])