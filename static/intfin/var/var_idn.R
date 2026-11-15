# VAR lecture: Stock and Watson (2001) "Vector Autoregressions", with Indonesian data.
# Run from the lecture folder. Data: data/idn_macro.csv (made by data/get_data.py).

library(vars)  # VAR(), VARselect(), irf(), fevd(), causality(), predict()
library(urca)  # ur.df()

# 1. Data ---------------------------------------------------------------------
d <- read.csv("data/idn_macro.csv")
d$infl   <- c(NA, 400 * diff(log(d$cpi)))  # annualised quarterly CPI inflation, %
d$growth <- c(NA, 400 * diff(log(d$gdp)))  # annualised quarterly real GDP growth, %

variables <- c("infl", "growth", "rate")   # this is also the Cholesky ordering
y_all <- ts(d[-1, variables], start = c(2000, 2), frequency = 4)
y     <- window(y_all, end = c(2019, 4))   # estimation sample stops before COVID-19

# 2. Unit-root tests (ADF with a constant, 4 lags) -----------------------------
adf <- sapply(variables, function(v) {
  test <- ur.df(y[, v], type = "drift", lags = 4)
  c(statistic = test@teststat[1, "tau2"], critical_5pct = test@cval["tau2", "5pct"])
})
print(round(adf, 2))

# 3. Lag length ---------------------------------------------------------------
lag_choice <- VARselect(y, lag.max = 8, type = "const")
print(lag_choice$selection)

# 4. Estimation: reduced-form VAR(4), equation-by-equation OLS -----------------
m <- VAR(y, p = 4, type = "const")
summary(m)

# 5. Diagnostics --------------------------------------------------------------
print(round(roots(m), 3))                               # stable if every modulus < 1
lm_test <- serial.test(m, lags.bg = 4, type = "BG")     # H0: no residual autocorrelation
print(lm_test)
residual_corr <- cor(resid(m))
print(round(residual_corr, 2))

# 6. Granger causality --------------------------------------------------------
# F-test that every lag of `cause` has a zero coefficient in the `effect` equation.
granger <- function(model, cause, effect) {
  equation <- model$varresult[[effect]]
  lags <- grep(paste0("^", cause, "\\.l"), names(coef(equation)))
  b <- coef(equation)[lags]
  f <- drop(t(b) %*% solve(vcov(equation)[lags, lags]) %*% b) / length(lags)
  pf(f, length(lags), equation$df.residual, lower.tail = FALSE)
}
# Rows: regressor (cause). Columns: dependent variable (effect). Cells: p-values.
granger_p <- outer(variables, variables, Vectorize(function(cause, effect) granger(m, cause, effect)))
dimnames(granger_p) <- list(cause = variables, effect = variables)
print(round(granger_p, 3))

causality(m, cause = "rate")$Granger                    # block test: rate -> (infl, growth)

# 7. Impulse responses: Cholesky, ordering infl -> growth -> rate --------------
horizon <- 12
ir <- irf(m, n.ahead = horizon, ortho = TRUE, boot = TRUE, runs = 1000, ci = 0.95, seed = 2001)
plot(irf(m, impulse = "rate", n.ahead = horizon, runs = 200, seed = 2001))

# Same VAR, reverse ordering: rate -> growth -> infl
m_reverse  <- VAR(y[, rev(variables)], p = 4, type = "const")
ir_reverse <- irf(m_reverse, n.ahead = horizon, ortho = TRUE, boot = TRUE, runs = 1000, ci = 0.95, seed = 2001)

# 8. Forecast error variance decomposition ------------------------------------
fe <- fevd(m, n.ahead = horizon)
print(lapply(fe, function(x) round(100 * x[c(1, 4, 8, 12), ], 1)))

# 9. Forecasting --------------------------------------------------------------
# 9a. Estimate to 2017Q4, forecast the eight quarters of 2018-2019.
m_2017   <- VAR(window(y, end = c(2017, 4)), p = 4, type = "const")
forecast <- predict(m_2017, n.ahead = 8, ci = 0.95)

# 9b. Recursive pseudo out-of-sample comparison, as in Stock and Watson's Table 2:
#     random walk, AR(4) and VAR(4), forecast origins 2011Q4 to 2019Q3.
horizons <- c(1, 4, 8)
origins  <- which(time(y) >= 2011.75 & time(y) < 2019.75)
errors   <- list()
for (origin in origins) {
  train  <- ts(y[1:origin, ], start = start(y), frequency = 4)
  var_fc <- predict(VAR(train, p = 4, type = "const"), n.ahead = max(horizons))$fcst
  for (v in variables) {
    ar_fc <- predict(ar(train[, v], order.max = 4, aic = FALSE, method = "ols"), n.ahead = max(horizons))$pred
    for (h in horizons[origin + horizons <= nrow(y)]) {
      actual <- y[origin + h, v]
      errors[[length(errors) + 1]] <- data.frame(
        variable = v, h = h,
        rw = actual - train[origin, v], ar = actual - ar_fc[h], var = actual - var_fc[[v]][h, "fcst"]
      )
    }
  }
}
errors <- do.call(rbind, errors)
rmse <- aggregate(cbind(rw, ar, var) ~ h + variable, errors, function(e) sqrt(mean(e^2)))
print(rmse, digits = 3)

# 10. What COVID-19 does: same VAR on the full sample ---------------------------
m_full <- VAR(y_all, p = 4, type = "const")
print(round(rbind(pre_covid = sqrt(diag(summary(m)$covres)), full = sqrt(diag(summary(m_full)$covres))), 2))
