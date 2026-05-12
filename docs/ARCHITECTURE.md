# System Architecture & Multi-Agent Coordination

### 1. The Orchestrator (The Brain)
- **Engine:** Large Language Model (LLM) - Llama-3-70B or GPT-4o.
- **Logic:** Interprets multi-modal inputs (vision + force) to select the appropriate "Skill Profile."
- **Communication:** ROS 2 (Robot Operating System) Pub/Sub architecture.

### 2. Decision Flow
- **Input Layer:** Camera (Sign Language), LiDAR (Path), EMG (Muscle intent).
- **Processing Layer:** Logic Agents evaluate "Patient Distress Level" vs. "Physical Stability."
- **Action Layer:** Motor torque adjustment + Audio-Visual output + Haptic feedback.

### 3. Block Diagram (Mermaid)

graph TB
    subgraph Input_Layer ["Sensing & Perception (The Senses)"]
        A[Vision: 3D Camera/LiDAR] --> |Sign Language/Obstacles| P_Agent(Perception Agent)
        B[Tactile: eSkin/Force Sensors] --> |Pain/Grip Intensity| T_Agent(Tactile Agent)
        C[Biometric: EMG/IMU] --> |Muscle Intent/Balance| K_Agent(Kinematic Agent)
    end

    subgraph Core_Brain ["Cognitive Orchestrator (The Mind)"]
        D{LLM Orchestrator: GPT-4o / Llama-3}
        E[(Patient Memory: History & Mood)] <--> D
        
        P_Agent --> D
        T_Agent --> D
        K_Agent --> D
    end

    subgraph Output_Layer ["Execution & Feedback (The Action)"]
        D --> F(Action Agent: Soft-Robotic Actuators)
        D --> G(Storyteller Agent: AR/VR & Narrative)
        D --> H(Haptic Agent: Music & Rhythm Vibration)
        D --> I(IoT Hub: Smart Home Control)
    end

    subgraph Safety_Loop ["Real-Time Safety Guard"]
        K_Agent -.-> |Emergency Override| F
        F --> |Active Balancing| J[Patient Stability]
    end

    style D fill:#f96,stroke:#333,stroke-width:4px
    style Core_Brain fill:#fff5e6,stroke:#f96
    style Safety_Loop fill:#ffe6e6,stroke:#ff0000,stroke-dasharray: 5 5


