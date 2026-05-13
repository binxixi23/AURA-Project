import random

class PerceptionAgent:
    """Xử lý thị giác máy tính (Computer Vision) và nhận diện cảm xúc (Affective Computing)"""
    def __init__(self):
        print("[Perception] Khởi tạo hệ thống camera MediaPipe/YOLO...")

    def analyze_patient_state(self):
        # Mô phỏng quét dữ liệu thời gian thực
        heart_rate = random.randint(70, 145) # Mô phỏng nhịp tim sinh lý
        gaze_confidence = round(random.uniform(0.5, 1.0), 2)
        print(f"[Perception] Đang quét dữ liệu: Nhịp tim={heart_rate} BPM | Độ chính xác ánh mắt={gaze_confidence}")
        return {"heart_rate": heart_rate, "gaze_confidence": gaze_confidence}
