library(tidyverse)
library(gghighlight)
migor<-readxl::read_excel("C:/github/krisna/content/id/post/migor/migor.xlsx") %>%
  mutate(Bulan = parse_date(Bulan, "%m/%Y")) %>%
  pivot_longer(!Bulan,names_to = "provinsi",values_to = "harga")
ggplot(data=migor,aes(Bulan,harga,color=provinsi))+geom_line()+
  gghighlight(provinsi%in%c("PAPUA BARAT","DKI JAKARTA","KEPULAUAN RIAU","KALIMANTAN TIMUR"))+
  theme_classic()+
  labs(
    x="Bulan",
    y="Rupiah per kg",
    title="Harga Bulanan Minyak Goreng",
    caption="sumber: PIHPS"
  )
ggsave("migor.png")
