import os

# Định nghĩa cấu trúc thư mục và nội dung file mẫu cho AURA
project_structure = {
    # 1. Các file nằm ở thư mục gốc (Root)
    "requirements.txt": "boto3==1.34.0\nopencv-python==4.9.0.80\nmediapipe==0.10.11\n",
    
    # 2. Thư mục docs
    "docs/architecture_spec.md": "# AURA Detailed Architecture Specification\n\nThis document outlines the detailed system blueprints for the Adaptive Universal Rehabilitation Agent.",

    # 3. Thư mục config
    "src/config/security_policy.json": """{
  "system_name": "AURA_Adaptive_Universal_Rehabilitation_Agent",
  "security_version": "1.0.2",
  "encryption_protocols": {
    "data_at_rest": "AES-256-GCM",
    "data_in_transit": "TLS_1.3_AES_256_GCM_SHA384",
    "data_in_use_boundary": "Hardware_Enclave_Isolated_RAM"
  },
  "edge_node_authentication": {
    "ros2_security_plugin": "SROS2_Enabled",
    "node_identity_verification": "X.509_Certificates",
    "packet_auth_frequency_ms": 1.0
  },
  "stress_handling_thresholds": {
    "patient_heart_rate_max_bpm": 140,
    "galvanic_skin_response_anomaly_score": 0.85,
    "intent_disambiguation_confidence_threshold": 0.85
  },
  "incident_response_actions": {
    "low_confidence_intent": "TRIGGER_ACTIVE_DELAY_MODE",
    "biometric_anomaly_detected": "ENGAGE_SAFE_HOLD_KINEMATICS",
    "critical_failure_override": "INITIATE_LOW_LATENCY_WEBRTC_HITL_UPLINK"
  }
}""",

    # 4. Các file Agents thông minh
    "src/agents/perception_agent.py": """import random

class PerceptionAgent:
    \"\"\"Xử lý thị giác máy tính (Computer Vision) và nhận diện cảm xúc (Affective Computing)\"\"\"
    def __init__(self):
        print("[Perception] Khởi tạo hệ thống camera MediaPipe/YOLO...")

    def analyze_patient_state(self):
        # Mô phỏng quét dữ liệu thời gian thực
        heart_rate = random.randint(70, 145) # Mô phỏng nhịp tim sinh lý
        gaze_confidence = round(random.uniform(0.5, 1.0), 2)
        print(f"[Perception] Đang quét dữ liệu: Nhịp tim={heart_rate} BPM | Độ chính xác ánh mắt={gaze_confidence}")
        return {"heart_rate": heart_rate, "gaze_confidence": gaze_confidence}
""",

    "src/agents/kinematic_agent.py": """class KinematicAgent:
    \"\"\"Điều khiển cơ khí, robot tự hành di chuyển và giữ thăng bằng (Series Elastic Actuators - SEA)\"\"\"
    def __init__(self):
        print("[Kinematic] Kết nối phần cứng ROS2 và hệ thống động cơ...")

    def execute_movement(self, state):
        if state == "NORMAL":
            print("[Kinematic] Đang chạy chế độ trợ lực Zero-Gravity nâng đỡ bệnh nhân tập đi.")
        elif state == "SAFE_HOLD":
            print("[Kinematic] 🚨 KÍCH HOẠT CHẾ ĐỘ PHÒNG THỦ: Khóa cứng toàn bộ khớp cơ khí (Lock Joint), ngăn chặn bệnh nhân ngã quỵ!")
""",

    "src/agents/storyteller_agent.py": """class StorytellerAgent:
    \"\"\"Điều phối LLM và tạo môi trường thực tế ảo tăng cường (AR/VR)\"\"\"
    def __init__(self):
        print("[Storyteller] Đang kết nối mô hình ngôn ngữ lớn (LLM Orchestrator)...")

    def adapt_environment(self, mood):
        if mood == "STRESSED":
            print("[Storyteller] Đang chuyển đổi không gian AR sang chế độ thư giãn (Âm thanh dịu nhẹ, phong cảnh thiên nhiên).")
        else:
            print("[Storyteller] Đang hiển thị bài tập phục hồi chức năng dưới dạng trò chơi (Gamification).")
""",

    "src/agents/arbitrator_agent.py": """class ArbitratorAgent:
    \"\"\"Đại lý trọng tài điều phối an toàn hệ thống (Stress Handling & HITL) - Cốt lõi của SOAR\"\"\"
    def __init__(self):
        print("[Arbitrator] Hệ thống lõi giám sát an toàn thời gian thực đang chạy...")

    def evaluate_risk(self, telemetry):
        # Logic xử lý căng thẳng thông minh (Human-in-the-Loop) theo ý kiến của bạn
        if telemetry["heart_rate"] > 140:
            print("[Arbitrator] 🚨 CẢNH BÁO: Phát hiện bệnh nhân hoảng loạn sinh lý (Nhịp tim > 140)!")
            return "TRIGGER_ACTIVE_DELAY"
        elif telemetry["gaze_confidence"] < 0.85:
            print("[Arbitrator] ⚠️ Dữ liệu ý định bị rối hoặc nhiễu. Tiến hành sàng lọc và thử lại.")
            return "RETRY_DATA_FILTER"
        return "PROCEED"
""",

    # 5. File điều phối tổng (Main Execution Loop)
    "src/main_orchestrator.py": """import time
from agents.perception_agent import PerceptionAgent
from agents.kinematic_agent import KinematicAgent
from agents.storyteller_agent import StorytellerAgent
from agents.arbitrator_agent import ArbitratorAgent

def run_aura_loop():
    print("=== KHỞI ĐỘNG HỆ THỐNG MÁY MÓC THỜI GIAN THỰC AURA ===")
    perception = PerceptionAgent()
    kinematic = KinematicAgent()
    storyteller = StorytellerAgent()
    arbitrator = ArbitratorAgent()
    
    print("\\n🛡️ Hệ thống bắt đầu quét vòng lặp 'Sense-Think-Act'...")
    try:
        for i in range(1, 4): # Chạy mô phỏng thử 3 vòng lặp
            print(f"\\n--- VÒNG LẶP THỜI GIAN THỰC THỨ {i} ---")
            # 1. Sense (Quét dữ liệu)
            telemetry = perception.analyze_patient_state()
            
            # 2. Think (Trọng tài phân tích rủi ro an ninh/y tế)
            decision = arbitrator.evaluate_risk(telemetry)
            
            # 3. Act (Hành động cơ khí & Thăng hoa cảm xúc)
            if decision == "TRIGGER_ACTIVE_DELAY":
                kinematic.execute_movement("SAFE_HOLD")
                storyteller.adapt_environment("STRESSED")
                print("[HITL Uplink] Đang kết nối trực tuyến (WebRTC Stream) báo động tới Bác sĩ trực ban...")
            else:
                kinematic.execute_movement("NORMAL")
                storyteller.adapt_environment("NORMAL")
                
            time.sleep(1.5) # Độ trễ chu kỳ hệ thống
            
    except KeyboardInterrupt:
        print("\\nDừng hệ thống an toàn.")

if __name__ == '__main__':
    run_aura_loop()
"""
}

# Tiến hành tạo thư mục và ghi file tự động
for filepath, content in project_structure.items():
    # Tạo thư mục cha nếu chưa tồn tại
    dirname = os.path.dirname(filepath)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)
        print(f"📁 Đã tạo thư mục: {dirname}")
        
    # Ghi nội dung code vào file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"📄 Đã tạo file: {filepath}")

print("\n✅ HOÀN THÀNH: Toàn bộ khung cấu trúc thư mục của dự án AURA đã được dựng xong!")
