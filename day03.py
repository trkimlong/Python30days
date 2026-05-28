# Day 03: String + Tư duy Big O đầu tiên
# Lý thuyết cần nhớ:
# - String là một chuỗi các ký tự, có thể được định nghĩa bằng dấu nháy đơn hoặc đôi.
# - String có thể được truy cập bằng chỉ số (index)
# - String có thể được cắt (slicing) để lấy một phần của chuỗi
# - String có thể được nối (concatenation) bằng toán tử +
# - String có thể được lặp (iteration) bằng vòng lặp for
# - String có thể được kiểm tra độ dài bằng hàm len()
# - String có thể được so sánh bằng toán tử ==, !=, <, >, <=, >=
# - String có thể được tìm kiếm bằng phương thức find() hoặc index
# - String có thể được thay thế bằng phương thức replace()
# - String có thể được chuyển đổi thành chữ hoa hoặc chữ thường bằng phương thức upper() hoặc lower()
# - String có thể được tách thành một danh sách bằng phương thức split()
# - String có thể được nối lại thành một chuỗi bằng phương thức join()
# - String có thể được định dạng bằng phương thức format() hoặc f-string
# - Hàm count() - đếm số lần xuất hiện của một ký tự hoặc chuỗi con trong một chuỗi
# - Hàm startswith() - kiểm tra xem một chuỗi có bắt đầu bằng một chuỗi con hay không
# - Hàm endswith() - kiểm tra xem một chuỗi có kết thúc bằng một chuỗi con hay không
#Methods quan trọng:
#strip() - loại bỏ khoảng trắng ở đầu và cuối chuỗi
#split() - tách chuỗi thành một danh sách các phần tử dựa trên  một ký tự phân cách
#join() - nối một danh sách các phần tử thành một chuỗi với một ký tự phân cách
#replace() - thay thế một phần của chuỗi bằng một phần khác
#find() - tìm kiếm một phần của chuỗi và trả về vị trí của nó
#count() - đếm số lần xuất hiện của một phần của chuỗi

# Big O - Tư duy hiệu suất
# - O(1) - Constant Time: Thời gian thực thi không phụ thuộc vào kích thước của dữ liệu đầu vào. Ví dụ: truy cập một phần tử trong một mảng.
# - O(n) - Linear Time: Thời gian thực thi tăng tuyến tính với kích thước của dữ liệu đầu vào. Ví dụ: duyệt qua tất cả phần tử trong một mảng.
# - O(n^2) - Quadratic Time: Thời gian thực thi tăng theo bình phương kích thước của dữ liệu đầu vào. Ví dụ: hai vòng lặp lồng nhau để duyệt qua tất cả cặp phần tử trong một mảng.
# - O(log n) - Logarithmic Time: Thời gian thực thi tăng theo logarit của kích thước của dữ liệu đầu vào. Ví dụ: tìm kiếm nhị phân trong một mảng đã sắp xếp.

# Bài tập:
# Bài 1: Slicing thực tế
from os import name


from os import name


date_str = "15/01/2024"
# Tách ngày, tháng, năm bằng split và bằng slicing. Cách nào rõ hơn và tại sao?
# Cách 1: Sử dụng split
print(date_str.split('/'))
# Cách 2: Sử dụng slicing
day = date_str[0:2]
month = date_str[3:5]
year = date_str[6:10]
print(f"day: {day}, month: {month}, year: {year}")
# Cách nào rõ hơn? Cách sử dụng split rõ hơn vì nó trực tiếp tách chuỗi dựa trên ký tự phân cách, trong khi cách sử dụng slicing yêu cầu phải biết chính xác vị trí của các phần tử trong chuỗi, điều này có thể gây nhầm lẫn nếu định dạng chuỗi thay đổi.

# Bài 2: Chuẩn hóa tên sản phẩm
def normalize_product_name(name: str) -> str:
    return name.strip().upper()
print(normalize_product_name(' Laptop Dell'))

# Bài 3: Parse CSV thủ công - không dùng thư viện
row = '2024-01-15,Coca Cola 330ml,24,8500,204000'
parts = row.split(',')
date = parts[0]
product_name = parts[1].strip()
quantity = int(parts[2])
unit_price = int(parts[3])
total = int(parts[4])
# Kiểm tra: total có bằng quantity * unit_price không?
assert total == quantity * unit_price, f'Dữ liệu không khớp: {total} != {quantity * unit_price}'

#Bài 4: Big O thực tế - tìm sản phẩm theo tên
products_list = [
        {'name': 'Coca', 'qty': 48},
        {'name': 'Pepsi', 'qty': 24},
        {'name': 'Fanta', 'qty': 36}
        # ... Giả sử có 10000 sản phẩm
]
# Cách O(n) - phải duyệt hết list
def find_by_name_slow(products, name):
    for p in products:
        if p['name'] == name:
            return p
    return None
print(find_by_name_slow(products_list, 'Coca')) # In ra dict của sản phẩm có tên Coca

#Cách O(1) - dùng dict
products_dict = {p['name']: p for p in products_list}
def find_by_name_fast(products_dict, name):
    return products_dict.get(name) # Trả về dict của sản phẩm có tên name hoặc None nếu không tìm thấy
print(find_by_name_fast(products_dict, 'Fanta')) # In ra dict của sản phẩm có tên Fanta

# Câu hỏi: Với 10,000 sản phẩm, bạn tìm 1,000 lần/ ngày
# Cách nào nhanh hơn? Bao nhiêu lần?
# Trả lời: đường nhiên là cách O(1) sẽ nhanh hơn rất nhiều, mỗi ngày 1000 lần tìm, thì cách O(1) luôn là 1000 phép tính, còn O(n) sẽ là 1000*10000 nếu xui còn hên là 1000 lần còn trung bình thì 1000*5000

#Bài 5: Debug string
data = 'Hanoi,Ho Chi Minh,Da Nang,Hue'
cities = data.split[','] # Lỗi gì? ( đọc eror message trước khi sửa)
# split là hàm dựng sẵn, dùng [] là sai
first= cities[1] # đay là thành phố nào?
# Ho Chi Minh
last = cities[-0] # logic error, tại sao?
# trên đời làm gì có -0, -1 mới đúng
upper_cities = cities.upper() # lỗi gì? ( list không có .upper())
print(upper_cities)

