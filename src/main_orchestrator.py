import time
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
    
    print("\n🛡️ Hệ thống bắt đầu quét vòng lặp 'Sense-Think-Act'...")
    try:
        for i in range(1, 4): # Chạy mô phỏng thử 3 vòng lặp
            print(f"\n--- VÒNG LẶP THỜI GIAN THỰC THỨ {i} ---")
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
        print("\nDừng hệ thống an toàn.")

if __name__ == '__main__':
    run_aura_loop()
