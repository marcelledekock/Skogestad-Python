from utils import tf, mimotf, poles, zeros


s = tf([1,0],[1])
T1 = (2*s + 1)/(s**2 + 0.8*s + 1)
T2 = (-2*s + 1)/(s**2 + 0.8*s + 1)

S1 = 1 - T1
S2 = 1 - T2

print("S1 contains RHP zero %.2f, therefore L1 contains a RHP pole at %.2f" %(S1.zeros()[0],S1.zeros()[0]))
print("T2 contains RHP zero %.2f, therefore L2 contains the same RHP zero %.2f" %(T2.zeros(),T2.zeros()))
