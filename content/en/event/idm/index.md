---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Economic recovery through export"
event: "IDM Co-op FGD: Badai Pandemi, Vaksinasi dan Harapan Pemulihan Ekonomi"
event_url:
location:
address:
  street:
  city:
  region:
  postcode:
  country:
summary: I share a possible recovery through export. There seem to be a trade-off between going ahead with commodity export with an import substitution policy.
abstract: I share a possible recovery through export. There seem to be a trade-off between going ahead with commodity export with an import substitution policy. Click slides for my slides, or videos to the youtube recording of the event.

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2021-02-27T14:00:00+11:00
date_end: 2021-02-27T15:30:00+11:00
all_day: false

# Schedule page publish date (NOT event date).
publishDate: 2021-02-26T20:41:11+11:00

authors: [admin]
tags: [economics, trade, coronavirus COVID-19]

# Is this a featured event? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
links:
 - name: IDM
   url: https://www.facebook.com/idmcooperatives/photos/?ref=page_internal
   icon_pack: fab
   icon: facebook
 - name: IDM
   url: https://twitter.com/idmcoop/status/1365231406180233218?s=20
   icon_pack: fab
   icon: twitter
 - name: IDM
   url: https://www.instagram.com/p/CLwS7SuA2Mt/?utm_source=ig_web_copy_link
   icon_pack: fab
   icon: instagram

# Optional filename of your slides within your event's folder or a URL.
url_slides: 

url_code:
url_pdf:
url_video: https://www.youtube.com/watch?v=aJx7ymHrQqI

# Markdown Slides (optional).
#   Associate this event with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: "idm"

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

## Pendahuluan

During a pandemic, the best economic policy is health policy. Vaccine is often cited to be the silver bullet of Indonesian economy. Say it is true, the speed seems to suggest that we need to readjust our hope from the vaccine. Data from [our world in data](https://ourworldindata.org/coronavirus-data-explorer?zoomToSelection=true&time=2020-03-01..latest&country=IDN~BRA~TUR~IND&region=World&vaccinationsMetric=true&interval=total&perCapita=true&smoothing=0&pickerMetric=total_vaccinations_per_hundred&pickerSort=desc) Shows that our speed need some bump if we are to meet the target.

{{< figure library="true" src="/idm/gambar1.svg" title="" numbered="" width=630 >}}

That said, Vaccination does not seem to correlate with economic growth. Although Indonesia is a bit behind compare to Turkey and Brazil, the economic growth are somewhat similar. I pick weekly tracker from OECD, and this data shows that albeit vary in vaccination speed, growth are somewhat similar.

{{< figure library="true" src="/idm/gambar2.png" title="" numbered="" width=450 >}}

A note on weekly tracker, it uses machine learning to nowcast growth from google trend, so read it with a grain of salt. The data however is timely (hence nowcasting instead of forecasting).

## Export recovery

Likewise, export performance doesn't seem to be impacted by the pandemic. In fact, Indonesia's export performance in terms of value is higher in November and December 2020 compared to the [same month a year earlier](https://www.bps.go.id/website/materi_ind/materiBrsInd-20210115093516.pdf). 

Export was also the way most ASEAN countries escape the Asian Financial Crisis 1998.

A little note on that though, cuz the crisis during 1998 was pretty much concentrated in ASEAN and East Asia region, hence selling stuff to EU or US is a viable option. There was a huge drop in exchange rate too, which allows for increased competitiveness of Indonesian goods. Both doesn't happen with the same extent as 1998, perhaps for the better.

That said, stimuli from advanced economies may provide the global demand Indonesia needs right now, if one's to recover through export.

Often times, people ask me "what products do we need to push to the export market"? Very complicated question, but in this seminar, I just use Revealed Comparative Advantage (RCA) to try to attend to that question.

## RCA

RCA is one metric we can look at to assess how competitive a country is on a certain product. In the RCA term, the higher the number, the more competitive that country is in producing that particular good.

I use UNCTAD's data hence their defintion which can be read [here](https://unctadstat.unctad.org/en/RcaRadar.html). Buat yang suka rumus, silakan lihat di [akhir post ini](#rumus).

I ain't running thru all of the HS codes. I aggregate them based on HS2 which can be seen [here](#agregasi).

The picture below shows Indonesian RCA dynamics from 2000 to 2018. We can see that Indonesia's RCAs are high in mining stuff and `vegetable` oil (which is basically Crude Palm Oil or CPO). There's oil, gas and coal in `fuels` terdapat minyak bumi, gas alam dan batubara. Indonesian rubber is also highly competitive. RCA in `minerals` drops significantly, I would speculate the mineral ban ruling which was started to get very interesting in 2009 onward.

{{< figure library="true" src="/idm/gambar4.png" title="" numbered="" width=630 >}}

Indonesia also great in producing wood and wood products, also labour intensive stuff like footwear and textiles.

{{< figure library="true" src="/idm/gambar5.png" title="" numbered="" width=630 >}}

## Harga-harga komoditas

Well, naturally Indonesia is a commodity exporter. Now is indeed a good time to be a commodity exporter since the prices of all of Indonesia's export commodities are skyrocketting at the moment. Maybe not fuels, but still.

{{< figure library="true" src="/idm/gambar6.png" title="" numbered="" width=630 >}}

## Export value

Data shows that Indonesia's overall export value isn't affected very much by the pandemic. CPO and fuels domination is clearly visible here. In fact, CPO grows compared to 2019. Fuel went down amid the pandemic, however, also the energy prices shock led by oil.

{{< figure library="true" src="/idm/gambar7.png" title="" numbered="" width=630 >}}

Transportation goods are dropping, one reason why Indonesia is exempting the tax for buying a car to exploit demand market. Textiles are hurt as well, perhaps amid the PPE viasco which lead to input for textiles disrupted. Textiles is a bit GVC heavy, so a disruption in the supply chain matters a lot.

{{< figure library="true" src="/idm/gambar8.png" title="" numbered="" width=630 >}}


## RCA isn't everything

RCA changes. Indonesian RCA also changes. Maybe Indonesia will not always be a commodity exporter forever. In fact, Indonesian government are heavily intervening through import substitution policies and trying to increase domestic value added by banning mineral export. As you can see from the graph above, mineral exports are going down while the export for metals, product of smelters, are increasing. I also hear anecdotes that the government is trying to improve CPO-processing industries.

On fuels, Indonesia may need to be careful since many advanced countries these days are pushing their zero emission target. Even China, in fact. This may reduce the coal price in the future. 

Backward participation in GVC may be the best option for the governmen. Consequently, import will be a bit high since backward participation may require firms to import inputs and capital goods. Import may be as important as export itself because of this cuz import may reflect industrial activities.

## Kinerja impor

For better or worse, import is a bit stagnant. Fuels import drops, likely because of the mobility issues amid the virus. Not just fuels, many other imports are dropping.

{{< figure library="true" src="/idm/gambar9.png" title="" numbered="" width=630 >}}

Capital goods (machinery and elect) and inputs (like metal (steel is important)) also drops, which can be a bad sign.

{{< figure library="true" src="/idm/gambar10.png" title="" numbered="" width=630 >}}

## Strategi Pemerintah

Many of Indonesia's manufacturer requires imported inputs, such as:

- Soybean for tofu, tempe, chicken and beef;
- iron, steel and chemical;
- synthetic fibre, etc.

Moreover, domestic value added through export ban may take some time to realize. From nickel to battery to electric car could take years to materialized. By that time, maybe COVID is over (or maybe endemic we'll see). Hence, speed matters.

If the government opt to go ahead with the ban (sunk cost is high anyway), then fiscal support in the short run is necessary. The government just need to make sure that these industries are growing and showing promises. Additionally, it may increase import, something the government really hate. 

Retaliation is another matter with the export ban. It is kinda pointless trying to build industries with foreign debt and investment if the country can't export its product to get foreign reserves. It also possibly limits economies of scale. This possible retaliation is worth keeping in mind. If we can ban import and export, why other countries can't? RCEP may play a great role in this fiasco, but we'll see.

All in all, let's hope for the best, as usual.

## rumus

$$
RCA_{Ai}=\frac{\frac{X_{Ai}}{\sum_{j \in P} X_{Aj}}}{\frac{X_{wi}}{\sum_{j \in P} X_{wj} }} \geq 1
$$

RCA negara $A$ untuk barang $i$ tergantung pentingnya ekspor barang $i$ untuk negara $A$, dibandingkan dengan pentingnya barang $i$ di seluruh dunia $w$.

kembali ke [RCA](#rca)

## Agregasi

{{< figure library="true" src="/idm/kelompok.png" title="" numbered="true" width=600 >}}

kembali ke [RCA](#rca)

