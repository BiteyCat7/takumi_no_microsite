import matplotlib.pyplot as plt

risks = {
    "Brand Dilution": (0.3, 0.3),
    "Consumer Rejection": (0.6, 0.6),
    "Quality Consistency": (0.7, 0.8),
    "Price Sensitivity": (0.8, 0.95)
}

fig, ax = plt.subplots(figsize=(12, 9))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

ax.set_xlabel('Likelihood (Low → High)', fontsize=12)
ax.set_ylabel('Impact (Low → High)', fontsize=12)

ax.axhline(0.5, color='black', linewidth=1)
ax.axvline(0.5, color='black', linewidth=1)

ax.text(0.25, 0.75, "High Impact, Low Likelihood", fontsize=10, ha='center', bbox=dict(facecolor='yellow', alpha=0.5))
ax.text(0.75, 0.75, "High Impact, High Likelihood", fontsize=10, ha='center', bbox=dict(facecolor='yellow', alpha=0.5))
ax.text(0.25, 0.25, "Low Impact, Low Likelihood", fontsize=10, ha='center', bbox=dict(facecolor='yellow', alpha=0.5))
ax.text(0.75, 0.25, "Low Impact, High Likelihood", fontsize=10, ha='center', bbox=dict(facecolor='yellow', alpha=0.5))

for risk, (x, y) in risks.items():
    ax.plot(x, y, 'o', markersize=10, label=risk)
    ax.text(x + 0.02, y, f" {risk}", fontsize=12, verticalalignment='center')

ax.legend(loc='upper left', fontsize=9, title="Risks")

ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

plt.title('Risk Assessment Matrix', fontsize=14)

plt.savefig('risk_heatmap.png')

plt.show()
