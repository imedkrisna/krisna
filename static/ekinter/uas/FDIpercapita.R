library(WDI)
library(tidyverse)

indi<-c(           
  "fdi"="BX.KLT.DINV.CD.WD",
  "lab"="SL.TLF.TOTL.IN",
  "pop"="SP.POP.TOTL"
)

ctr<-c('BGD','CHN','IDN','MYS','IND','THA','VNM')

dat<-as_tibble(WDI(
  indicator = indi,
  country = ctr,
  start=2017
  ))
dat$weks<-dat$fdi/dat$pop
dat$wuks<-dat$fdi/dat$lab

dat |>
  subset(country!="China") |> 
  ggplot(aes(x=year,y=fdi,color=country))+geom_line(linewidth=1.1)+theme_classic()+
  labs(title = "Total FDI, BoP, current USD (minus China)", y="Total FDI, current USD")+
  scale_y_continuous(labels = scales::label_number_si())
ggsave("pic1.svg")
ggplot(data=dat,aes(x=year,y=weks,color=country))+geom_line(linewidth=1.1)+theme_classic()+
  labs(title = "Total FDI per capita, current USD (with China)", y="FDI per capita, current USD")+
  scale_y_continuous(labels = scales::label_number_si())
ggsave("pic2.svg")
ggplot(data=dat,aes(x=year,y=wuks,color=country))+geom_line(linewidth=1.1)+theme_classic()+
  labs(title = "Total FDI per worker, current USD (with China)", y="FDI per worker, current USD")+
  scale_y_continuous(labels = scales::label_number_si())
ggsave("pic3.svg")