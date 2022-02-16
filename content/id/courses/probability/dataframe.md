---
title: Data Frame
date: '2021-01-01'
type: book
weight: 20
---

Menarik file yang di-host di google drive:

```r
id <- "0B-wuZ2XMFIBUd09Ob0pKVkRzQTA" # google file ID
read.csv(sprintf("https://docs.google.com/uc?id=%s&export=download", id))
```

### Dual Y-axis

not using ggplot2 cuz ggplot2 doesn't like dual Y-axis. [Source](https://thepracticalr.wordpress.com/2016/08/30/2-y-axis-plotting/).

```r
# final plot
par(mar = c(5, 5, 3, 5))
plot(beaver1[1:100, 3], type ="l", ylab = "beaver1 temperature",
     main = "Beaver Temperature Plot", xlab = "Time",
     col = "blue")
par(new = TRUE)
plot(beaver2[,3], type = "l", xaxt = "n", yaxt = "n",
     ylab = "", xlab = "", col = "red", lty = 2)
axis(side = 4)
mtext("beaver2 temperature", side = 4, line = 3)
legend("topleft", c("beaver1", "beaver2"),
       col = c("blue", "red"), lty = c(1, 2))
```