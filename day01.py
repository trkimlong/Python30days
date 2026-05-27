# Bài 1
shop_name = 'Cửa hàng Kim Long'
total_products = 47
revenue = 2800000
is_open = True
print(type(shop_name))
print(type(total_products))
print(f"Shop: {shop_name}")
print(f"Doanh thu: {revenue:,.0f}đ")

# Bài 2 Dự đoán output TRƯỚC khi chạy - Ghi ở phần comment trước khi chạy
x = '5'
y = 3
print(int(x) + y) # Output: 8
print(x + str(y)) # Output: 53
print(float(x) * y) # Output: 15.0
print(type(int(x) + y)) # Output: <class 'int'>

#Bài 3 : Viết không nhìn gợi ý
shop_name = 'Cửa hàng Kim Long'
number_of_employees = 3
month_revenue = 1000000
is_open = True
address = '262 Trần Hưng Đạo, phường Kon Tum, tỉnh Quãng Ngãi'
print(f"Shop: {shop_name} có số lượng nhân viên là {number_of_employees}, doanh thu tháng này khoảng {month_revenue:,.0f}VNĐ, địa chỉ tại {address} và hiện đang {'mở cửa' if is_open else 'đóng cửa'}.")

#Bài 4 : Tìm và giải thích lỗi bằng comment
name = 'laptop'
Price ='250000' # Lỗi: chữ cái đầu tiên của biến viết hoa
quantity = 10
total = Price * quantity # Lỗi: biến Price sai trước đó, và khi in ra kết quả của total sẽ in 10 lần str '250000' thay vì số nguyên
print(f'Tổng:{total}')

#Bài 5: Giải thích cho người khác nghe: tại sao Python dùng thụt dòng thay vì {} như ngôn ngữ khác, và điều đó có nghĩa gì với người đọc code.
# Python sử dụng thụt dòng để người đọc code có thể dễ dàng nhận biết các blocks, trực quan hơn. Và giúp kéo cần giữa visual struture và logic structure của code

