class ArbitratorAgent:
    """Đại lý trọng tài điều phối an toàn hệ thống (Stress Handling & HITL) - Cốt lõi của SOAR"""
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
