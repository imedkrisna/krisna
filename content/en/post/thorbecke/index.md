---
title: "Thorbecke 2019: Japan's Exchange Rate and Electronics Exports"
categories: [Economics, Data & Code]
tags: [economics, econometrics]
date: '2020-02-25'
authors: [admin]
---

For my first paper review post, I will cover a paper by Thorbecke that is certainly interesting. The paper, which examines how Japan's electronics export competitiveness was affected by exchange rate movements, was recently published. It is fascinating to see how a manufacturing giant like Japan has been displaced by South Korea and Taiwan.

The paper starts with a compelling premise. Japan has long been a powerhouse in exporting electronic components and parts. Competition in components and parts is quite fierce, so Japan has to compete on price with other countries (mainly Taiwan and South Korea). Trouble came when the Global Financial Crisis (GFC) hit. Japan suddenly became a safe haven. Capital flowed in, the Yen appreciated, and export prices became expensive relative to costs denominated in Yen. This caused Japan's electronic components and parts industry to lose competitiveness against other countries -- an effect that persists to this day.

The paper uses a Vector Auto Regressive (VAR) method. The estimation takes roughly the following form:

$$ \Delta p_{jt}^x = \beta_0 + \sum_{i=0}^p \beta_{1i} \Delta e_{jt-i} + \sum_{i=0}^p \beta{2i} \Delta p_{t-i}^f + \sum_{i=0}^p \beta_{3i} \Delta c_{jt-i} + \sum_{i=0}^q \beta_{4i} \Delta y_{t-i}^f + u_t $$

where $p^x$ denotes Japan's export price to a destination country, $e$ is the exchange rate, $p^f$ is the international market price, $c$ represents production cost, and $y$ is the producer price index in OECD countries. All data in the paper come from the Bank of Japan and the OECD. The model itself is fairly straightforward and could readily be replicated for other country contexts -- provided, of course, that comparable data are available as those supplied by the Bank of Japan. The key identification assumption is that the sudden exchange rate change is treated as exogenous.

Upon reading this paper, the first thing I noticed was how convincingly the initial premise was built. The author opens with a simple yet impactful narrative supported by clear findings. The charts used (such as producer price indices and export price indices) strongly support the storytelling in the opening section. The model is not overly complicated either, relying on the assumption that the exchange rate is exogenous. Having a natural experiment like a financial crisis is certainly advantageous for a researcher.

Just kidding. Crises are bad. Nobody wants a crisis. Hopefully we will not see another one.

Anyway, this paper is very concise -- only 9 pages. The results are as expected, and with the key variable assumed to be exogenous, there is no need for complex methods to deal with endogeneity bias. It is a fairly accessible paper for someone who is just starting to learn about VAR.
