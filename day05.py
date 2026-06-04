# Ngày 5 - Dictionary + Hashmap Mindset
# DIct là cấu trúc dữ liệu quan trọng nhất trong Python thực tế
# Cần hiểu sâu tại sao, không chỉ cách dùng
# Dict dùng kỹ thuật gọi là hash table ( bảng băm )
# Khi làm dict['Coca'], Python không duyệt từng key - nó tính một
# con số (hash) từ 'Coca' và nhảy thẳng đến vị trí đó. Đó là lý do O(1).

# Tạo dict
product = {
    'name': 'Coca Cola 330m',
    'quantity': 48,
    'price': 8500,
    'category': 'nước giải khát',
    'active': True
}

# Truy cập - Có 2 cách
name = product['name'] # KeyError nếu không có key
price = product.get('price') # None nếu không có key
cost = product.get('cost', 0) # 0 nếu không có key - default value

# [] dùng khi chắc chắn key tồn tại, muốn crash nếu không có
# .get() dùng khi key có thể không tồn tại

# Thêm - Sửa - Xóa
product['supplier'] = 'TCCV' # thêm key mới
product['quantity'] = 50 # sửa giá trị
del product['active'] # xóa key
remove = product.pop('supplier') # Xóa và lấy giá trị

# Iterate
for key in product:          # iterate qua keys
    print(key, product[key])

for key, value in product.items():    # interate qua cả key và value
    print(f'{key}: {value}')

# Check key tồn tại
if 'price' in product:
    print(product['price'])

# Dict lồng nhau - Cấu trúc thực tế:
inventory = {
    'sp001': {
        'name': 'Coca Cola 330ml',
        'quantity': 48,
        'price': 8500,
        'reorder_point': 12
    },
    'sp002':{
        'name': 'Pepsi 330ml',
        'quantity': 5,
        'price': 8000,
        'reorder_point': 10
    }
}

# Truy cập nested
print(inventory['sp001']['name'])
print(inventory.get('sp999',{}).get('name', 'Không tồn tại')) # Safe access

# Bài 1: .get() vs [] - Tại sao quan trọng
products = {'Coca': 48, 'Pepsi':24}
print(products['Fanta']) # KeyError - Crash
print(products.get('Fanta')) # Trả về None, code vẫn chạy nếu không có key này

# Đoạn này lỗi gì? Sửa bằng .get() với default value hợp lý

print(products['7Up']) #KeyError! - Crash
# Sửa
print(products.get('7Up'))

print(products['Coca'] + products['7Up']) # KeyError
# Sửa
print(products.get('Coca',0) + product.get('7Up',0))

# Trường hợp nào nên để crash (dùng []) thay vì dùng .get()?
# Dùng để kiểm tra tính hoàn thiện của Database

# Bài 2: Pattern đếm tần suất - Hasmap mindset
sales = ['Coca', 'Pepsi', 'Coca', '7Up', 'Coca', 'Pepsi', 'Fanta']

# Không dùng counter - tự viết bằng dict
frequency = {}
for item in sales:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)

# Cách ngắn hơn dùng .get()
frequency_v2 = {}
for item in sales:
    frequency_v2[item] = frequency_v2.get(item,0) + 1

# Tìm sản phẩm bán chạy nhất
best_saller = max(frequency, key=frequency.get)

# Bài 3: Dict lồng nhau - phân tích kho
inventory = {
    'coca_330': {'name': 'Coca Cola 330ml', 'qty': 48,'price':8500, 'reorder': 12},
    'pepsi_330':{'name': 'Pepsi 330ml', 'qty': 5, 'price': 8000, 'reorder':10},
    '7up_330':{'name': '7Up 330ml', 'qty': 0, 'price': 8200, 'reorder': 8},
    }

# Viết code trả lời:
# 1. Tổng giá trị tồn kho
total_value = sum(item['qty'] * item['price'] for item in inventory.values())
print(f'Tổng giá trị tồn kho: {total_value}')
# 2. Sản phẩm nào cần đặt thêm (qty <= reorder)?
for item in inventory.values():
    product_order = item['name']
if  item['qty'] <= item['reorder']:
    print(f'Cần order thêm: {product_order}')
#3. Sản phẩm nào hết hàng?
het_hang = []
for item in inventory.value():
    if item['qty'] == 0:
        het_hang.append(item['name'])
print(f'Sản phẩm hết hàng: {','.join(het_hang)}')
#4. Sản phẩm nào đắt nhất?
dat_nhat = max(inventory.values(), key=lambda item: item['price'])
print(f'Sản phẩm đắt nhát: {dat_nhat['price']}')
# Bài 4: Xây dict từ list = dict comprehension (giới thiệu sớm)
names = ['Coca', 'Pepsi', '7Up']
prices = [8500, 800, 8200]

# Cách 1: dùng zip
price_map = dict(zip(names, prices))

# Cách 2: dict comprehension
price_map_v2 = {name: price for name, price in zip(names, prices)}

# Bài 5: Đánh giá code LLM - dict hay list?
# Code LLM thường sinh ra:
def find_product(products_list, product_name):
    for p in products_list:
        if p['name'] == product_name:
            return p
    return None
# Nếu hàm này được gọi 1000 lần/ngày với list 500 sản phẩm:
# Tổng số bước so sánh trung bình là bao nhiêu? Nếu list 500 sản phẩm khác nhau, mỗi lần tìm 1 sản phẩm thì trung bình số lần tìm là min(1000L gọi với kết quả ngay ở lần duyệt đầu tiên) = 1000, cộng với, max(1000 lần gọi hàm với sản phẩm này ở cuối list) = 1000*500, chia 2
# Refactor để đạt O(1) lookup - cần thay đổi gì ở architecture?
products_dict = {p['name']: p for p in products_list}
def fast_find_products(products_dict, products_name):
    return products_dict.get(products_name)

