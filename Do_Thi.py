import numpy as np
import matplotlib.pyplot as plt

# ==============================
# Sinh dữ liệu hàm số
# ==============================

# Tạo 256 giá trị x từ -pi đến pi
X = np.linspace(-np.pi, np.pi, 256)

# Tính cos(x) và sin(x)
C = np.cos(X)
S = np.sin(X)

# ==============================
# Kiểm tra dữ liệu
# ==============================

print(f"X: số lượng = {len(X)}, khoảng = [{np.min(X):.2f}, {np.max(X):.2f}]")
print(f"Cos(X): số lượng = {len(C)}, khoảng = [{np.min(C):.2f}, {np.max(C):.2f}]")
print(f"Sin(X): số lượng = {len(S)}, khoảng = [{np.min(S):.2f}, {np.max(S):.2f}]")

# ==============================
# Vẽ đồ thị
# ==============================

# Vẽ hàm cos(x)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")

# Vẽ hàm sin(x)
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

# Giới hạn trục X
plt.xlim(X.min() * 1.1, X.max() * 1.1)

# Các mốc trên trục X
plt.xticks(
    [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
    [r"$-\pi$", r"$-\pi/2$", r"$0$", r"$+\pi/2$", r"$+\pi$"]
)

# Giới hạn trục Y
plt.ylim(-1.1, 1.1)

# Các mốc trên trục Y
plt.yticks(
    [-1, 0, 1],
    [r"$-1$", r"$0$", r"$+1$"]
)

# Hiển thị đồ thị
plt.show()