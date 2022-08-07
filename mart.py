items = []
index = -1

def mart(query, item_name, item_price):
    global index 
    if query == 'INSERT':
        item = [item_name, item_price]
        items.append(item)
        items.sort(key = lambda x: (x[1], x[0]))
    elif query == 'VIEW':
        index += 1
        return items[index][0]


if __name__ == '__main__':

    mart('INSERT','Pizza', 5)
    mart('INSERT','Gum', 1)
    print(mart('VIEW',"-","-"))

    mart('INSERT','Milk', 4)
    mart('INSERT','Coffee', 3)
    print(mart('VIEW',"-","-"))

    # mart('INSERT','Pizza', 5)
    # mart('INSERT','Gum', 1)
    # print(mart('VIEW',"-","-"))

    mart('INSERT','A', 4)
    mart('INSERT','B', 10)
    print(mart('VIEW',"-","-"))

    print(mart('VIEW',"-","-"))
