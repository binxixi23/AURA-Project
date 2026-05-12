# Safety Protocols & Fall Prevention Logic

The AURA system prioritizes "Zero-Harm" through a multi-layered safety architecture.

### 1. Active Stability Control (ASC)
- **IMU Integration:** Dual 6-axis Gyroscopes monitor the patient's center of mass 200 times per second.
- **Predictive Braking:** If the system detects a tilt angle exceeding 15 degrees, electromagnetic brakes lock the wheels instantly to provide a rigid support frame.

### 2. Compliant Interaction
- **Impedance Control:** The robot does not follow a rigid path. It behaves like a spring. If a patient stumbles, the robot "yields" and then gently guides them back to a stable position.
- **Force Limiting:** Every motor has a hardware-level torque limit to ensure it never applies more force than a human limb can safely handle.

### 3. Emergency "Hug" Protocol
- In the event of a total loss of balance, the AURA arms (supports) transition into a "Lock-and-Cradle" mode, using the bio-inspired eSkin to grip the patient securely while lowering the center of gravity.
