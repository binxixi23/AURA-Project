class KinematicAgent:
    """Điều khiển cơ khí, robot tự hành di chuyển và giữ thăng bằng (Series Elastic Actuators - SEA)"""
    def __init__(self):
        print("[Kinematic] Kết nối phần cứng ROS2 và hệ thống động cơ...")

    def execute_movement(self, state):
        if state == "NORMAL":
            print("[Kinematic] Đang chạy chế độ trợ lực Zero-Gravity nâng đỡ bệnh nhân tập đi.")
        elif state == "SAFE_HOLD":
            print("[Kinematic] 🚨 KÍCH HOẠT CHẾ ĐỘ PHÒNG THỦ: Khóa cứng toàn bộ khớp cơ khí (Lock Joint), ngăn chặn bệnh nhân ngã quỵ!")
