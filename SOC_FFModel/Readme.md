# Self-Organized Criticality and the Forest Fire Model 

https://github.com/user-attachments/assets/a4a38b08-b5c6-4e36-bb1d-ee2c33939350

Here, I have implemented the Bak–Chen–Tang forest fire model as a cellular automaton to study self-organized criticality (SOC) in a driven dissipative system.

The simulations were performed in both 2D and 3D using periodic boundary conditions. The model exhibits intermittent avalanche-like dynamics, power-law behavior, and fractal fire structures characteristic of SOC systems.

---

## Results

Spatial fire distributions exhibit approximate power-law scaling over intermediate distances. The extracted fractal dimensions are consistent with scale-invariant clustering:

- **2D:** $D_f \approx{} 1.21$  
- **3D:** $D_f \approx{} 2.35$

---

## References

Bak, P., Tang, C., & Wiesenfeld, K. (1987).  
*Self-Organized Criticality: An Explanation of the 1/f Noise.*  
Physical Review Letters, 59, 381.

Bak, P., Chen, K., & Tang, C. (1990).  
*A forest-fire model and some thoughts on turbulence.*  
Physics Letters A, 147, 297–300.

---

## Usage

Run the simulation script 2DFF_Model_ani.py to get the simulation of the 2D Forest fire model. You can also save snapshots of the desired time interval from the simulation. 

The Jupyter notebook, powerlaw_plots.ipynb, is used to simulate the power law dependence of the SOC and also calculates the fractal dissipation.
