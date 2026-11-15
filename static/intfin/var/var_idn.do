* VAR lecture: Stock and Watson (2001) "Vector Autoregressions", with Indonesian data.
* Run from the lecture folder. Data: data/idn_macro.csv (made by data/get_data.py).

clear all
set more off

* 1. Data ---------------------------------------------------------------------
import delimited "data/idn_macro.csv", clear
gen tq = quarterly(quarter, "YQ")
format tq %tq
tsset tq

gen infl   = 400 * (ln(cpi) - ln(L.cpi))   // annualised quarterly CPI inflation, %
gen growth = 400 * (ln(gdp) - ln(L.gdp))   // annualised quarterly real GDP growth, %
label variable infl   "Inflation"
label variable growth "GDP growth"
label variable rate   "Interbank rate"

keep if tin(, 2019q4)                      // estimation sample stops before COVID-19

* 2. Unit-root tests (ADF with a constant, 4 lags) -----------------------------
foreach v in infl growth rate {
    dfuller `v', lags(4)
}

* 3. Lag length ---------------------------------------------------------------
varsoc infl growth rate, maxlag(8)

* 4. Estimation: reduced-form VAR(4) ------------------------------------------
* The variable order here is the Cholesky ordering used by the IRFs below.
* dfk and small give the degrees-of-freedom corrections that R's vars package uses.
var infl growth rate, lags(1/4) dfk small

* 5. Diagnostics --------------------------------------------------------------
varstable                                  // stable if every modulus < 1
varlmar, mlag(4)                           // H0: no residual autocorrelation
matrix list e(Sigma)

* 6. Granger causality --------------------------------------------------------
vargranger

* 7. Impulse responses: Cholesky, ordering infl -> growth -> rate --------------
irf create baseline, set(var_idn, replace) step(12)
irf graph oirf, irf(baseline) impulse(rate) response(infl growth rate)
irf table oirf, irf(baseline) impulse(rate) response(infl) noci

* Same VAR, reverse ordering: rate -> growth -> infl
irf create reverse, order(rate growth infl) step(12)
irf table oirf, irf(baseline reverse) impulse(rate) response(infl) noci

* 8. Forecast error variance decomposition ------------------------------------
irf table fevd, irf(baseline) response(infl) noci
irf table fevd, irf(baseline) response(growth) noci
irf table fevd, irf(baseline) response(rate) noci

* 9. Forecasting: estimate to 2017Q4, forecast the eight quarters of 2018-2019 --
var infl growth rate if tin(, 2017q4), lags(1/4) dfk small
fcast compute f_, step(8)
fcast graph f_infl f_growth f_rate, observed
list tq infl f_infl growth f_growth rate f_rate if tin(2018q1, 2019q4), noobs
