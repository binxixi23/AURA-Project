class StorytellerAgent:
    """Điều phối LLM và tạo môi trường thực tế ảo tăng cường (AR/VR)"""
    def __init__(self):
        print("[Storyteller] Đang kết nối mô hình ngôn ngữ lớn (LLM Orchestrator)...")

    def adapt_environment(self, mood):
        if mood == "STRESSED":
            print("[Storyteller] Đang chuyển đổi không gian AR sang chế độ thư giãn (Âm thanh dịu nhẹ, phong cảnh thiên nhiên).")
        else:
            print("[Storyteller] Đang hiển thị bài tập phục hồi chức năng dưới dạng trò chơi (Gamification).")
