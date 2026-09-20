"""Figures for the currency-crisis lecture (EKI meeting 9).

Pulls from three key-free or key-light sources, caches every raw pull to
``data/raw/`` so the deck can be re-rendered offline, and writes DEN-styled
PNGs to ``figures/``.

    python scripts/make_figures.py            # build everything, use cache
    python scripts/make_figures.py --refresh  # force re-download
    python scripts/make_figures.py fig02 fig07  # build a subset

Sources
-------
BIS   Bank for International Settlements, WS_XRU (nominal exchange rates
      against USD) and WS_EER.  Public REST API, no key.
FRED  Federal Reserve Bank of St. Louis.  Needs $FRED_API_KEY.
WDI   World Bank World Development Indicators.  Public REST API, no key.

Exchange rates are kept throughout in *units of local currency per USD*, so
that a rising line always means a weakening currency.  Every figure keeps that
convention so students never have to re-orient themselves.
"""

from __future__ import annotations

import io
import os
import sys
import textwrap

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

import fig_den as den

# --------------------------------------------------------------------------
# paths and constants
# --------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RAW = os.path.join(ROOT, "data", "raw")
FIGS = os.path.join(ROOT, "figures")

os.makedirs(RAW, exist_ok=True)
os.makedirs(FIGS, exist_ok=True)

BIS_XRU = "https://stats.bis.org/api/v2/data/dataflow/BIS/WS_XRU/1.0"
WB_API = "https://api.worldbank.org/v2"
HEADERS = {"User-Agent": "Mozilla/5.0 (teaching materials; EKI FEB UI)"}

SLIDE_BG = "#f0f1eb"  # matches mytheme.scss so figures blend into the slide

REFRESH = False

# --------------------------------------------------------------------------
# fetch helpers — every one caches to data/raw/
# --------------------------------------------------------------------------


def _cache(name: str, fetch):
    """Return cached CSV if present, otherwise fetch, save and return it."""
    path = os.path.join(RAW, f"{name}.csv")
    if os.path.exists(path) and not REFRESH:
        return pd.read_csv(path)
    df = fetch()
    if df is None or df.empty:
        raise RuntimeError(f"fetch for '{name}' returned no rows")
    df.to_csv(path, index=False)
    print(f"    fetched {name}  ({len(df)} rows)")
    return df


def _to_period(s: pd.Series) -> pd.Series:
    """BIS TIME_PERIOD comes as 1996, 1996-01 or 1996-01-03."""
    return pd.to_datetime(s.astype(str), format="mixed")


def bis(freq: str, area: str, currency: str, start: str, end: str) -> pd.Series:
    """BIS nominal exchange rate, local currency per USD, indexed by date."""
    name = f"bis_{freq}_{area}_{currency}_{start}_{end}".replace("-", "")

    def fetch():
        url = f"{BIS_XRU}/{freq}.{area}.{currency}.A"
        r = requests.get(
            url,
            params={"startPeriod": start, "endPeriod": end, "format": "csv"},
            headers=HEADERS,
            timeout=180,
        )
        r.raise_for_status()
        df = pd.read_csv(io.StringIO(r.text))
        return df[["TIME_PERIOD", "OBS_VALUE"]]

    df = _cache(name, fetch)
    s = pd.Series(df["OBS_VALUE"].values, index=_to_period(df["TIME_PERIOD"]))
    return s.sort_index().dropna()


def bis_all_annual(start: str = "1970", end: str = "2025") -> pd.DataFrame:
    """Annual average USD rate for every currency BIS covers (long format)."""

    def fetch():
        r = requests.get(
            f"{BIS_XRU}/A...A",
            params={"startPeriod": start, "endPeriod": end, "format": "csv"},
            headers=HEADERS,
            timeout=600,
        )
        r.raise_for_status()
        df = pd.read_csv(io.StringIO(r.text))
        return df[["REF_AREA", "CURRENCY", "TIME_PERIOD", "OBS_VALUE"]]

    return _cache(f"bis_all_annual_{start}_{end}", fetch)


def fred(series_id: str) -> pd.Series:
    """One FRED series, indexed by date."""

    def fetch():
        key = os.environ.get("FRED_API_KEY")
        if not key:
            raise RuntimeError("FRED_API_KEY is not set in the environment")
        r = requests.get(
            "https://api.stlouisfed.org/fred/series/observations",
            params={"series_id": series_id, "api_key": key, "file_type": "json"},
            timeout=120,
        )
        r.raise_for_status()
        obs = r.json()["observations"]
        return pd.DataFrame(obs)[["date", "value"]]

    df = _cache(f"fred_{series_id}", fetch)
    s = pd.Series(
        pd.to_numeric(df["value"], errors="coerce").values,
        index=pd.to_datetime(df["date"]),
    )
    return s.sort_index().dropna()


def wdi(countries: str, indicator: str, start: int = 1970, end: int = 2025) -> pd.DataFrame:
    """World Bank indicator, wide format: index = year, columns = country code."""
    name = f"wdi_{countries.replace(';', '_')}_{indicator}"

    def fetch():
        r = requests.get(
            f"{WB_API}/country/{countries}/indicator/{indicator}",
            params={"format": "json", "per_page": 20000, "date": f"{start}:{end}"},
            timeout=180,
        )
        r.raise_for_status()
        payload = r.json()
        if len(payload) < 2 or payload[1] is None:
            raise RuntimeError(f"World Bank returned no data for {indicator}")
        rows = [
            {"iso3": x["countryiso3code"], "year": int(x["date"]), "value": x["value"]}
            for x in payload[1]
        ]
        return pd.DataFrame(rows)

    df = _cache(name, fetch)
    return df.pivot(index="year", columns="iso3", values="value").sort_index()


# --------------------------------------------------------------------------
# plotting helpers
# --------------------------------------------------------------------------


def new_fig(nrows=1, ncols=1, figsize=None):
    fig, axes = den.subplots(nrows, ncols, figsize=figsize)
    fig.patch.set_facecolor(SLIDE_BG)
    for ax in np.atleast_1d(axes).ravel():
        ax.set_facecolor(SLIDE_BG)
    return fig, axes


def finish(fig, filename):
    path = os.path.join(FIGS, filename)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  wrote figures/{filename}")


def legend_below(axes, ncol=4, y=-0.14, fontsize=10):
    """Merged legend under the plot area.

    den.legend_top anchors at 1.12, which collides with the axes title, so
    every figure here puts its legend below instead.
    """
    axes = list(np.atleast_1d(axes))
    handles, labels = [], []
    for a in axes:
        h, l = a.get_legend_handles_labels()
        handles.extend(h)
        labels.extend(l)
        if a.get_legend() is not None:
            a.get_legend().remove()
    axes[0].legend(handles, labels, ncol=ncol, frameon=False, fontsize=fontsize,
                   loc="upper center", bbox_to_anchor=(0.5, y))


def mark(ax, when, text, *, y=0.95, color=None, ha="left"):
    """Dated vertical marker with a short label."""
    color = color or den.DARK_GREY
    x = pd.Timestamp(when)
    ax.axvline(x, color=color, linestyle="--", linewidth=1.2, alpha=0.8)
    ax.annotate(
        text,
        xy=(x, y),
        xycoords=("data", "axes fraction"),
        fontsize=9,
        color=color,
        ha=ha,
        va="top",
        rotation=0,
        xytext=(4 if ha == "left" else -4, 0),
        textcoords="offset points",
    )


# --------------------------------------------------------------------------
# figures
# --------------------------------------------------------------------------


def fig01():
    """How often do currencies crash?  Frankel-Rose criterion on BIS data."""
    df = bis_all_annual()
    wide = df.pivot_table(
        index="TIME_PERIOD", columns="REF_AREA", values="OBS_VALUE", aggfunc="mean"
    ).sort_index()

    # depreciation against the USD, in per cent (rates are local per USD)
    dep = wide.pct_change() * 100
    # Frankel & Rose (1996): >=25 per cent depreciation, and at least 10
    # percentage points faster than the previous year's depreciation
    crash = (dep >= 25) & (dep - dep.shift(1) >= 10)
    counts = crash.sum(axis=1)
    counts = counts.loc[1971:2025]

    fig, ax = new_fig(figsize=(11.5, 4.8))
    ax.bar(counts.index, counts.values, color=den.DARK_BROWN, width=0.75)

    top = counts.max() * 1.42
    # (year, label, label height, horizontal alignment) — heights alternate so
    # neighbouring labels never collide
    episodes = [
        (1982, "Krisis utang\nAmerika Latin", 0.80, "right"),
        (1992, "ERM", 0.62, "right"),
        (1994, "Devaluasi\nfranc CFA", 0.94, "center"),
        (1998, "Krisis Asia", 0.72, "left"),
        (2009, "GFC", 0.42, "center"),
        (2022, "Pengetatan\nThe Fed", 0.72, "center"),
    ]
    for year, text, frac, ha in episodes:
        if year not in counts.index:
            continue
        ax.annotate(
            text,
            xy=(year, counts.loc[year] + 0.6),
            xytext=(year + (-1.5 if ha == "right" else 1.5 if ha == "left" else 0),
                    top * frac),
            ha=ha if ha != "right" else "right",
            fontsize=8.8,
            color=den.RED,
            fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=den.RED, lw=1.0,
                            shrinkA=2, shrinkB=2),
        )
    den.label(
        ax,
        title="Krisis nilai tukar bukan peristiwa langka",
        xlabel="Tahun",
        ylabel="Jumlah mata uang",
    )
    ax.set_ylim(0, top)
    ax.margins(x=0.01)
    finish(fig, "fig01_crisis_frequency.png")


def fig02():
    """The three places pressure shows up, for Indonesia 1995-2001.

    Replaces the old EMP index.  The index compressed three series into one
    number and hid the point: Indonesia did not defend by burning reserves, so
    pressure surfaced in the exchange rate and then in interest rates, never
    in reserves.  Three panels show that; one index cannot.
    """
    e = bis("M", "ID", "IDR", "1990-01", "2005-12")
    r = fred("TRESEGIDM052N")
    i_id = fred("IRSTCI01IDM156N")
    i_us = fred("FEDFUNDS")

    idx = pd.period_range("1995-01", "2001-12", freq="M").to_timestamp()
    m = lambda s: s.resample("MS").mean().reindex(idx)
    e, r, i_id, i_us = (m(s) for s in (e, r, i_id, i_us))
    diff = i_id - i_us

    fig, axes = new_fig(3, 1, figsize=(10.5, 7.4))
    ax1, ax2, ax3 = axes

    ax1.plot(e.index, e.values / 1000, color=den.DARK_BROWN, linewidth=2.2)
    den.label(ax1, title="Kurs: rupiah per USD (ribu)", xlabel="", ylabel="")

    ax2.plot(r.index, r.values / 1e3, color=den.SLATE_BLUE, linewidth=2.2)
    den.label(ax2, title="Cadangan devisa bruto (miliar USD)", xlabel="", ylabel="")

    ax3.plot(diff.index, diff.values, color=den.RED, linewidth=2.2)
    den.label(ax3, title="Diferensial suku bunga terhadap AS (poin persentase)",
              xlabel="", ylabel="")

    for ax in axes:
        for when in ("1997-08-14", "1998-01-15", "1998-05-21"):
            ax.axvline(pd.Timestamp(when), color=den.DARK_GREY,
                       linestyle="--", linewidth=1.1, alpha=0.75)
        ax.set_xlim(idx[0], idx[-1])
    ax1.annotate("14 Ags 1997\nband dilepas", xy=(pd.Timestamp("1997-08-14"), 0.92),
                 xycoords=("data", "axes fraction"), xytext=(-6, 0),
                 textcoords="offset points", ha="right", va="top",
                 fontsize=9, color=den.DARK_GREY)
    ax1.annotate("Mei 1998", xy=(pd.Timestamp("1998-05-21"), 0.40),
                 xycoords=("data", "axes fraction"), xytext=(6, 0),
                 textcoords="offset points", fontsize=9, color=den.DARK_GREY)

    fig.tight_layout()
    finish(fig, "fig02_tiga_komponen_tekanan.png")


def fig03():
    """First-generation schematic: reserves run down, attack comes early."""
    R0, mu, alpha = 100.0, 5.0, 4.0
    t_exhaust = R0 / mu          # 20: when reserves would hit zero with no attack
    t_attack = t_exhaust - alpha  # 16: when the shadow rate reaches the peg

    t = np.linspace(0, 26, 600)
    reserves = np.where(t < t_attack, R0 - mu * t, 0.0)
    naive = R0 - mu * t

    peg = 100.0
    slope = 3.0
    shadow = peg + slope * (t - t_attack)
    actual = np.where(t < t_attack, peg, shadow)

    fig, axes = new_fig(1, 2, figsize=(11.5, 4.4))
    ax1, ax2 = axes

    ax1.plot(t[naive >= 0], naive[naive >= 0], color=den.DARK_GREY,
             linestyle=":", linewidth=2, label="lintasan tanpa serangan")
    ax1.plot(t[t < t_attack], reserves[t < t_attack], color=den.DARK_BROWN,
             linewidth=2.6, label="cadangan devisa")
    ax1.plot(t[t >= t_attack], reserves[t >= t_attack], color=den.DARK_BROWN,
             linewidth=2.6)
    ax1.plot([t_attack, t_attack], [R0 - mu * t_attack, 0], color=den.RED,
             linewidth=2.6)
    ax1.scatter([t_attack], [R0 - mu * t_attack], color=den.RED, zorder=5, s=45)
    ax1.axvline(t_attack, color=den.RED, linestyle="--", linewidth=1, alpha=0.6)
    ax1.axvline(t_exhaust, color=den.DARK_GREY, linestyle="--", linewidth=1, alpha=0.6)
    ax1.annotate("serangan spekulatif:\ncadangan sisa habis seketika",
                 xy=(t_attack, 10), xytext=(-14, 26),
                 textcoords="offset points", ha="right", fontsize=9.5,
                 color=den.RED, fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=den.RED, lw=1.2))
    ax1.annotate("cadangan habis\n(jika tak diserang)", xy=(t_exhaust, 62),
                 xytext=(6, 0), textcoords="offset points", fontsize=9.5,
                 color=den.DARK_GREY)
    ax1.set_ylim(-6, 118)
    ax1.legend(loc="lower left", fontsize=9)
    den.label(ax1, title="Cadangan devisa", xlabel="Waktu", ylabel="Cadangan")

    ax2.plot(t, shadow, color=den.SLATE_BLUE, linestyle=":", linewidth=2,
             label="shadow exchange rate")
    ax2.axhline(peg, color=den.DARK_GREY, linewidth=1.4, alpha=0.7)
    ax2.plot(t, actual, color=den.DARK_BROWN, linewidth=2.8, label="kurs berlaku")
    ax2.scatter([t_attack], [peg], color=den.RED, zorder=5, s=45)
    ax2.axvline(t_attack, color=den.RED, linestyle="--", linewidth=1, alpha=0.6)
    ax2.annotate("peg", xy=(0.5, peg), xytext=(0, 6), textcoords="offset points",
                 fontsize=9.5, color=den.DARK_GREY)
    ax2.annotate("peg ditinggalkan\ntanpa lompatan kurs", xy=(t_attack, peg),
                 xytext=(10, -38), textcoords="offset points", fontsize=9.5,
                 color=den.RED, fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=den.RED, lw=1.2))
    ax2.set_ylim(peg - 52, peg + 34)
    ax2.legend(loc="upper left", fontsize=9)
    den.label(ax2, title="Kurs dan shadow rate", xlabel="Waktu",
              ylabel="Rupiah per dolar")

    for ax in axes:
        ax.set_xticks([t_attack, t_exhaust])
        ax.set_xticklabels([r"$t^{*}$", r"$t_{0}$"])
    finish(fig, "fig03_gen1_schematic.png")


def fig04():
    """Mexico 1994: peso and reserves."""
    fx = bis("D", "MX", "MXN", "1993-01", "1996-06")
    res = fred("TRESEGMXM052N").loc["1993-01":"1996-06"] / 1e3

    fig, ax = new_fig(figsize=(11, 4.8))
    ax.plot(fx.index, fx.values, color=den.DARK_BROWN, linewidth=2.2,
            label="Peso per USD (kiri)")
    ax2 = den.twinx(ax, ylabel="Cadangan devisa (miliar USD)")
    ax2.plot(res.index, res.values, color=den.SLATE_BLUE, linewidth=2.2,
             label="Cadangan devisa (kanan)")
    ax2.set_facecolor("none")

    mark(ax, "1994-03-23", "23 Mar 1994\nColosio dibunuh", y=0.99)
    # 20 and 22 December are two days apart: one marker, one label
    mark(ax, "1994-12-21", "20-22 Des 1994\nband dilebarkan,\nlalu peso mengambang",
         y=0.99)

    den.label(ax, title="Meksiko 1994: cadangan terkuras lebih dulu, kurs menyusul",
              xlabel="", ylabel="Peso per USD (naik = peso melemah)")
    legend_below([ax, ax2], ncol=2)
    finish(fig, "fig04_mexico_1994.png")


def fig05():
    """Second-generation schematic: three fundamental zones."""
    x = np.linspace(0, 30, 400)  # expected devaluation, per cent

    def defend_cost(level):
        return level + 0.09 * x ** 1.55

    abandon = 22.0
    # strong: defending is cheaper than abandoning even if everyone attacks
    # middle: cheaper only while expectations stay low  -> two equilibria
    # weak:   dearer than abandoning even with zero expected devaluation
    strong, middle, weak = 1.0, 9.0, 25.0

    fig, axes = new_fig(1, 3, figsize=(12.6, 4.4))
    titles = ["Fundamental kuat\npeg selalu bertahan",
              "Zona abu-abu\ndua ekuilibrium",
              "Fundamental lemah\npeg selalu jatuh"]
    for ax, level, title in zip(axes, [strong, middle, weak], titles):
        c = defend_cost(level)
        ax.plot(x, c, color=den.DARK_BROWN, linewidth=2.6,
                label="biaya mempertahankan peg")
        ax.axhline(abandon, color=den.RED, linewidth=2.2, linestyle="--",
                   label="biaya melepas peg")
        ax.fill_between(x, c, abandon, where=(c > abandon), color=den.RED,
                        alpha=0.12)
        ax.set_ylim(0, 62)
        ax.set_xlim(0, 30)
        ax.set_title(title, fontsize=10.5, fontweight="bold", pad=10)
        ax.set_xlabel("Ekspektasi devaluasi (%)")
        ax.set_yticks([])

    # the middle panel carries the whole point, so label both equilibria
    ax = axes[1]
    c = defend_cost(middle)
    xc = x[np.argmin(np.abs(c - abandon))]
    ax.axvline(xc, color=den.GOLD, linestyle=":", linewidth=1.4)
    ax.scatter([0], [defend_cost(middle)[0]], color=den.MUTED_TEAL, s=70, zorder=6)
    ax.scatter([30], [defend_cost(middle)[-1]], color=den.RED, s=70, zorder=6)
    ax.annotate("Ekuilibrium A\ntak ada yang menyerang,\nmembela peg murah",
                xy=(0.5, defend_cost(middle)[0]), xytext=(2.0, 40),
                fontsize=8.8, color=den.MUTED_TEAL, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=den.MUTED_TEAL, lw=1.1))
    ax.annotate("Ekuilibrium B\nsemua menyerang,\nmembela peg mahal",
                xy=(29.0, defend_cost(middle)[-1]), xytext=(11.5, 6),
                fontsize=8.8, color=den.RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=den.RED, lw=1.1))

    axes[0].set_ylabel("Biaya bagi pemerintah")
    axes[0].legend(loc="upper left", fontsize=8.5)
    finish(fig, "fig05_gen2_multiple_eq.png")


def fig06():
    """ERM 1992: sterling and the UK short rate."""
    fx = bis("D", "GB", "GBP", "1992-01", "1993-06")
    rate = fred("IRSTCI01GBM156N").loc["1992-01":"1993-06"]

    fig, axes = new_fig(2, 1, figsize=(10.5, 6.0))
    ax1, ax2 = axes
    ax1.plot(fx.index, fx.values, color=den.DARK_BROWN, linewidth=2.2)
    mark(ax1, "1992-09-16", "16 Sep 1992\nInggris keluar dari ERM", y=0.42)
    den.label(ax1, title="Poundsterling per USD (naik = pound melemah)",
              xlabel="", ylabel="GBP per USD")

    ax2.plot(rate.index, rate.values, color=den.SLATE_BLUE, linewidth=2.2,
             marker="o", markersize=3)
    mark(ax2, "1992-09-16", "", y=0.95)
    ax2.annotate(
        "Rata-rata bulanan menyembunyikan 16 September:\n"
        "suku bunga acuan 10% $\\rightarrow$ 12%, lalu 15% diumumkan,\n"
        "semuanya dalam satu hari sebelum peg dilepas",
        xy=(pd.Timestamp("1992-09-16"), 0.55), xycoords=("data", "axes fraction"),
        xytext=(-10, 0), textcoords="offset points", ha="right", va="center",
        fontsize=9, color=den.RED, fontweight="bold",
    )
    ax2.annotate(
        "setelah peg dilepas,\nbunga bebas dipangkas",
        xy=(pd.Timestamp("1993-02-01"), 0.30), xycoords=("data", "axes fraction"),
        fontsize=9, color=den.MUTED_TEAL, fontweight="bold",
    )
    den.label(ax2, title="Suku bunga pasar uang Inggris (rata-rata bulanan)",
              xlabel="", ylabel="% per tahun")

    # both panels must span the same dates or the comparison misleads
    for ax in axes:
        ax.set_xlim(pd.Timestamp("1992-01-01"), pd.Timestamp("1993-06-30"))
    fig.tight_layout()
    finish(fig, "fig06_erm_1992.png")


def fig07():
    """Asian currencies through 1997-98, indexed to 30 June 1997."""
    pairs = [("ID", "IDR", "Indonesia"), ("TH", "THB", "Thailand"),
             ("KR", "KRW", "Korea"), ("MY", "MYR", "Malaysia"),
             ("PH", "PHP", "Filipina")]
    series = {}
    for area, cur, name in pairs:
        s = bis("D", area, cur, "1996-01", "1999-12")
        base = s.loc[:"1997-06-30"].iloc[-1]
        series[name] = s / base * 100
    df = pd.DataFrame(series).sort_index()

    fig, ax = new_fig(figsize=(11, 5.0))
    colors = [den.RED, den.DEEP_AMBER, den.SLATE_BLUE, den.MUTED_TEAL, den.GOLD]
    for (name, col), c in zip(df.items(), colors):
        ax.plot(col.index, col.values, color=c, linewidth=2.2, label=name)
    ax.axhline(100, color=den.DARK_GREY, linewidth=1, alpha=0.6)
    mark(ax, "1997-07-02", "2 Jul 1997\nbaht mengambang", y=0.42, ha="right")
    mark(ax, "1997-08-14", "14 Ags 1997\nband rupiah dilepas", y=0.26)
    mark(ax, "1998-01-08", "Jan 1998\nLOI IMF kedua", y=0.99)
    den.label(
        ax,
        title="Krisis Asia 1997-98: indeks kurs terhadap USD (30 Juni 1997 = 100)",
        xlabel="",
        ylabel="Indeks (naik = mata uang melemah)",
    )
    legend_below(ax, ncol=5)
    finish(fig, "fig07_afc_fx.png")


def fig08():
    """Third-generation balance-sheet loop."""
    fig, ax = new_fig(figsize=(10.5, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.4)
    ax.axis("off")

    nodes = [
        (5.0, 5.6, "Rupiah terdepresiasi"),
        (8.5, 3.9, "Nilai rupiah dari\nutang valas melonjak"),
        (7.2, 1.3, "Kekayaan bersih &\nagunan perusahaan anjlok"),
        (2.8, 1.3, "Kredit dan investasi\nterhenti"),
        (1.5, 3.9, "Modal keluar,\npermintaan valas naik"),
    ]
    coords = []
    for x, y, text in nodes:
        box = FancyBboxPatch(
            (x - 1.32, y - 0.46), 2.64, 0.92,
            boxstyle="round,pad=0.06",
            linewidth=1.6, edgecolor=den.DARK_BROWN, facecolor="white",
        )
        ax.add_patch(box)
        ax.text(x, y, text, ha="center", va="center", fontsize=9.5,
                color=den.DARK_BROWN, fontweight="bold")
        coords.append((x, y))

    for i in range(len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % len(coords)]
        dx, dy = x2 - x1, y2 - y1
        norm = (dx ** 2 + dy ** 2) ** 0.5
        pad = 1.45
        start = (x1 + dx / norm * pad, y1 + dy / norm * pad * 0.55)
        end = (x2 - dx / norm * pad, y2 - dy / norm * pad * 0.55)
        ax.add_patch(FancyArrowPatch(
            start, end, connectionstyle="arc3,rad=-0.18",
            arrowstyle="-|>", mutation_scale=18,
            linewidth=2.0, color=den.RED,
        ))

    ax.text(5.0, 3.45, "lingkaran setan\nneraca", ha="center", va="center",
            fontsize=12, color=den.RED, fontweight="bold", style="italic")
    finish(fig, "fig08_gen3_loop.png")


def fig09():
    """Indonesian reserves against short-term external debt."""
    res = wdi("IDN", "FI.RES.TOTL.CD", 1990, 2000)["IDN"] / 1e9
    std = wdi("IDN", "DT.DOD.DSTC.CD", 1990, 2000)["IDN"] / 1e9
    df = pd.DataFrame({"Cadangan devisa": res, "Utang LN jangka pendek": std}).dropna()

    fig, ax = new_fig(figsize=(10.5, 4.8))
    width = 0.38
    xs = np.arange(len(df))
    ax.bar(xs - width / 2, df["Cadangan devisa"], width, color=den.SLATE_BLUE,
           label="Cadangan devisa")
    ax.bar(xs + width / 2, df["Utang LN jangka pendek"], width, color=den.RED,
           label="Utang luar negeri jangka pendek")
    ax.set_xticks(xs)
    ax.set_xticklabels(df.index)
    den.label(
        ax,
        title="Indonesia: cadangan devisa di bawah utang jangka pendek sepanjang 1990-1997",
        xlabel="",
        ylabel="Miliar USD",
    )
    legend_below(ax, ncol=2)
    finish(fig, "fig09_idn_reserves_debt.png")


def fig10():
    """Indonesian macro outcomes around 1998."""
    g = wdi("IDN", "NY.GDP.MKTP.KD.ZG", 1993, 2003)["IDN"]
    infl = wdi("IDN", "FP.CPI.TOTL.ZG", 1993, 2003)["IDN"]
    rate = fred("IRSTCI01IDM156N").loc["1993-01":"2003-12"]

    fig, axes = new_fig(1, 3, figsize=(12.4, 3.9))
    ax1, ax2, ax3 = axes

    cols = [den.RED if v < 0 else den.DARK_BROWN for v in g.values]
    ax1.bar(g.index, g.values, color=cols, width=0.72)
    ax1.axhline(0, color=den.DARK_GREY, linewidth=1)
    ax1.annotate(f"{g.loc[1998]:.1f}%".replace(".", ","), xy=(1998, g.loc[1998]), xytext=(0, -16),
                 textcoords="offset points", ha="center", fontsize=10,
                 color=den.RED, fontweight="bold")
    den.label(ax1, title="Pertumbuhan PDB riil", xlabel="", ylabel="% per tahun")

    ax2.bar(infl.index, infl.values, color=den.DEEP_AMBER, width=0.72)
    ax2.annotate(f"{infl.loc[1998]:.0f}%", xy=(1998, infl.loc[1998]), xytext=(0, 6),
                 textcoords="offset points", ha="center", fontsize=10,
                 color=den.RED, fontweight="bold")
    den.label(ax2, title="Inflasi (IHK)", xlabel="", ylabel="% per tahun")

    ax3.plot(rate.index, rate.values, color=den.SLATE_BLUE, linewidth=2.2)
    den.label(ax3, title="Suku bunga pasar uang", xlabel="", ylabel="% per tahun")

    for ax in (ax1, ax2):
        ax.set_xticks(range(1994, 2004, 3))
    fig.tight_layout()
    finish(fig, "fig10_idn_macro_1998.png")


def fig11():
    """Argentina 2001-02: the currency board breaks."""
    fx = bis("D", "AR", "ARS", "1999-01", "2003-12")
    res = fred("TRESEGARM052N").loc["1999-01":"2003-12"] / 1e3

    fig, ax = new_fig(figsize=(11, 4.8))
    ax.plot(fx.index, fx.values, color=den.DARK_BROWN, linewidth=2.2,
            label="Peso per USD (kiri)")
    ax2 = den.twinx(ax, ylabel="Cadangan devisa (miliar USD)")
    ax2.plot(res.index, res.values, color=den.SLATE_BLUE, linewidth=2.2,
             label="Cadangan devisa (kanan)")
    ax2.set_facecolor("none")

    ax.annotate("currency board 1 peso = 1 dolar", xy=(pd.Timestamp("1999-06-01"), 1.0),
                xytext=(0, 10), textcoords="offset points", fontsize=9.5,
                color=den.DARK_GREY, fontweight="bold")
    mark(ax, "2001-12-01", "corralito", y=0.92)
    mark(ax, "2002-01-06", "pesificación & default", y=0.78)

    den.label(ax, title="Argentina 1999-2003: dari currency board ke default",
              xlabel="", ylabel="Peso per USD (naik = peso melemah)")
    legend_below([ax, ax2], ncol=2)
    finish(fig, "fig11_argentina_2001.png")


def fig12():
    """Contemporary episodes, monthly, indexed to January 2018."""
    pairs = [("TR", "TRY", "Turki"), ("LK", "LKR", "Sri Lanka"),
             ("EG", "EGP", "Mesir"), ("ID", "IDR", "Indonesia")]
    series = {}
    for area, cur, name in pairs:
        s = bis("M", area, cur, "2018-01", "2026-06")
        series[name] = s / s.iloc[0] * 100
    df = pd.DataFrame(series).sort_index()

    fig, ax = new_fig(figsize=(11, 4.9))
    colors = [den.RED, den.DEEP_AMBER, den.MUTED_TEAL, den.SLATE_BLUE]
    for (name, col), c in zip(df.items(), colors):
        col = col.dropna()
        ax.plot(col.index, col.values, color=c, linewidth=2.3, label=name)
        ax.annotate(f"{col.iloc[-1]:.0f}", xy=(col.index[-1], col.iloc[-1]),
                    xytext=(5, 0), textcoords="offset points", fontsize=9.5,
                    color=c, fontweight="bold", va="center")
    ax.axhline(100, color=den.DARK_GREY, linewidth=1, alpha=0.6)
    ax.set_yscale("log")
    ax.set_yticks([100, 200, 400, 800, 1600])
    ax.set_yticklabels(["100", "200", "400", "800", "1.600"])
    den.label(
        ax,
        title="Episode kontemporer: indeks kurs terhadap USD (Januari 2018 = 100, skala log)",
        xlabel="",
        ylabel="Indeks (naik = mata uang melemah)",
    )
    legend_below(ax, ncol=4)
    finish(fig, "fig12_modern_episodes.png")


def fig13():
    """Greenspan-Guidotti ratio then and now."""
    # Korea and Malaysia have graduated from the World Bank Debtor Reporting
    # System, so DT.DOD.DSTC.CD is empty for them; use peers that still report.
    iso = "IDN;THA;PHL;TUR;MEX;IND"
    res = wdi(iso, "FI.RES.TOTL.CD", 1994, 2024)
    std = wdi(iso, "DT.DOD.DSTC.CD", 1994, 2024)
    ratio = (res / std).dropna(how="all")

    latest_year = int(ratio.dropna(how="all").index.max())
    names = {"IDN": "Indonesia", "THA": "Thailand", "PHL": "Filipina",
             "TUR": "Turki", "MEX": "Meksiko", "IND": "India"}
    rows = []
    for iso3, name in names.items():
        if iso3 not in ratio.columns:
            continue
        rows.append({
            "negara": name,
            "1996": ratio.loc[1996, iso3],
            str(latest_year): ratio.loc[latest_year, iso3],
        })
    df = pd.DataFrame(rows).dropna().sort_values("1996")

    fig, ax = new_fig(figsize=(10.5, 4.8))
    xs = np.arange(len(df))
    width = 0.38
    ax.bar(xs - width / 2, df["1996"], width, color=den.RED, label="1996")
    ax.bar(xs + width / 2, df[str(latest_year)], width, color=den.SLATE_BLUE,
           label=str(latest_year))
    ax.axhline(1.0, color=den.DARK_GREY, linestyle="--", linewidth=1.6)
    ax.annotate("aturan Greenspan-Guidotti: rasio = 1", xy=(-0.45, 1.0),
                xytext=(0, 7), textcoords="offset points", ha="left",
                fontsize=9.5, color=den.DARK_GREY, fontweight="bold")
    ax.set_xticks(xs)
    ax.set_xticklabels(df["negara"])
    den.label(
        ax,
        title="Cadangan devisa terhadap utang luar negeri jangka pendek",
        xlabel="",
        ylabel="Rasio",
    )
    legend_below(ax, ncol=2)
    finish(fig, "fig13_reserve_adequacy.png")


def fig14():
    """Rupiah and reserves since 2010."""
    fx = bis("M", "ID", "IDR", "2010-01", "2026-06") / 1000
    res = fred("TRESEGIDM052N").loc["2010-01":] / 1e3

    fig, ax = new_fig(figsize=(11, 4.8))
    # cyan is not in the fig-den palette; #0097A7 rather than pure cyan so the
    # line stays legible on the cream slide background
    ax.plot(fx.index, fx.values, color=den.RED, linewidth=2.2,
            label="Rupiah per USD (kiri, ribu)")
    ax2 = den.twinx(ax, ylabel="Cadangan devisa (miliar USD)")
    ax2.plot(res.index, res.values, color="#0097A7", linewidth=2.2,
             label="Cadangan devisa (kanan)")
    ax2.set_facecolor("none")

    mark(ax, "2013-05-22", "taper tantrum\n2013", y=0.16)
    mark(ax, "2020-03-01", "Covid-19", y=0.52)
    mark(ax, "2024-04-01", "tekanan 2024-25", y=0.92, ha="right")

    den.label(ax, title="Rupiah dan cadangan devisa sejak 2010",
              xlabel="", ylabel="Ribu rupiah per USD (naik = rupiah melemah)")
    legend_below([ax, ax2], ncol=2)
    finish(fig, "fig14_idr_recent.png")


# --------------------------------------------------------------------------
# runner
# --------------------------------------------------------------------------

FIGURES = {
    "fig01": fig01, "fig02": fig02, "fig03": fig03, "fig04": fig04,
    "fig05": fig05, "fig06": fig06, "fig07": fig07, "fig08": fig08,
    "fig09": fig09, "fig10": fig10, "fig11": fig11, "fig12": fig12,
    "fig13": fig13, "fig14": fig14,
}


def main(argv):
    global REFRESH
    args = [a for a in argv if a != "--refresh"]
    REFRESH = "--refresh" in argv

    den.style()
    wanted = args or list(FIGURES)
    failures = []
    for name in wanted:
        if name not in FIGURES:
            raise SystemExit(f"unknown figure '{name}'; choose from {list(FIGURES)}")
        print(f"[{name}]")
        try:
            FIGURES[name]()
        except Exception as exc:  # report every failure, do not fail silently
            failures.append((name, f"{type(exc).__name__}: {exc}"))
            print(f"  FAILED  {type(exc).__name__}: {exc}")

    print()
    if failures:
        print(f"{len(failures)} of {len(wanted)} figures failed:")
        for name, msg in failures:
            print(textwrap.indent(f"{name}  {msg}", "  "))
        return 1
    print(f"all {len(wanted)} figures written to {FIGS}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
