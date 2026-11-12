# Aluno: Victor Alves Freire De Queiroz
# Matrícula: 202307122

import numpy as np
import control as ct
import matplotlib.pyplot as plt

s = ct.tf('s')
G = 20 / ((s + 2) * (s + 8))
H = 1

# sem compensação
mf0 = ct.feedback(G, H)
polos0 = ct.poles(mf0)
sigma = -polos0[0].real
wd = abs(polos0[0].imag)
print("Polos sem compensação:", np.round(polos0, 4))
print(f"sigma = {sigma:.4f}  wd = {wd:.4f}")
print(f"Ts teórico = {4/sigma:.4f} s  Tp teórico = {np.pi/wd:.4f} s")

# novo Ts 4x maior, mantendo wd
sigma_novo = sigma / 4
a1 = 2 * sigma_novo
a0 = sigma_novo**2 + wd**2
print(f"\nEq. desejada: s^2 + {a1:.4f}s + {a0:.4f} = 0")

# zero cancela o polo em -8
T = 1 / 8
alfa = 8 / (a1 - 2)
K = (a0 * alfa - 16) / 20

print(f"\nK    = {K:.4f}")
print(f"alfa = {alfa:.4f}")
print(f"T    = {T:.4f}")

C = K * (1 + s*T) / (1 + s*alfa*T)
print(f"\nC(s) = {K/alfa:.4f} (s + {1/T:.0f}) / (s + {1/(alfa*T):.4f})")

mf = ct.feedback(C * G, H)
print("Polos com compensação:", np.round(ct.poles(mf), 4))

t = np.linspace(0, 8, 8000)
t0, y0 = ct.step_response(mf0, t)
t1, y1 = ct.step_response(mf, t)

info0 = ct.step_info(mf0, T=t, SettlingTimeThreshold=0.02)
info1 = ct.step_info(mf, T=t, SettlingTimeThreshold=0.02)

print("\nSem compensação (C=1):")
print(f"  Mp = {info0['Overshoot']:.2f} %")
print(f"  Ts = {info0['SettlingTime']:.4f} s")
print(f"  Tp = {info0['PeakTime']:.4f} s")
print(f"  y(inf) = {info0['SteadyStateValue']:.4f}")

print("\nCom compensador atraso:")
print(f"  Mp = {info1['Overshoot']:.2f} %")
print(f"  Ts = {info1['SettlingTime']:.4f} s")
print(f"  Tp = {info1['PeakTime']:.4f} s")
print(f"  y(inf) = {info1['SteadyStateValue']:.4f}")

print(f"\nRazão Ts: {info1['SettlingTime']/info0['SettlingTime']:.2f}x")

plt.figure(figsize=(9, 5))
plt.plot(t0, y0, label='Sem compensação (C=1)')
plt.plot(t1, y1, label='Com compensador atraso')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.title('Resposta ao degrau unitário')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('resposta_degrau.png', dpi=120)
plt.show()
