import time

class AuraAgent:
    def __init__(self, name):
        self.name = name
    def log(self, message):
        print(f"[{self.name}] {message}")

class PerceptionAgent(AuraAgent):
    def get_patient_intent(self):
        return "SPEED_UP_GESTURE"

class BiometricAgent(AuraAgent):
    def get_vitals(self):
        return {"heart_rate": 145, "muscle_fatigue": 0.85}

class KinematicAgent(AuraAgent):
    def apply_support(self, level):
        self.log(f"Adjusting physical support to {level*100}% of body weight.")
    def set_speed(self, speed):
        self.log(f"Setting walking speed to {speed} m/s.")

class StorytellerAgent(AuraAgent):
    def play_reassurance(self, context):
        self.log(f"STORYTELLER INTERVENTION: '{context}'")

class AuraOrchestrator:
    def __init__(self):
        self.perception = PerceptionAgent("PERCEPTION")
        self.biometrics = BiometricAgent("BIOMETRICS")
        self.kinematics = KinematicAgent("KINEMATICS")
        self.storyteller = StorytellerAgent("STORYTELLER")

    def run_cycle(self):
        print("--- AURA SIMULATION START ---")
        intent = self.perception.get_patient_intent()
        vitals = self.biometrics.get_vitals()
        
        print(f"[INPUT] Patient Intent: {intent} | HR: {vitals['heart_rate']} | Fatigue: {vitals['muscle_fatigue']*100}%")
        
        # Core Orchestration Logic (Simulating LLM Decision)
        if intent == "SPEED_UP_GESTURE" and vitals['muscle_fatigue'] > 0.70:
            print("[ORCHESTRATOR] Conflict: Patient is ambitious but physically exhausted.")
            print("[ORCHESTRATOR] Safety Override: Enforcing recovery mode.")
            
            self.kinematics.apply_support(0.40) # Boost physical support
            self.kinematics.set_speed(0.5)      # Safe recovery speed
            self.storyteller.play_reassurance("You've reached the summit of today's path. Let's pause and admire the view.")
        
        print("--- AURA SIMULATION SUCCESSFUL ---")

# Execute
aura = AuraOrchestrator()
aura.run_cycle()
