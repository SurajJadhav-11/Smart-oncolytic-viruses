"""
Figure 4: coupled MMP cleavage + first-order hepatic clearance (single well-mixed compartment).

States (% of the injected, initially intact dose; molar units with [Vi]0 = [S]0 = 1 uM):
  Vi circulating intact | Vu circulating unlocked | Ci liver-cleared intact | Cu liver-cleared UNLOCKED
Mass is conserved: Vi + Vu + Ci + Cu = S0.

PARAMETERS (see Table 2 of the manuscript)
  kcat/Km = 6.5e5 M^-1 s^-1 (manufacturer-reported MMP-2/9 values on a PLGL fluorogenic peptide), Km = 30 uM,
  kcat = 19.5 s^-1 (derived); [E]_blood = 0.42 nM and [E]_TME = 50 nM are ASSUMED;
  t1/2,circ = 2 min (Alemany et al. 2000 report < 2 min in mice); sensitivity: 1 and 5 min.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.integrate import solve_ivp

OUT_DIR = "."                               # figures are saved in the folder you run the script from
os.makedirs(OUT_DIR, exist_ok=True)

KM, S0 = 30e-6, 1.0e-6
KCM = 6.5e5
KCAT = KCM * KM
E_BLOOD, E_TME = 0.42e-9, 50e-9
T_HALF_CIRC = 120.0                         # s

def kclear(t_half): return np.log(2) / t_half

def simulate(E, k_cl, T, n=4001):
    def rhs(t, y):
        Vi, Vu = max(y[0], 0.0), max(y[1], 0.0)
        r = KCAT * E * Vi / (KM + Vi)
        return [-r - k_cl*Vi, r - k_cl*Vu, k_cl*Vi, k_cl*Vu]
    t = np.linspace(0, T, n)
    s = solve_ivp(rhs, [0, T], [S0, 0, 0, 0], t_eval=t, method="Radau", rtol=1e-11, atol=1e-18)
    return s.t, s.y / S0 * 100

t_b, Yb = simulate(E_BLOOD, kclear(T_HALF_CIRC), 900)         # 15 min in blood
t_long, Yl = simulate(E_BLOOD, kclear(T_HALF_CIRC), 7200)     # final fate of the dose
t_t, Yt = simulate(E_TME, 0.0, 300, 30001)                    # tumour stroma, no clearance
i120 = np.argmin(abs(t_t - 120))

E_grid = np.logspace(-12, np.log10(3e-9), 31)                 # 1 pM .. 3 nM
HALF = (60, 120, 300)
leak = {th: [simulate(E, kclear(th), 7200, 600)[1][3, -1] for E in E_grid] for th in HALF}

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8})
fig = plt.figure(figsize=(7.2, 6.6))
gs = GridSpec(2, 2, figure=fig, hspace=0.38, wspace=0.32)

a = fig.add_subplot(gs[0, 0]); tm = t_b / 60
a.plot(tm, Yb[0], color="#1f77b4", lw=2, label="Circulating, intact")
a.plot(tm, Yb[1], color="#d62728", lw=2, ls="--", label="Circulating, unlocked")
a.plot(tm, Yb[2], color="#2ca02c", lw=2, ls="-.", label="Liver-cleared, intact (cum.)")
a.plot(tm, Yb[3], color="#ff7f0e", lw=2, ls=":",  label="Liver-cleared, unlocked (cum.)")
a.set_xlabel("Time in circulation (min)"); a.set_ylabel("% of injected dose")
a.set_title("A", loc="left", fontweight="bold"); a.legend(fontsize=6.5, loc="center right"); a.grid(alpha=.3)

b = fig.add_subplot(gs[0, 1])
labels = ["Blood / liver\n(final fate)", "Tumor stroma\n(2 min, no clearance)"]
intact = [Yl[2, -1] + Yl[0, -1], Yt[0, i120]]
unlocked = [Yl[3, -1] + Yl[1, -1], Yt[1, i120]]
b.bar(labels, intact, color="#1f77b4", width=0.5, label="Intact (shielded)")
b.bar(labels, unlocked, bottom=intact, color="#d62728", width=0.5, label="Unlocked")
for x, (i_, u_) in enumerate(zip(intact, unlocked)):
    if i_ > 6: b.text(x, i_/2, f"{i_:.1f}%", ha="center", va="center", color="white", fontweight="bold")
    else: b.text(x, i_ + 3, f"intact {i_:.1f}%", ha="center", va="bottom", color="black", fontsize=7)
    if u_ > 6: b.text(x, i_ + u_/2, f"{u_:.1f}%", ha="center", va="center", color="white", fontweight="bold")
    else: b.text(x, i_ + u_ + 2, f"unlocked {u_:.1f}%", ha="center", va="bottom", color="black", fontsize=7)
b.set_ylim(0, 118); b.set_ylabel("% of dose"); b.grid(alpha=.3, axis="y"); b.legend(fontsize=6.5, loc="upper right", ncol=2)
b.set_title("B", loc="left", fontweight="bold")

c = fig.add_subplot(gs[1, :])
for th, col in zip(HALF, ("#9467bd", "#d62728", "#2ca02c")):
    c.plot(E_grid*1e12, leak[th], color=col, lw=2, label=f"t\u00bd,circ = {th//60:g} min")
c.axhline(5, color="gray", ls=":", lw=1); c.text(1.2, 6.0, "5% leakage", fontsize=7, color="gray")
c.axvline(0.42e3, color="k", ls="--", lw=1); c.text(0.42e3*1.08, 36, "assumed 0.42 nM", fontsize=7)
c.set_xscale("log"); c.set_xlabel("Active MMP-2/9 in blood (pM)")
c.set_ylabel("% of dose reaching liver unlocked")
c.set_title("C", loc="left", fontweight="bold")
c.legend(fontsize=7, loc="upper left"); c.grid(alpha=.3)

fig.savefig(os.path.join(OUT_DIR, "Figure4_pkpd_400dpi.png"), dpi=400, bbox_inches="tight")
fig.savefig(os.path.join(OUT_DIR, "Figure4_pkpd_600dpi.png"), dpi=600, bbox_inches="tight")
print("Saved Figure4_pkpd_400dpi.png and Figure4_pkpd_600dpi.png in:", os.path.abspath(OUT_DIR))

print("Mass balance error:", abs(Yb[:, -1].sum() - 100))
for m in (2, 5, 10, 15):
    k = np.argmin(abs(t_b - m*60))
    print(f"{m:2d} min | circ intact {Yb[0,k]:5.1f} | circ unlocked {Yb[1,k]:5.1f} | cleared intact {Yb[2,k]:5.1f} | cleared unlocked {Yb[3,k]:5.1f}")
print(f"Peak circulating unlocked: {Yb[1].max():.2f}% at {t_b[Yb[1].argmax()]/60:.3f} min")
print(f"Final: liver intact {Yl[2,-1]:.2f}% | liver UNLOCKED {Yl[3,-1]:.2f}%")
print(f"TME at 2 min: unlocked {Yt[1,i120]:.1f}%")

# Show the figure inline when run in Colab / Jupyter (does nothing in a plain Python run)
try:
    from IPython import get_ipython
    if get_ipython() is not None:
        from IPython.display import display, Image
        display(Image(filename=os.path.join(OUT_DIR, "Figure4_pkpd_400dpi.png")))
except ImportError:
    pass
