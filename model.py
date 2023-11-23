def demand(a, b, e, p, tau):
    return a - b*p + tau*e

def profit(a, b, c, e, h, p, w, tau, v=0, phi=0):
    return ((1-v)*w - c) * demand(a, b, e, p, tau) - (1-phi) * h*e**2

## Centralized model
e_c_star = tau * (a - b*c) / (4*b*h - tau**2)
p_c_star = (2*a*h + 2*b*c*h - c*tau**2) / (4*b*h - tau**2)
D_c_star = demand(a, b, e_c_star, p_c_star, tau)

# profit for m
Pi_m_c_star = profit(a, b, c, e_c_star, h, p_c_star, w, tau)
# profit for r
Pi_r_c_star = profit(a, b, w, e_c_star, 0, p_c_star, p_c_star, tau)
# profit for sc
Pi_sc_c_star = profit(a, b, c, e_c_star, h, p_c_star, p_c_star, tau)

## Decentralized model
e_d_star = tau * (w - c) / (2*h)
p_d_star = (2*h * (a + b*w) + (w - c)*tau**2) / (4*b*h)
D_d_star = demand(a, b, e_d_star, p_d_star, tau)

# profit for m
Pi_m_c_star = profit(a, b, c, e_d_star, h, p_d_star, w, tau)
# profit for r
Pi_r_c_star = profit(a, b, w, e_d_star, 0, p_d_star, p_d_star, tau)
# profit for sc
Pi_sc_d_star = Pi_m_d_star + Pi_r_d_star


## Hybrid greening cost and revenue sharing contract
def find_v(a, b, e_c_star, p_c_star, e_d_star, p_d_star, tau, w, phi):
    # v_ub = ((p_c_star-c)*demand(a, b, e_c_star, p_c_star, tau) - (w-c)*demand(a, b, e_d_star, p_d_star, tau)) / (p_c_star*demand(a, b, e_c_star, p_c_star, tau))
    v_ub = (profit(a, b, c - wr, e_c_star, h, p_c_star, p_c_star, tau, 0, phi) - profit(a, b, c, e_d_star, h, p_d_star, w, tau)) / (p_c_star*demand(a, b, e_c_star, p_c_star, tau))
    v_lb = (profit(a, b, w, e_d_star, h, p_d_star, p_d_star, tau, 0, 1) + profit(a, b, 0, e_c_star, h, p_c_star, wr, tau, 0, 1-phi)) / (p_c_star*demand(a, b, e_c_star, p_c_star, tau))
    return [v_lb, v_ub]

e_HGRS_star = tau * (2*b*v*(wr - c) + (1-v)*(v*a + wr*b)) / (4*b*h*v*(1-phi) - tau**2*v*(1-v))
p_HGRS_star = (tau**2*v*(wr - c) + 2*h*(1-phi)*(v*a + wr*b)) / (4*b*h*v*(1-phi) - tau**2*v*(1-v))
D_HGRS_star = demand(a, b, e_HGRS_star, p_HGRS_star, tau)

# # profit for m
# Pi_m_d_star = profit(a, b, c - wr, e_d_star, h, w, tau, v, phi)
# # profit for r
# Pi_r_d_star = profit(a, b, wr, e_d_star, 0, p_d_star, tau, 1 - v, 1 - phi)
# # profit for sc
# Pi_sc_d_star = Pi_m_d_star + Pi_r_d_star