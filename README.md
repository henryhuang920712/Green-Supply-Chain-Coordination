# Green Supply Chain Coordination Approach

 <!-- A green supply chain coordination approach of balancing price and green quality in presence of consumer environmental awareness. -->

<details open="open">
<summary><b>Table of Contents</b></summary>

1. [Introduction](#introduction)
2. [The Model](#the-model)
   - [Model Description](#model-Description)
   - [Model Formulations and Solution](#model-formulations-and-solution)
     - [Centralised model](#centralised-model)
     - [Decentralised model](#centralised-model)
     - [Hybrid greening cost and revenue sharing contract](#hybrid-greening-cost-and-revenue-sharing-contract)
3. [Numerical Analyses](#numerical-analyses)
4. [Conclusion](#conclusion)

</details>

# Introduction

This repository serves as a tutorial for implementing the Green Supply Chain Coordination Approach, inspired by the concepts outlined in the paper "Balancing price and green quality in the presence of consumer environmental awareness: a green supply chain coordination approach" authored by Jafar Heydari, Kannan Govindan & Zahra Basiri (2021). We developed this tutorial as a hands-on application for the course "Operations Research Applications and Implementation" instructed by Professor Chia-Yen Lee.

# The Model

In the proposed model, various assumptions are taken into account. Some assumptions enhance the model's realism, while others are employed for simplification. To establish a sound mathematical model, it is assumed that:

- **Single Period Setting:** The channel operates within a single period, indicating that transactions and interactions occur within a specific timeframe.
- **Environmental Awareness of Customers:** Customers in the channel possess environmental tendencies and the ability to recognise the environmental quality of the offered products.
- **Customer Sensitivity to Price:** The sensitivity of customers to price is known. Additionally, the level of Consumer Environmental Awareness (CEA) within the customer community is presumed to be measured previously through survey methods.
- **Symmetric Information Sharing:** For simplicity reasons it is considered that all the model parameters are known to both channel members, implying symmetric information sharing between them.
- **Deterministic Demand Function:** The demand function is deterministic and assumed to follow a linear relationship with the selling price and the greenness level of the product.
- **Static Pricing Scheme:** Due to the nature of the product and the business environment, a static pricing scheme is employed in the studied Supply Chain (SC). This suggests that the pricing strategy remains constant over the studied period.

## Model Description

The **notation** used in this tutorial is as follows:<br>
**1. Parameters**

<table>
  <tr>
    <td>Notation</td>
    <td>Description</td>
  </tr>
  <tr>
    <td><em>c</em></td>
    <td>Production cost of the manufacturer per unit</td>
  </tr>
  <tr>
    <td><em>h</td>
    <td>Greening cost coefficient</td>
  </tr>
  <tr>
    <td><em>τ</td>
    <td>Customer environmental awareness (CEA) level which is related to the willingness of consumers to buy the product with higher green quality even at a higher price</td>
  </tr>
  <tr>
    <td><em>a</td>
    <td>Basic market size</td>
  </tr>
  <tr>
    <td><em>b</td>
    <td>Price sensitivity of demand</td>
  </tr>
  <tr>
    <td><em>w</td>
    <td>The unit wholesale price</td>
  </tr>
  <tr>
    <td>&#928<sub><em>sc</sub></td>
    <td>Channel profit</td>
  </tr>
  <tr>
    <td>&#928<sub><em>m</sub></td>
    <td>Manufacturer’s profit</td>
  </tr>
  <tr>
    <td>&#928<sub><em>r</sub></td>
    <td>Retailer’s profit</td>
  </tr>
</table>

**2. Decision variables**

<table>
  <tr>
    <td>Notation</td>
    <td>Description</td>
  </tr>
  <tr>
    <td><em>p</em></td>
    <td>Selling price of the product (decision variable of the retailer)</td>
  </tr>
  <tr>
    <td><em>e</em></td>
    <td>The product green quality (decision variable of the manufacturer)</td>
  </tr>
</table>

**3. Coordination model variables**

<table>
  <tr>
    <td>Notation</td>
    <td>Description</td>
  </tr>
  <tr>
    <td><em>w<sub><em>r</sub></em></td>
    <td>Selling price of the product (decision variable of the retailer)</td>
  </tr>
  <tr>
    <td><em>&#966</em></td>
    <td>Share of greening-cost allocated to the retailer
(&#966 &#8712 [0, 1])</td>
  </tr>
  <tr>
    <td>v</td>
    <td> Share of revenue allocated to the retailer (v &#8712 [0, 1])</td>
  </tr>
</table>

## Model Formulations and solution

The optimal solutions are derived under different scenarios: (1) centralised scenario, (2) decentralised scenario, (3) coordination scenario via contracts. <br>

The **Demand Function** is D = _a − bp + τe_

### (1) Centralised model

$$
\begin{aligned}
Π_{sc}^{*} = \max_{p, e} \quad & Π_{sc} = Π_{m} + Π_{r} \\
\text{s.t.} \quad & Π_{sc} = (p - c)(a - bp + τe) - he^2\\
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial Π_{sc}}{\partial p} = 0 \quad & \Rightarrow \quad p^{c*} = \frac{τ(a - bc)}{4bh - τ^2}\\
\frac{\partial Π_{sc}}{\partial e} = 0 \quad & \Rightarrow \quad e^{c*} = \frac{2ah + 2bch -cτ^2}{4bh - τ^2} \\
\end{aligned}
$$

By substituting (2) and (3) into the demand function, we obtain the demand from consumers of the centralised model:

$$
\begin{aligned}
D(p^{c*}, e^{c*}) = a - bp^{c*} + τe^{c*} \quad & \Rightarrow \quad D(p^{c*}, e^{c*}) = \frac{2a - 2bc}{4 - \frac{τ^2}{bh}}\\
\end{aligned}
$$

Substituting equations(2) into (1), we could obtain the optimal profit of the centralised model:

$$
\begin{aligned}
Π_{sc}^{c*} = \frac{a^2 - 2abc + b^2c^2}{4bh - τ^2}
\end{aligned}
$$

$$
\begin{aligned}
Π_{m} &= (w - c)(a - bp + τe) - he^2\\
Π_{r} &= (p - w)(a - bp + τe)
\end{aligned}
$$

Furthermore, we seperate the overall profit into the profit of the manufacturer and retailer as (5). Again, we substitute (2) into (5) and obtain the optimal profit of the manufacturer and retailer of the centralised model:

$$
\begin{aligned}
Π_{m}^{c*} &= w \left(\frac{2abh - 2b^2ch}{4bh - τ^2} \right) + \frac{\begin{pmatrix} 8b^3c^2h^2 - 8ab^2ch^2 \\- 3b^2c^2hτ^2 + 4abchτ^2 - ha^2τ^2 \end{pmatrix}}{(4bh - τ^2)^2}\\
Π_{r}^{c*} &= \frac{2bh(2a^2h - 2b^2c^2h - acτ^2 + bc^2τ^2)}{(4bh - τ^2)^2} - w\frac{2abh - 2b^2ch}{(4bh - τ^2)}
\end{aligned}
$$

### Decentralised model

### (2) Decentralised model

### (3) Hybrid greening cost and revenue sharing contract

# Numerical analyses

# Conclusion
