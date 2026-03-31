---
layout: post
title: "The Export Ban and Standards Relaxation Drama in Indonesia's PPE Market"
categories: [industry]
tags: [coronavirus COVID-19, trade, industry]
date: '2020-06-10'
author: admin
---

It's probably no secret that I've been somewhat critical of the Ministry of Trade's export ban, specifically Permendag 34/2020 on the export ban of antiseptics, PPE, masks, and PPE raw materials. The regulation may be well-intentioned, but it [can have negative effects](https://imedkrisna.github.io/covtrade/) by disrupting supply chains, reducing the credibility of our government and businesses, and failing to help increase production capacity. Especially since we are highly import-dependent for nearly every COVID-19-related *item* (see tables 1 and 2). We could help the world fight COVID-19 by contributing our garment-sewing workforce for PPE, while obtaining those imported goods in return. Exports would also help secure dollar reserves for imports.

**Table 1.** Imports of COVID-19-related goods (1,000 $)
<table>
  {% for row in site.data.coronaimpor %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>
<span style="font-size:0.8em"> *source: processed from the Ministry of Industry based on BPS data* </span>

<span style="font-size:0.8em">note: WCO/WHO classification can be found [here](http://www.wcoomd.org/en/media/newsroom/2020/june/new-edition-of-the-wco-who-hs-classification-list-for-covid-19-medical-supplies-now-available). I'm still using edition 2; the latest is edition 3</span>

**Table 2.** Exports of COVID-19-related goods (1,000 $)
<table>
  {% for row in site.data.coronaekspor %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>
<span style="font-size:0.8em"> *source: processed from the Ministry of Industry based on BPS data*</span>

<span style="font-size:0.8em">note: WCO/WHO classification can be found [here](http://www.wcoomd.org/en/media/newsroom/2020/june/new-edition-of-the-wco-who-hs-classification-list-for-covid-19-medical-supplies-now-available). I'm still using edition 2; the latest is edition 3</span>

## Supply chain disruption
What I feared has happened: [The private sector has been able to produce quite a lot of PPE, but not all of it is being absorbed by the domestic market](https://tirto.id/apd-lokal-melimpah-dan-kemenkes-enggan-menyerapnya-fETf). The reason is that the Ministry of Health doesn't want to risk domestically produced goods whose quality isn't guaranteed, not made from non-woven material. Well, this spunbond non-woven material is imported; we're not yet capable of mass-producing spunbond in-country. Most domestically produced PPE is cotton-based, which according to the Ministry of Health isn't good enough, even though producers claim their PPE meets WHO standards.

What I find quite ironic is that the reason these companies were able to produce PPE in the first place is because [the Ministry of Health relaxed distribution permits for PPE-producing companies](https://republika.co.id/berita/q8xdu7396/kemenkes-permudah-penerbitan-izin-edar-industri-produksi-apd). In fact, the Ministry boasted about the rapid growth of PPE suppliers *thanks to* their permit relaxation initiative. True, thanks to the relaxation, the number of PPE-supplying companies increased. But then the Ministry itself refused to buy because there were no standards -- the very thing they had relaxed through their own policy. Wow!

Indonesia's PPE export ban forces raw material exporters to think twice. They used to rely on countries like Indonesia to process their materials. This regulation introduces supply chain risk -- the raw materials they send to Indonesia to be made into PPE might not come back intact. Better to make it yourself than take that risk. An Australian 3D printing company, 3DMEDiTech, [used to be unable to compete with countries like Indonesia on PPE costs because 3D printing was more expensive](https://www.abc.net.au/news/2020-04-14/inside-australias-race-to-prepare-for-the-worst-of-coronavirus/12140878?nw=0). Thanks to international *excess demand* (*partly thanks to countries banning exports!*), their PPE prices became competitive.

Not just Australia -- countries around the world have been repurposing their businesses to make masks and PPE. More expensive, sure, but clearly better than nothing. Governments in countries like Australia, China, and the United States [have helped in various ways to facilitate these business pivots](https://www.vox.com/the-goods/2020/4/6/21207135/factories-face-masks-ventilators-hand-sanitizer-coronavirus-manufacturing). Things like *cheap loans*, *purchasing guarantees*, and *active coordination* were deployed to help companies retool, purchase necessary equipment and materials, help companies estimate the business case for expansion, and *share know-how* along with standardization across domestic and even international agencies. I discussed this in [another post](https://imedkrisna.github.io/covin/).

Meanwhile, to the extent of my limited knowledge, measures beyond export bans, import facilitation, and standards relaxation don't appear to have been initiated by the Indonesian government. There are various efforts by the task force to increase *self-sufficiency* in COVID-19 goods. But who knows. The task force has the privilege of importing directly. So their *self-sufficiency* will likely still depend on imports. Not a bad thing -- just a little hypocritical.

## Looking ahead
By the end of June, the export ban will expire. Most likely, it won't be extended by the Ministry of Trade. The next thing to consider is how to export the PPE that has already been produced at competitive prices, meeting the standards recognized by the international market. With the new normal, PPE demand should increase sustainably, leaving room for our producers. What matters now is getting our PPE recognized internationally. Standards become even more important after the [controversy over Chinese PPE being rejected everywhere for not meeting standards](https://www.google.com/url?sa=t&source=web&rct=j&url=http://amp.abc.net.au/article/12105110&ved=2ahUKEwjurv6UoffpAhXv7HMBHcPpCe0QFjAAegQIBhAC&usg=AOvVaw3ZmZyZLff4mhzRTol_vSm2&ampcf=1). Especially now that these countries can already make PPE on their own in large quantities (though possibly still more expensive than *made in Indonesia*).

BTW, why hasn't there been any news about *faulty* PPE from China in Indonesia? We've received a lot of PPE from there. Hopefully there's no issue and I'm just overthinking.

Another option might be to rely on domestic demand. The Ministry of Health can refuse to buy, but perhaps grassroots fundraising can be directed here. Let us buy it ourselves, then donate it to hospitals. But bear in mind, hospitals might have their own standards too. The absence of demand-supply coordination is costly. Usually this is solved by institutions bridging *asymmetric information*, namely quality checkers -- in this case, the Ministry of Health. But the Ministry relaxed its own standards, so hospitals and suppliers have to communicate on their own. It may be too late now. Hopefully I'm wrong.

Without a solution, these PPE companies will have produced in vain. Costs already incurred may not generate revenue. The result? Companies close. Workers get fired. The economy underutilizes. Let's hope that when we return to the new normal, we still have enough companies and workers.

## Lessons from a public policy perspective
For those working in public policy or international trade, there is a valuable lesson here: policymaking is not as simple as flipping an *on-off* switch. Turn on barriers when you feel protection is needed, reduce them when you feel you need imports. Carelessly banning exports turns out to be not very useful: we still relied on PPE imports *even when* domestic producers could make them. Carelessly removing standards also produced goods whose quality was unacceptable to the Ministry of Health itself. This *on-off* approach has long been practiced by the Ministry of Trade to control prices of staple goods. It usually works. But COVID-19 is no ordinary phenomenon. The *on-off* approach is easier, but this time we need somewhat more creative policies. Something more sophisticated than *on-off*.

Another lesson: imports are not a bad thing. Just as I buy rice from farmers, Indonesia importing medical equipment is not something to be ashamed of. Using the rice analogy, rather than thinking "how do I grow my own rice," I prefer to think "how can I be useful to farmers so they'll sell me rice." Economic complexity is a source of prosperity. Cooperation across professions -- between farmers and non-farmers -- is actually beneficial. Indonesia has had enough experience with self-sufficiency experiments that have been wasteful and unsustainable.

What we should be thinking about is how to participate in the global economy. If we can't make medical equipment, what can we make? Indonesia has long contributed through commodities like oil (a long time ago), coal, and palm oil -- things that are easy to produce. There's still room to contribute in manufacturing, especially amid the world's need to diversify away from China. This also requires more creative policies than just *on-off*.

It's also somewhat funny when you think about it. What's wrong with other countries being able to make things we need? Are they not allowed to be useful and impressive? Only we get to be impressive? Anyway. Hopefully this serves as a good lesson for all of us.
