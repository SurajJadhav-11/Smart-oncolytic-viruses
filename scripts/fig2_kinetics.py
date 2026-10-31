"""
Figure 2: MMP-2/9 cleavage kinetics, time-dependent selectivity and kcat/Km sensitivity.

PARAMETERS (see Table 2 of the manuscript)
  kcat/Km = 6.5e5 M^-1 s^-1  : mean of the MMP-2 (6.9e5) and MMP-9 (6.2e5) values reported by the
                               manufacturer (Enzo, BML-P276) for Mca-Lys-PLGL-Dpa-Ala-Arg-NH2
  Km      = 30 uM            : reported lower bound (">30 uM"); with [S]0 = 1 uM << Km only kcat/Km matters
  kcat    = kcat/Km * Km = 19.5 s^-1 (derived)
  [S]0    = 1 uM (model assumption);  [E]_TME = 50 nM and [E]_healthy = 0.42 nM are ASSUMED scenarios
"""
import os
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.integrate import solve_ivp

OUT_DIR = "."                           # figures are saved in the folder you run the script from
os.makedirs(OUT_DIR, exist_ok=True)

KM, S0 = 30e-6, 1.0e-6                  # M
KCM0 = 6.5e5                            # M^-1 s^-1
E_T, E_H = 50e-9, 0.42e-9               # M
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8})

def frac(E, kcm, times):
    kcat = kcm * KM
    f = lambda t, y: [-kcat*E*y[0]/(KM+y[0]), kcat*E*y[0]/(KM+y[0])]
    s = solve_ivp(f, [0, max(times)], [S0, 0], t_eval=times, method="LSODA", rtol=1e-10, atol=1e-17)
    return s.y[1]/S0*100

t = np.logspace(-1, np.log10(7200), 500)
pT, pH = frac(E_T, KCM0, t), frac(E_H, KCM0, t)

fig = plt.figure(figsize=(7.2, 6.6))
gs = GridSpec(2, 2, figure=fig, height_ratios=[1, 1.05], hspace=0.38, wspace=0.42)

a = fig.add_subplot(gs[0, 0])
a.plot(t, pT, color="#d95f02", lw=2, label="TME (50 nM)")
a.plot(t, pH, color="#7570b3", lw=2, ls="--", label="Healthy (0.42 nM)")
a.axhline(50, color="gray", ls=":", lw=0.8)
a.set_xscale("log"); a.set_xlabel("Time (s)"); a.set_ylabel("Precursor cleaved (%)")
a.set_title("A", loc="left", fontweight="bold"); a.legend(fontsize=7, loc="upper left", framealpha=0.95); a.grid(alpha=.3)

b = fig.add_subplot(gs[0, 1])
ratio = pT/np.maximum(pH, 1e-12)
l1, = b.plot(t, ratio, color="#1b9e77", lw=2, label="Fold ratio")
b.axhline(119.05, color="k", ls=":", lw=0.8)
b.set_ylim(0.9, 400); b.text(0.12, 150, "119 = 50/0.42 (t \u2192 0)", fontsize=7)
b.set_xscale("log"); b.set_yscale("log"); b.set_xlabel("Time (s)"); b.set_ylabel("Fold discrimination")
b2 = b.twinx(); l2, = b2.plot(t, pT-pH, color="#e7298a", lw=2, ls="-.", label="Gap (pts)")
b2.set_ylabel("Absolute gap (% points)")
b.legend([l1, l2], [l1.get_label(), l2.get_label()], fontsize=7, loc="center left", framealpha=0.95)
b.set_title("B", loc="left", fontweight="bold"); b.grid(alpha=.3)

kcms = np.logspace(3, 7, 31); tt = np.logspace(0, np.log10(7200), 31)
G = np.zeros((len(tt), len(kcms)))
for j, k in enumerate(kcms):
    G[:, j] = frac(E_T, k, tt) - frac(E_H, k, tt)
c = fig.add_subplot(gs[1, :])
im = c.pcolormesh(kcms, tt, G, shading="auto", cmap="viridis", vmin=0, vmax=100)
c.axvline(KCM0, color="white", ls="--", lw=1.4)
c.text(KCM0*0.85, 1.6, "baseline kcat/Km\n6.5\u00d710\u2075 M\u207b\u00b9s\u207b\u00b9", color="white", fontsize=7, ha="right")
c.contour(kcms, tt, G, levels=[50], colors="red", linewidths=1.3)
c.set_xscale("log"); c.set_yscale("log")
c.set_xlabel("kcat/Km (M\u207b\u00b9s\u207b\u00b9)"); c.set_ylabel("Time (s)")
c.set_title("C", loc="left", fontweight="bold")
fig.colorbar(im, ax=c, label="TME \u2212 healthy gap (% points)", pad=0.02)
fig.savefig(os.path.join(OUT_DIR, "Figure2_kinetics_400dpi.png"), dpi=400, bbox_inches="tight")
fig.savefig(os.path.join(OUT_DIR, "Figure2_kinetics_600dpi.png"), dpi=600, bbox_inches="tight")
print("Saved Figure2_kinetics_400dpi.png and Figure2_kinetics_600dpi.png in:", os.path.abspath(OUT_DIR))

# numbers quoted in the manuscript (baseline)
for tm in (30, 120):
    print(f"t={tm}s  TME {np.interp(tm,t,pT):.2f}%  healthy {np.interp(tm,t,pH):.2f}%")
g = pT - pH
print(f"peak gap {g.max():.1f} points at {t[g.argmax()]:.0f} s")
