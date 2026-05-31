# Ngày 4 - List + Collections tư duy
# CRUD trên list
products  = ['Coca', 'Pepsi', '7Up', 'Fanta']
products.append('Sprite') # thêm cuối
products.insert(1, 'Mirinda') # Chèn vào vị trí 1
products.remove('Mirinda') # xóa theo giá trị
popped = products.pop() # lấy và xóa phần tử cuối
popped_at = products.pop(1) # lấy và xóa theo index

# Truy vấn
print(len(products))

if 'Coca' in products:
    print('Có hàng')
else : print('Hết hàng') # True/False - O(n)

print(products.index('7Up')) # Vị trí của '7Up'
print(products.count('Coca')) # Đếm số lần xuất hiện của phần từ 'Coca'

# Sort
products.sort() #sort tại chỗ, thay đổi list gốc
sorted_copy = sorted(products) #  tạo bản copt list đã sort, giữ list gốc
products.sort(reverse=True) # Sort ngược

# Slice products[start:stop:step]
first_two = products[:2]
last_two = products[-2:]
every_other = products[::2]

#Copy trap - Bug kinh điển:
list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)
print(list_a)

# Sửa đúng cách
list_c = list_a.copy() #Shallow copy
list_d = list_a[:] # Cũng là Shallow copy
list_e = list(list_a) # cũng được

# Thực hành

# Bài 1: Dự đoán output TRƯỚC khi chạy
products = ['Coca', 'Pepsi', '7Up', 'Fanta'] 
products.append('Sprite') # ['Coca', 'Pepsi', '7Up', 'Fanta', 'Sprite']
products.insert(1, 'Mirinda') # ['Coca', 'Mirinda', 'Pepsi', '7Up', 'Fanta', 'Sprite']
products.remove('Pepsi') # ['Coca', 'Mirinda', 'Pepsi', '7Up', 'Fanta', 'Sprite']
print(products) # ['Coca', 'Mirinda', '7Up', 'Fanta', 'Sprite']
print(products[2]) # 7Up
print(len(products)) # 5
print('Coca' in products) # True

# Bài 2: Nested list _ Bảng dữ liệu đơn giản
inventory = [
    ['Coca Cola 330ml', 48 ,8500],
    ['Pepsi 330ml', 24, 8000],
    ['7Up 330ml', 0, 8200],
    ['Fanta 330ml', 12, 8500],
]
# Câu hỏi (Viết code trả lời từng câu):
# 1, Tên sản phẩm đầu tiên?
print(inventory[0][0])
# 2, Sô lượng của Pepsi?
for item in inventory:
    if 'Pepsi' in item[0]:
        print(item[1])
# 3, Sản phẩm nào hết hàng?
    if item[1] == 0:
        print(item[0])
#4, Tổng giá trị tồn kho
print(sum(item[1] for item in inventory))

# Bài 3: Loại bỏ trùng lặp giữ thứ tự
raw = ['Coca', 'Pepsi', 'Coca', '7Up', 'Pepsi', 'Coca']

# Cách 1: dùng set (nhanh nhưng mất thứ tự)
unique_set = list(set(raw))
print(unique_set)

# Cách 2: giữ thứ tự xuất hiện đầu tiên (O(n))
seen = set()
unique_ordered = []
for item in raw:
    if item not in seen:
        seen.add(item)
        unique_ordered.append(item)

# Cách nào dùng khi nào? Giải thích?
# Khi làm gọn data mà không cần giữ thứ tự, còn cách 2 dùng trong 
# trường hợp tinh gọn data và thứ tự có ý nghĩa

# Bài 4: Copy trap thực tế
original = [{'name':'Coca', 'qty': 48}]
copy = original.copy() # shallow copy
copy[0]['qty'] = 0 # sửa bên copy
print(original[0]['qty']) # 0 hay 48? Tại sao?
# 0 vì copy() chỉ tạo bản sao list và phần tử bên trong vẫn trỏ cùng 1 địa chỉ, nên thay đổi phần tử của dict bên trong list thì list cũ cũng thay đổi theo
# Tạo bản sao cho dict
import copy
deep_copy = copy.deepcopy(original)

# Bài 5: Sort với key function
products = [
    ('Coca Cola', 48, 8500),
    ('Pepsi', 5, 8000),
    ('7Up', 120, 8200),
    ('Fanta', 24, 8500),
]
# Sort theo số lượng tăng dần
by_qty = sorted(products, key=lambda x: x[1])
print(by_qty)

#Sort theo giá trị tồn kho giảm dần (qty * price)
by_value = sorted(products, key=lambda x: x[1] * x[2], reverse=True)
print(by_value)

# lambda là gì? ' Với mỗi x, lấy x[1]'
# lambda x: x1[1] = def get_qty(x): return x[1]


