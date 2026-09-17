import numpy as np #//sử dụng thư viện numpy để sinh dữ liệu ngẫu nhiên
import matplotlib.pyplot as plt #//sử dụng thư viện matplotlib để hiển thị biểu đồ

# ============================================================
# BÀI: HIỂN THỊ NGẪU NHIÊN 50 HÌNH TRÒN
# ============================================================

# Số lượng hình tròn
N = 50


# ============================================================
# 1. SINH NGẪU NHIÊN TÂM CỦA HÌNH TRÒN
# ============================================================

# Tọa độ x của 50 hình tròn, x thuộc [0, 1]
x = np.random.rand(N)

# Tọa độ y của 50 hình tròn, y thuộc [0, 1]
y = np.random.rand(N)


# ============================================================
# 2. SINH NGẪU NHIÊN MÀU SẮC
# ============================================================

# Mỗi hình tròn có một giá trị màu ngẫu nhiên thuộc [0, 1]
colors = np.random.rand(N)


# ============================================================
# 3. SINH NGẪU NHIÊN BÁN KÍNH
# ============================================================

# Bán kính r của mỗi hình tròn thuộc [0, 1]
r =np.random.rand(N)


# ============================================================
# 4. TÍNH DIỆN TÍCH HÌNH TRÒN
# ============================================================

# Công thức:
# area = pi * r^2
area = np.pi * r**2

# ============================================================
# 5. KIỂM TRA DỮ LIỆU
# ============================================================

print("===== THÔNG TIN DỮ LIỆU =====")

print(f"Số lượng hình tròn: {N}")

print(f"\nX:")
print(f"  Số lượng: {len(x)}")
print(f"  Giá trị nhỏ nhất: {min(x):.2f}")
print(f"  Giá trị lớn nhất: {max(x):.2f}")

print(f"\nY:")
print(f"  Số lượng: {len(y)}")
print(f"  Giá trị nhỏ nhất: {min(y):.2f}")
print(f"  Giá trị lớn nhất: {max(y):.2f}")

print(f"\nMàu sắc:")
print(f"  Số lượng: {len(colors)}")
print(f"  Giá trị nhỏ nhất: {min(colors):.2f}")
print(f"  Giá trị lớn nhất: {max(colors):.2f}")

print(f"\nBán kính:")
print(f"  Số lượng: {len(r)}")
print(f"  Giá trị nhỏ nhất: {min(r):.2f}")
print(f"  Giá trị lớn nhất: {max(r):.2f}")

print(f"\nDiện tích:")
print(f"  Số lượng: {len(area)}")
print(f"  Giá trị nhỏ nhất: {min(area):.2f}")
print(f"  Giá trị lớn nhất: {max(area):.2f}")


# ============================================================
# 6. HIỂN THỊ 50 HÌNH TRÒN
# ============================================================

plt.scatter(
    x,
    y,
    s=area * 500,
    c=colors,
    alpha=0.5
)

# Giới hạn trục X và Y từ 0 đến 1
plt.xlim(0, 1)
plt.ylim(0, 1)

# Tên biểu đồ
plt.title("50 hình tròn ngẫu nhiên")

# Tên trục
plt.xlabel("X")
plt.ylabel("Y")

# Hiển thị lưới
plt.grid(True)

# Hiển thị biểu đồ
plt.show()