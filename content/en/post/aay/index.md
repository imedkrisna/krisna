---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Reviewing the National Economic Council Paper on the Economic Impact of Free Nutritious Meals"
subtitle: ""
summary: ""
authors: [admin]
tags: [CGE, Economics,MBG]
categories: [CGE, Economics,MBG]
date: 2025-03-24T21:06:59+07:00
lastmod: 2025-03-24T21:06:59+07:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

It was quite surprising yet interesting when I watched the [press conference](https://www.youtube.com/watch?v=YapJrjVDYpY) by the National Economic Council (DEN) some time ago. The reason was that Luhut Binsar Panjaitan (LBP), the DEN chair, gave the _spotlight_ to Professor Arif Anshory Yusuf (AAY) to present a _teaser_ of his _ex-ante_ model results on the impact of the Free Nutritious Meals program (MBG) on the economy. According to AAY, MBG has the potential to create 1.9 million jobs and reduce poverty by up to 5.8%. MBG, he said, is equivalent to giving IDR 600,000 per family if the average number of children in poor families is 3. This figure is 3x larger than PKH! He also added that to realize the maximum impact of MBG, "leakage" of food demand "that does not need to be imported" should be minimized by prioritizing domestic products. _Those numbers sound off._

Then on the evening of March 23, 2025 Jakarta time, I watched Professor Arief Anshory Yusuf (AAY) present his latest paper written for the National Economic Council (DEN). The event was organized by Doctrine UK, an Indonesian student association in the United Kingdom. There, he presented a paper on the macroeconomic impact analysis of the Free Nutritious Meals program (MBG). The paper itself was shared in the event chat. The recording has been uploaded to YouTube and can be viewed [here](https://www.youtube.com/watch?v=tWA4TwJJ2b4).

After reviewing both the paper and the presentation, I felt compelled to write some notes about it. The main purpose is actually for myself, since this model is quite fun to explore and replicate. Additionally, at the event, AAY also represented DEN, which means the policies emerging from this paper can be considered as coming from the government and will likely become public policy. I'm also writing this for friends who aren't very familiar with CGE[^1] but want to learn. Lastly, it would be great if this post were read by AAY and DEN, but I'm sure someone of his caliber already receives plenty of input from people far more capable than me, so it's fine if this goal isn't achieved. Mostly, this post is for learning and sharing.

I greatly respect him as an academic because AAY is one of the few Indonesian economists who is very vocal about economic issues in Indonesia, especially on Higher Education and pro-poor and pro-job programs. He does not hesitate to criticize the government. Even his paper, which serves as the _ex-ante_ justification for MBG, was shared with everyone, and he regularly presents and seeks opinions from many people across various circles. This level of transparency is something I haven't found in other government policies.

_Having said that_, I have some notes that I believe are very important and _worth_ writing about on this blog. I will focus on 2 caveats that he mentioned in his presentation. For other parts, that can be an opportunity for other friends who want to contribute comments. For example, [Riandy Laksono's](https://medium.com/@laksonomics/klaim-bombastis-dampak-mbg-yang-menyesatkan-be8a9f37cc50) commentary is also very interesting in my opinion, and easier to read than this post haha.

I will start by briefly summarizing the points I agree with, then move on to things I'm less sure about or disagree with.

## Key points in my view

In his paper, AAY summarizes various studies about programs similar to MBG in other countries. In other countries, according to him, MBG has been quite successful. He also says that MBG is a very progressive program. I think it's hard to disagree that MBG, as a concept, is a progressive program.

The paper also explains some details about MBG that are consistent with explanations from other sources (e.g., CISDI). He mentions a budget of 171 trillion rupiah, _one of the largest welfare programs in the world_, targeting approximately 82.9 million people.

Equally important: AAY mentions several official objectives of MBG: better nutrition, job creation, supporting local food systems, and improving student attendance and health. Nevertheless, he says that MBG should not be designed to pursue too many objectives at once, and I agree.

Finally, AAY uses input-output (IO) analysis and microsimulation to show the economic impacts in terms of increased output, value added, and employment, as well as poverty reduction from this program. Various simulations with different scenarios were conducted, but the results are consistently positive overall.

## Important caveats

However, in his presentation, AAY stated two caveats that are very heroic and automatically dismiss much of the discussion about MBG:

1. This model is an _ex-ante_ scenario assuming ideal implementation. All criticisms regarding operational aspects cannot be answered with this paper.
2. There is no general equilibrium aspect (supply, demand, market, and optimization, at least), so things like price changes and international trade are not reflected in this model.

In my personal opinion, these two things are _arguably_ the most influential factors that could potentially derail this program. At the Doctrine UK event the other day, perhaps the majority of questions and discussions from participants were precisely about best practices and institutional readiness. I add some additional thoughts here beyond what was already raised by friends at the event, which can be read directly at the [end of this post](#implementation-problems).

But this post will hyperfocus on point 2, something more relevant to AAY's paper. I was quite surprised to hear AAY argue that IO analysis $\neq$ Computable General Equilibrium (CGE), and that IO does not account for price changes. In my opinion, that statement is not technically correct. I will also provide 3 arguments for why the results from the IO scenario may not be suitable for making claims as confident as what AAY showed at the DEN press conference above.

I will nerd out a bit about CGE to address caveat no. 2. This section will be too _geeky_. Read at your own risk. You've been warned.

## The General Equilibrium Aspect

### What is Input-Output Analysis (IO)?

In his paper, AAY explains IO in section 3.1.1., which is on page 4 of the paper.

There are 3 important terms AAY uses when explaining IO analysis: output, value added, and employment. Output is essentially the total production of an industry. Value added is total production minus inputs/raw materials. So value added consists of factors of production, _mainly_ labor and capital. And labor equals employment.

The IO structure in AAY's paper is exactly the same as a typical IO model, which is more or less like this:

$$
  \begin{align*}
  x&=Ax+y \newline
  (I-A)x&=y \newline
  x&=(I-A)^{-1}y
  \end{align*}
$$

where the resulting vector x represents input demand for sector $i$. That is, input demand from vector $i$ depends on the shift-share $A$ of each industry in $x$ for each industry in $x$, and final demand $y$.

In an Input-Output table, we can show output and value added if you open an actual IO table from BPS.

| wew | s1 | s2 ... sj | y | sum |
| --- | --- | -------- | --- | --- |
| s1 | $q_{1,1}$ | $q_{1,2} \dots q_{1,j}$ | $y_1$ | $x_1$ |
| s2 | $q_{2,1}$ | $q_{2,2} \dots q_{2,j}$ | $y_2$ | $x_2$ |
| $\vdots$ | $\ddots$ | $\ddots$ | $\vdots$ | $\vdots$ |
| si | $q_{i,1}$ | $q_{i,2} \dots q_{i,j}$ | $y_i$ |
| va | $va_1$ | $va_2 \dots va_j$ | - | GDP |
| sum | $x_1$ | $ x_2 \dots x_j$ | GDP | - |

Here, $q_{i,j}$ can be formed into a matrix equivalent to $Ax$ by setting $q_{i,j}=a_{i,j}x_i$. Hopefully that's clear.

Usually, matrix $Ax$ is set through some optimization (you know, lagrange and stuff). Well, typically, matrix A in IO analysis is exogenous. In other words, the elements of matrix A are fixed and only expand along with output $x$. Therefore, all exogenous changes in the economy (in this case in $y$) are assumed to only expand according to matrix A.

Actually, IO is also CGE. It's just that IO is a _special case_ of CGE, where the output demand function has a _perfect complement_ property. Perfect complement is a very useful assumption because the optimization becomes linear. Computationally, it becomes much easier since we only need linear algebra without any nonlinear optimization.

Additionally, Leontief is convenient because the optimization only expands according to the optimal share of each component.

For example, an input function $U=min(a_1x_1,a_2x_2)$ will have an optimal point at $a_1x_1=a_2x_2$ so the demand function for $x_1$ will be $x_1=\frac{a_2}{a_1}x_2$ and $\frac{a_2}{a_1}$ will be constant and fixed throughout changes in the consumption composite.

This method is relatively straightforward to implement in Python, as long as the IO matrix is available. I tried to replicate using a lite version of the IO table, [which is aggregated to 17 sectors](https://www.bps.go.id/en/statistics-table/1/MjI2OSMx/tabel-input-output-indonesia-transaksi-domestik-atas-dasar-harga-dasar--17-produk---2020--juta-rupiah-.html). Of all the scenarios, I will try to replicate scenario A1 in the paper. From the 17-sector IO table, the lite version, I converted it into matrix A, x and y, and the data for the matrices and vectors can be downloaded [here](https://1drv.ms/f/s!AjelszXKKcmskdpCs3C-MVYQOLtW0w?e=kIzj2t). Note that the y matrix there still contains import values. That's why in my simulation I construct y myself, not using y from there, so the imports are removed. Actually, you can also subtract the imports from final demand in the Excel file yourself.




```python
import numpy as np
A=np.loadtxt('A.csv',delimiter=',') # matrix A
#y=np.loadtxt('y.csv',delimiter=',') ini final demand yang ada final importnya
u=np.loadtxt('x.csv',delimiter=',') # output
y=u-np.dot(A,u) # final demand tanpa final import
ia=np.identity(17)-A
invA=np.linalg.inv(ia)
np.savetxt('invA.csv', invA,delimiter=",") # save the change matrix result to a new file
x=np.dot(invA,y) ## Make sure replikasi final output di tabel.
x-u
```




    array([ 0.00000000e+00,  4.76837158e-07,  9.53674316e-07,  1.19209290e-07,
           -1.49011612e-08, -4.76837158e-07,  4.76837158e-07,  0.00000000e+00,
            2.38418579e-07,  0.00000000e+00,  0.00000000e+00, -1.19209290e-07,
            0.00000000e+00, -1.19209290e-07,  1.19209290e-07, -1.19209290e-07,
           -1.19209290e-07])




```python
## Simulasi MBG A1 di paper AAY
yy=y+np.array([0,0,0,0,0,0,0,0,171e6,0,0,0,0,-171e6,0,0,0]) ## + MBG shock - budget shock
xx=np.dot(invA,yy)
print(f'perubahan %output sektoral setelah +MBG-penghematan:\n {(xx-x)/x*100}') ## Percent change of sectoral output
```

    perubahan %output sektoral setelah +MBG-penghematan:
     [  1.08864224   0.03824485   0.57615184  -0.79322713  -0.71996072
      -0.27533884   0.34350708  -0.80514386  13.29429074  -1.13615204
       0.0553673   -0.13483742  -1.60608706 -22.73385632  -0.14187647
      -0.18583608  -0.23295487]
    


```python
print(f'pertumbuhan output nasional adalah {(np.sum(xx)-np.sum(x))/np.sum(x)*100} persen') ## Percent change of total output
```

    pertumbuhan output nasional adalah 0.046445748306372714 persen
    


```python
## Put everything into a dataframe
import pandas as pd
sec=["Pertanian, Kehutanan, dan Perikanan", "Pertambangan dan Penggalian", "Industri Pengolahan", "Pengadaan Listrik dan Gas", "Pengadaan Air, Pengelolaan Sampah, Limbah dan Daur Ulang", "Konstruksi", "Perdagangan Besar dan Eceran; Reparasi Mobil dan Sepeda Motor", "Transportasi dan Pergudangan", "Penyediaan Akomodasi dan Makan Minum", "Informasi dan Komunikasi", "Jasa Keuangan dan Asuransi", "Real Estate", "Jasa Perusahaan", "Administrasi Pemerintahan, Pertahanan dan Jaminan Sosial Wajib", "Jasa Pendidikan", "Jasa Kesehatan dan Kegiatan Sosial", "Jasa lainnya"]
delta=(xx-x)/x*100
## Create pandas of the result
df=pd.DataFrame({'sektor':sec,'delta':delta})
#concat the national results
df2=pd.DataFrame({'sektor':'Total','delta':(np.sum(xx)-np.sum(x))/np.sum(x)*100},index=[17])
df=pd.concat([df,df2])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sektor</th>
      <th>delta</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Pertanian, Kehutanan, dan Perikanan</td>
      <td>1.088642</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pertambangan dan Penggalian</td>
      <td>0.038245</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Industri Pengolahan</td>
      <td>0.576152</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pengadaan Listrik dan Gas</td>
      <td>-0.793227</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Pengadaan Air, Pengelolaan Sampah, Limbah dan ...</td>
      <td>-0.719961</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Konstruksi</td>
      <td>-0.275339</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Perdagangan Besar dan Eceran; Reparasi Mobil d...</td>
      <td>0.343507</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Transportasi dan Pergudangan</td>
      <td>-0.805144</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Penyediaan Akomodasi dan Makan Minum</td>
      <td>13.294291</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Informasi dan Komunikasi</td>
      <td>-1.136152</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Jasa Keuangan dan Asuransi</td>
      <td>0.055367</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Real Estate</td>
      <td>-0.134837</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Jasa Perusahaan</td>
      <td>-1.606087</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Administrasi Pemerintahan, Pertahanan dan Jami...</td>
      <td>-22.733856</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Jasa Pendidikan</td>
      <td>-0.141876</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Jasa Kesehatan dan Kegiatan Sosial</td>
      <td>-0.185836</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Jasa lainnya</td>
      <td>-0.232955</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Total</td>
      <td>0.046446</td>
    </tr>
  </tbody>
</table>
</div>



| indicator | original | replica |
| ------ | --- | --- |
| National output | 0.06 | 0.046 |
| Agriculture | 1.37 | 1.08 |
| manufacture | 0.12 | 0.57 |

The A1 simulation results: the original is from AAY, the replica is mine. There are differences in the numbers, likely due to different tables and certainly different aggregation levels. But they're relatively close, so I think it's fairly accurate haha.

Three limitations of this model are immediately apparent.

First is the limitation of the _constant shift-share_ assumption a la Leontief. This is immediately visible from the source of growth. The _balanced budget_ reallocation produces positive additional output because the food service sector has a larger "total multiplier" (in the paper, terms $m_{ij}$ and $m_{ik}$, pp.6) than the government services sector. The problem is that this total multiplier is constant regardless of how much is added or subtracted. Without changes in marginal return, if the goal is output growth, we might as well move ALL output from government services to the food service sector (i.e., corner solution). But in the real world this doesn't happen, because as a sector loses output, marginal productivity there rises, while a sector that is already bloated will experience diminishing returns, eliminating gains as more resources flow into it. Plus, on the demand side, there is also marginal utility that changes as consumption patterns concentrate on a single service. This is not a problem if the shock is relatively small. But given that the MBG shock raises the food service sector by 13.3% and cuts the government service sector by -22.73%, the constant marginal return assumption is likely to be problematic.

Second, the vector $y$ is treated as final demand without considering exports and imports. Indeed, the $y$ column in the BPS IO table originally contains capital formation and exports, which are aggregated into $y$ here. Meanwhile, in the first column there should be an imported raw materials row. In CGE, we often add a substitution function with Armington elasticity between imported and domestic inputs for each sector. Naturally, the absence of international trade (or more precisely, treating the shift-share of international trade as exogenous/constant) makes it difficult to forecast MBG's impact on exports and imports. That is why AAY said at [this event](https://www.youtube.com/watch?v=YapJrjVDYpY) something like MBG will have a good impact as long as there is no "leakage," that "materials that don't need to be imported" should not be imported. I think this is not the best way to conclude from the model.

More importantly, in AAY's paper, I could not find information about which table he used for the analysis. This is important because BPS has 2 types of IO tables: [total transactions](https://www.bps.go.id/en/statistics-table/1/MjI3MSMx/indonesia-input-output-table-for-total-transactions-at-basic-prices--17-products---2020.html) and [domestic transactions](https://www.bps.go.id/en/statistics-table/1/MjI2OSMx/tabel-input-output-indonesia-transaksi-domestik-atas-dasar-harga-dasar--17-produk---2020--juta-rupiah-.html). In the domestic table, only domestic input figures appear in the $Ax$ matrix, and all imports are pooled in row 2000. In the total table, the $Ax$ matrix already includes imports, so row 2000 is empty. There is no information in the paper about whether Armington calibration was performed for domestic vs. imported product choices.

If the domestic transaction table was used, then the $Ax$ matrix does not reflect total inputs (tends to be biased), implicitly treating imports as fixed, hence the "don't leak" conclusion, which may be consistent with what the model says. But if the total transaction table was used, then the $Ax$ matrix already _includes_ imported goods, and it may well be that "leakage" occurs in the model with no negative consequences whatsoever. Or maybe I'm the one misreading it and the procedure for removing imported input is actually explained somewhere in the paper. But it should be made more explicit.

However, the critique about the exogenous trade balance is actually very much related to the third critique: the absence of prices. The absence of prices becomes super relevant when we use a model with optimization and _constraints_. Without constraints, production in the MBG-recipient sector can seemingly expand as far as $Ax$. In reality, it is the supply-side _constraint_ that would cause inflation. When there is a (budget) constraint, optimization must be performed, and consequently _income effect_ and _substitution effect_ will emerge (if using assumptions other than Leontief). In particular, this _income effect_ will greatly affect the need for exports/imports, but more importantly, total consumption and poverty calculations.

Let me explain.

### Constraint and prices

Under the Leontief assumption, when we _shock_ final demand (in column $y_i$ where $i=$ the shocked sector), output from the shocked sector increases, and input demand from that sector increases, visible in column $s_j$ where $j=$ the sector experiencing the change in $y$. Like $\frac{dy}{dx}$ sort of thing.

For example, if demand in sector $k$ increases to $y_k+1$ so we have a vector $y_{new}$ shaped like this:

$$
  y_{new}=y+
  \begin{bmatrix}
  0 \newline
  \vdots \newline
  1 \newline
  \vdots \newline
  0 
  \end{bmatrix}
$$

let us call that new vector $d$ so that $y_{new}=y+d$. Then we compute $x_{new}=(I-A)^{-1}y_{new}$.

$$
  \begin{align*}
  x_{new}&=(I-A)^{-1}(y+d) \newline
  x_{new}&=(I-A)^{-1}y+(I-A)^{-1}d \newline
  x_{new}&=x+(I-A)^{-1}d
  \end{align*}
$$

The change in input demand from sector $k$ is exactly $(I-A)^{-1}$. AAY explains this on page 6 of his paper. Now, that term contains the identity matrix and matrix $A$, which we have made exogenous. This means the change in input demand from that sector depends only on $\Delta y$ and does not depend on price changes at all.

The BPS 2020 IO table is essentially a transaction matrix. Transactions _imply current prices_, where there is both quantity and price. Now, a simple IO exercise usually treats those matrix values as quantities. So if an element of the matrix (which is actually a value) moves, the movement is treated as a quantity movement.

The problem is that, with _constraints_, we can show that _input demand_ usually depends on prices!

Consider typical Leontief production:

$$
  \begin{align*}
  \max \min(a_1q_1,a_2q_2) \newline
  \text{subject to} \ p_1 q_1+p_2 q_2 \leq I
  \end{align*}
$$

Optimization implies $a_1q_1=a_2q_2$, so $q_1=\frac{a_2}{a_1}q_2$. Substituting into the constraint:

$$
  \begin{align*}
  p_1 \frac{a_2}{a_1}q_2+p_2 q_2 = I \newline
  q_2=\frac{I}{\frac{a_2}{a_2}p_2+\frac{a_2}{a_i}p_1}
  \end{align*}
$$

If we replace income $I$ with the price of output 1 times the quantity of output 1, $p_1x_1$, then demand for output 2 becomes:

$$
q_2=\frac{p_1x_1}{\frac{a_2}{a_1}p_1+\frac{a_2}{a_2}p_2}
$$

and we can generalize the equation above for $\max \min(a_1q_1,a_2q_2,\dots,a_Jq_J)$ to:

$$
q^j_i=\frac{p_ix_i}{\sum_{s=1}^S \frac{a^s_i}{a^j_i}p_s}
$$

where $q^j_i$ is the material input from industry $j$ to industry $i$, $p_i$ is the output price of industry $i$, $x_i$ is the output of industry $i$. $q^j_i$ is a function of the isocost of industry $i$ (which equals total revenue) and input prices for each industry $s$ including $s=j$.

In the replication [above](#what-is-input-output-analysis-io), $q^j_i$ is proxied by $a_{i,j}x_i$, where this term only changes because of $x_i$. Yet, as shown above, prices also matter. If $p=1$, then $q$ simply has relative shift share $a$ and final demand $x$, which is exactly what happens in the replication above.

Now, one can argue that price-dependent input demand is not a problem as long as we assume the sector is a _price taker_. That is, the demanding sector is so small that the market will always provide supply (i.e., there are _infinitely many_ suppliers) without affecting price increases. But this is certainly not always realistic, especially since the sector _in question_ has high demand for agricultural products, a sector that has historically always been plagued by bureaucratic trade governance, miscalculations, perpetually failed self-sufficiency programs, and so on. It seems difficult to expect super elastic supply from this sector.

Of course, we could also model the limitations from the _supply composite_ labor side, where we could model a _production nest_. Indeed, in the IO table there is actually a separate labor share, which is also assumed to have a constant parameter $e$, just like value added which has a constant parameter $v$. Both assumptions can be relaxed.

But perhaps another time.

## Implementation problems

I also intend to add some thoughts on the importance of considering implementation problems that will have a very significant impact on the conclusions about MBG's impact.

I agree that if ALL schools receive this program, then it could be progressive, assuming the budget sacrificed for MBG comes from a line item that is usually enjoyed by the [relatively wealthier segment of society](https://www.krisna.or.id/post/consumption/) (hence lower marginal propensity to consume[^2]). But there are several implementation possibilities suggesting this may not happen on the ground.

First, regarding the distribution of recipient schools. As I understand it, not all schools receive this program simultaneously. Some schools get MBG (treatment) and others do not (control). The problem arises if treatment does not occur randomly/exogenously. For example, if in general the schools that receive it first are those that tend to be more prepared in terms of infrastructure. Such schools are typically located in relatively wealthier areas. If this is the case, although AAY provides some anecdotes about poor community groups as beneficiaries, many participants may actually be in areas that are already fairly well-off.

Second is corruption. If this program is corrupted, the corrupt actors are most likely much wealthier than the beneficiaries. This means MBG would be dangerous if it becomes a vehicle for income transfer from the party whose budget was cut to the party that corrupts MBG. This is certainly not pro-poor. Indications of corruption (or at least failure to meet good nutritional standards) were already raised by participants at the Doctrine UK event the other day.

Lastly, the CGE scenario above may also be less effective if it turns out that not all of the 171T is used for food portions. Some of the money could also be used for operations and institution-building. Someone mentioned that the Ministry of Health already has institutions ready for use, so there's no need to create new institutions like BGN and communal kitchens. A waste of resources.

## Conclusion

In closing, I have tried to offer constructive criticism in this post. I focused on the IO model and tried to show that 3 assumptions in the IO model (constant shift-share, absence of international trade, and fixed nominal prices) could be violated. Of course, no model will be exactly the same as the real world. _All models are wrong_ but that's fine as long as the model is useful for explaining phenomena. It only becomes a problem when the assumptions that don't hold have very important consequences for the conclusions drawn as a basis for policy.

I also want to once again express my appreciation for AAY for providing a level of transparency that is quite rare in government circles. It is very rare for anyone to document the studies used by the government as a _policy guide_, so that _civil society_ like me can participate in the debate. As someone still junior, my input may not be that important, but it's nice to be able to follow the thinking of Indonesia's policy architects and learn from it. Hopefully this kind of openness will spread to all government sectors.

I'll stop here for now. Maybe next time we can try modeling that _production nest_ if I have some spare time. It's gonna be fun! It's been a long time since I've tinkered with CGE. Alright, see ya next post.

[^1]: Honestly, I'm not that great at CGE either, so please take this post with a grain of salt.
[^2]: BTW, MPC <1 is what makes in-kind assistance like MBG potentially more effective at boosting consumption than cash transfers. Worth a separate discussion.
