---
title: "Crystal Plasticity 101"
collection: teaching
type: "Tutorials"
permalink: /teaching/2024-fall-teaching-4
excerpt: ""
venue: "written by Prof. Zhang"
date: 2024-10-16
location: "Beijing, China"
---
## Rate Dependent Crystal Plasticity Model

A cyclic CP model is developed to represent the elastic-viscoplastic behavior of crystal grains under cyclic loading. The model extends the CP framework of Asaro and Needleman (Asaro and Needleman, 1985) and Kalidindi et al. (Kalidindi et al., 1992) to account for nonlinear kinematic hardening at the slip system level, akin to the J2 kinematic hardening model by Chaboche (Chaboche, 1986). Despite the viscoplastic formulation used, the strain rate sensitivity is small for the coarse-grained stainless steel studied in this work. Consequently, the simulated cyclic viscoplastic response approaches its rate-independent counterpart from the cyclic J2 model. 

In the continuum mechanics framework for finite deformation, the deformation gradient tensor F can be decomposed into its elastic ${{\mathbf{F}}^{\text{e}}}$ and plastic ${{\mathbf{F}}^{\text{p}}}$ parts such that $\mathbf{F}={{\mathbf{F}}^{\text{e}}}{{\mathbf{F}}^{\text{p}}}$. The rate of plastic deformation gradient is given by 

${{\mathbf{\dot{F}}}^{\text{p}}}={{\mathbf{L}}^{\text{p}}}{{\mathbf{F}}^{\text{p}}}$	(1)

The plastic velocity gradient ${{\mathbf{L}}^{\text{p}}}$ is 

${{\mathbf{L}}^{\text{p}}}=\sum\limits_{\alpha }{{{{\dot{\gamma }}}^{\alpha }}\mathbf{S}_{0}^{\alpha }}$	(2)

where $\mathbf{S}_{0}^{\alpha }=\mathbf{m}_{0}^{\alpha }\otimes \mathbf{n}_{0}^{\alpha }$, with $\mathbf{m}_{0}^{\alpha }$ and $\mathbf{n}_{0}^{\alpha }$ being the unit vectors corresponding the slip direction and slip plane normal direction of slip system α in the reference configuration, respectively, and ${{\dot{\gamma }}^{\alpha }}$ is the plastic shearing rate on slip system α. Each fcc grain consists of 12 {111}<110> slip systems.

The applied resolved shear stress (RSS) acting on slip system α is expressed as 

${{\tau }^{\alpha }}=({{\mathbf{C}}^{\text{e}}}{{\mathbf{T}}^{\text{PK-}2}}):\mathbf{S}_{0}^{\alpha }$	(3)

In Eq. (3), \\[{{\mathbf{C}}^{\text{e}}}={{\mathbf{F}}^{{{\text{e}}^{\text{T}}}}}{{\mathbf{F}}^{\text{e}}}\\] is the right Cauchy-Green tensor. The elastic strain tensor is defined as,
 \\[{{\mathbf{E}}^{\text{e}}}=\frac{1}{2}\left( {{\mathbf{F}}^{{{\text{e}}^{\text{T}}}}}{{\mathbf{F}}^{\text{e}}}-\mathbf{I} \right)\\]	(4)
The second Piola-Kirchhoff stress tensor can be calculated from elastic stiffness tensor and elastic strain,
${{\mathbf{T}}^{\text{PK-}2}}=\mathbf{C}:{{\mathbf{E}}^{\text{e}}}$	(5)
The 2nd PK stress relates to the Cauchy stress σ through elastic deformation tensor,
${{\mathbf{T}}^{\text{PK-}2}}={{\mathbf{F}}^{{{\text{e}}^{-1}}}}\left\{ (\text{det}{{\mathbf{F}}^{\text{e}}})\sigma  \right\}{{\mathbf{F}}^{{{\text{e}}^{-\text{T}}}}}$	(6)
$\mathbf{\sigma }=\frac{1}{\text{det}{{\mathbf{F}}^{\text{e}}}}{{\mathbf{F}}^{\text{e}}}{{\mathbf{T}}^{\text{PK-}2}}{{\mathbf{F}}^{{{\text{e}}^{\text{T}}}}}$	(7)
Noted that this Cauchy stress is defined in the laboratory basis of the current configuration. The Abaqus VUMAT actually need the Cauchy stress defined in the corational basis.
$\mathbf{\sigma }={{\mathbf{R}}^{\text{T}}}\mathbf{\sigma R}$	(8)

where R comes from the RU decomposition of the total deformation gradient F. 
The elastic stretch is usually infinitesimal for metallic materials, so that ${{\tau }^{\alpha }}\approx {{\mathbf{T}}^{\text{PK-}2}}:\mathbf{S}_{0}^{\alpha }$ (Kalidindi et al., 1992).
Two resolved back stress components are introduced to account for kinematic hardening at the slip system level. The rate of the resolved back stress is  
\\[\dot{B}_{i}^{\alpha }={{\tilde{C}}_{i}}{{\dot{\gamma }}^{\alpha }}-{{\tilde{D}}_{i}}B_{i}^{\alpha }\left| {{{\dot{\gamma }}}^{\alpha }} \right|,\begin{matrix}
   {} & {}  \\
\end{matrix}i=1,\text{ }2\\]	(9)

where \\[B_{i}^{\alpha }\\] is the i-th component of the resolved back stress on slip system α , and \\[{{\tilde{C}}_{i}}\\] and \\[{{\tilde{D}}_{i}}\\] are the material parameters. While Eq. (9) is sufficient to capture the cyclic plastic strain response of stainless steel,  Hennessey et al. (Hennessey et al., 2017) showed that for 7075-T6 Al it was necessary to employ a nonlinear dynamic recovery term as opposed to the linear one in Eq. (10) to accurately represent the cyclic plastic strain response. The effective RSS on slip system α is 
$\tau _{\text{eff}}^{\alpha }={{\tau }^{\alpha }}-\sum\limits_{i}{B_{i}^{\alpha }}$	(10)

The plastic shearing rate ${{\dot{\gamma }}^{\alpha }}$ on slip system α is

${{\dot{\gamma }}^{\alpha }}={{\dot{\gamma }}_{\text{0}}}{{\left| \frac{\tau _{\text{eff}}^{\alpha }}{{{s}^{\alpha }}} \right|}^{\frac{1}{m}}}\sgn (\tau _{\text{eff}}^{\alpha })$	(11)

where ${{\dot{\gamma }}^{\alpha }}$ is the reference shearing rate, m is the slip rate sensitivity, and ${{s}^{\alpha }}$ is the non-directional slip resistance on slip system α. The slip resistance ${{s}^{\alpha }}$, with an initial value $s_{0}^{\alpha }$, evolves according to

${{\dot{s}}^{\alpha }}=\sum\limits_{\beta }{{{h}^{\alpha \beta }}}\left| {{{\dot{\gamma }}}^{\alpha }} \right|$	(12)

The matrix of the strain hardening rate is 

${{\left[ {{h}^{\alpha \beta }} \right]}_{12\times 12}}=\left\{ \begin{matrix}
{{h}^{\beta }}\begin{matrix}
{} & {} & \text{ if }\alpha =\beta   \\
\end{matrix}  \\
q{{h}^{\beta }}\begin{matrix}
{} & {} & \text{if }\alpha \ne \beta   \\
\end{matrix}  \\
\end{matrix} \right.$	(13)

where q is the latent hardening coefficient taken as 1.4 (Asaro and Needleman, 1985). Some literature also use 1.0 for coplanar slip system and 1.4 for non-coplanar systems. 
${{h}^{\beta }}$ is the single slip hardening rate, which is taken as (Kalidindi et al., 1992)  
${{h}^{\beta }}={{h}_{0}}{{\left\{ 1-\frac{{{s}^{\beta }}}{{{s}_{\text{sat}}}} \right\}}^{{{a}_{0}}}}$	(14)

where ${{h}_{0}}$ is the initial hardening rate, ${{a}_{0}}$ is the hardening exponent and ${{s}_{\text{sat}}}$ is the saturated non-directional slip resistance. These hardening parameters are taken to be identical for all 12 {111}<101> slip systems. The CP model is implemented by writing an Abaqus/Explicit user subroutine VUMAT (ABAQUS/Explicit, 2009).

### Reference
Asaro, R.J., Needleman, A., 1985. Overview no. 42 texture development and strain hardening in rate dependent polycrystals. Acta Metall. 33, 923–953.
Kalidindi, S.R., Bronkhorst, C.A., Anand, L., 1992. Crystallographic texture evolution in bulk deformation processing of FCC metals. J. Mech. Phys. Solids 40, 537–569.
Chaboche, J.-L., 1986. Time-independent constitutive theories for cyclic plasticity. Int. J. Plast. 2, 149–188.
