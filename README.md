# The World on Friday 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kainze29/news-image-20261120/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kainze29/news-image-20261120/reward.svg)](https://make.fun/c/news-image-20261120)

One front page, one day: Friday 20 November 2026, told in 50
stories. The masthead carries the date and a date check, the six
biggest stories of the day each get a photograph with a headline and
a short summary, stories 7 to 50 run as a numbered list below, and a
strip at the bottom places the day's turning points on a UTC timeline.
Every item on the page happened, or was first reported, on 20
November 2026. The page was built from the news reported in the
first hours of the day (up to about 01:30 UTC), so it covers the
morning's headlines: the cyclone bearing down on Odisha, the BBC's
report from besieged Taiz, and the day's early political and market
moves.

## The six top stories

1. **Cyclone Akvan bears down on Odisha.** Landfall is due near
   Gopalpur around noon IST, with 105,000 people evacuated and
   winds of 90-100 km/h.
2. **Inside besieged Taiz: "just fireworks".** The BBC speaks to
   seven people trapped in the Houthi-ringed Yemeni city, where
   more than 140 civilians have been killed since August.
3. **The EU to summon Russia's envoy over Kyiv.** After Russian
   strikes damaged the Austrian and Dutch embassies, Brussels calls
   in Moscow's ambassador.
4. **Malaysia: air force drug ring alarm.** Prime Minister Anwar
   Ibrahim says air force officers, pilots included, are suspected
   of smuggling drugs.
5. **Asian markets plunge: Nikkei -4.6%.** Tokyo and Seoul sink in
   Friday trade, the Kospi drops below 5,000, and global stocks
   head for their longest slide since September 2023.
6. **Phillips ton powers New Zealand to 317-6.** Glenn Phillips
   hits 118 and Henry Nicholls is 146 not out as New Zealand
   dominate India on day two in Wellington.

## Stories 7 to 50

Bapco plant nears full resumption; NATO chief meets intel chiefs;
Xi says ties with Moscow and the US are essential; the EU takes
Austria to court; Qatar foreign ministers discuss the Gulf by
phone; the Saudi crown prince and the Centcom chief talk defence;
the Gulf Railway is to link six nations; Merz sets terms for
Ukraine talks; Takaichi holds talks with Putin; Latvia plans a
De-Russification move; a US Senate leader hits Trump's "friend"
line on Putin; the EPPO charges a €213.7m rail fraud; three are
held in a Poland VAT probe; the EU pushes AI skills for pupils;
the US Justice Department issues 200+ subpoenas in the Alaska
probe; Bahrain says the Iran war is still a concern; the IEA says
the Iran conflict hits energy; Hegseth hails US-Colombia ties; the
UK is to get 1,000+ strike drones; the EU defers methane rules to
2029; Syrian families seek answers over ISIS detainees; Crimea
ferry services are to start; The Economist's World Ahead 2027
cover is out; MSCI Asia-Pacific falls 1.1%, a seventh day down;
global stocks are in their longest slide since 2023; ASX tech
stocks fall 3.9%; Modi opens the FICCI centenary meet; COP31
reaches its final day in Antalya; World Children's Day is marked;
the Centre announces new PUC rules; India signs a ₹1,976cr Barak
missile upgrade; India beat Malaysia in the Hong Kong Open;
the Women's Asian Hockey Trophy begins; the Rising Stars Asia Cup
begins in Doha; the UGC NET December schedule is out; UP Police
constable scores are out; APEC leaders talk trade in Shenzhen;
the NYT says Trump weighs more Iran strikes; gold $3,614 and
Brent $92.35 in early trade; Xi urges open trade at APEC; India
presses climate finance at COP31; Guterres says adaptation cash
is still short; a study says test-time compute lifts chip checks;
the December WTI oil contract expires.

## The day in UTC

00:13, the BBC publishes its report from besieged Taiz; 00:20,
Phillips completes his century as New Zealand reach 317-6 at
lunch; 00:33, gold $3,614 and Brent $92.35 in early trade; 00:59,
Anwar raises the alarm over air force drugs; 01:09, Hegseth hails
US-Colombia ties; 06:30, Cyclone Akvan landfall due near Gopalpur.

## Running it

`main.py` is Python 3.13, standard library only. It reads the
bundled `news.png`, checks it is a whole PNG under the 1 MiB limit
and no larger than 1024x1024 pixels, and writes it unchanged to
`entry.png` in the output directory. No network is used, so two runs
produce byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Contents

- `main.py` — the entry program described above
- `news.png` — the front page, 1024x1024 PNG, under 1 MiB
- `LICENSE` — MIT

The reporting behind each story comes from the BBC, Reuters, AP,
the India Meteorological Department, Bloomberg, Media Selangor,
the Financial Times and the outlets named on the page, all dated
20 November 2026.
