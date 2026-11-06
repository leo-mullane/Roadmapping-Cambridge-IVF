#!/usr/bin/env python3
"""Generates the quick-wins tab: one page per quick win, the overview and src/js/quick-wins.js.

Titles come from data/ideas.json (the phase 1 idea list) by idea number, so the model,
the findings page and the implementation guide always use the same names.
Edit this file and run it; don't edit the generated pages.

    python3 tools/quick_wins.py && node build-includes.js && node validate.js
"""
import json, os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'src', 'quick-wins')
IDEAS = {i['n']: i for i in json.load(open(os.path.join(ROOT, 'data', 'ideas.json')))}

THEMES = [
    ('costs', 'Costs and packages'),
    ('start', 'Getting started'),
    ('trust', 'Trust'),
    ('content', 'Content clean-up'),
    ('look', 'Look and findability'),
]
QW = []


def qw(idea, **k):
    k['idea'] = idea
    k['title'] = IDEAS[idea]['title'].replace("'", '’')
    QW.append(k)


HEAD_SITE = '<div class="cv-mock-head"><span class="logo">Cambridge IVF</span><span class="cv-mock-nav"><span>About us</span><span>Services</span><span>Prices</span><span>Referrals</span><span>Success rates</span><span>Contact us</span></span></div>'


def page(title, body, hero_cls=''):
    return f'{HEAD_SITE}<div class="cv-mock-hero {hero_cls}"><h2>{title}</h2></div><div class="cv-mock-body">{body}</div>'


# ---------------------------------------------------------------------------
# Costs and packages
# ---------------------------------------------------------------------------
qw(5, slug='pure-criteria', theme='costs',
   summary='Agree one set of PURE criteria with the clinical lead and make the prices page and the PURE page say the same thing.',
   url='cambridge-ivf.nhs.uk/prices/ and /services/fertility-treatments/pure-duo-ivf/',
   also='Also part of big improvement 1, Clear costs.',
   why='Two different sets of PURE criteria are live today. The prices page says 37 and under, AMH 6 to 35 and BMI below 35. The PURE page says under 38, AMH above 10, BMI below 30 and regular periods. Someone with an AMH of 8 and a BMI of 32 is eligible on one page and not on the other, and finds out which at a £220 consultation. It costs an hour of an editor’s time to fix, once someone decides which is right.',
   before_cap='The two pages disagree on AMH and BMI.',
   after_cap='Both pages show the same criteria, in the same words.',
   before='<div class="grid grid-2"><div class="cv-panel"><p class="cv-eyebrow">Prices page</p><p><b>Pure IVF package – £5,240</b></p><p>Criteria: 37 years of age and under, AMH of between <span class="cv-mark">6 – 35</span>, BMI <span class="cv-mark">below 35</span>, no severe uterine abnormalities…</p></div><div class="cv-panel"><p class="cv-eyebrow">PURE page</p><p><b>PURE Package – 1 cycle</b></p><p>The criteria for PURE is under 38 yrs old, AMH <span class="cv-mark">above 10</span>, BMI <span class="cv-mark">below 30</span>, <span class="cv-mark">regular periods</span>, if diagnosed with endometriosis then only mild…</p></div></div>',
   after='<div class="grid grid-2"><div class="cv-panel"><p class="cv-eyebrow">Prices page</p><p><b>PURE IVF · £5,240</b></p><p><b>Who it’s for:</b> 37 or under, AMH [agreed range], BMI [agreed limit]. Your consultant confirms.</p></div><div class="cv-panel"><p class="cv-eyebrow">PURE page</p><p><b>PURE IVF · £5,240</b></p><p><b>Who it’s for:</b> 37 or under, AMH [agreed range], BMI [agreed limit]. Your consultant confirms.</p></div></div>')

qw(6, slug='addon-ratings', theme='costs',
   summary='Show the HFEA’s traffic-light rating beside every optional add-on the clinic sells, with a line on why it might be suggested.',
   url='cambridge-ivf.nhs.uk/prices/',
   also='Also part of big improvement 1, Clear costs.',
   why='The prices page lists PICSI, Zymot, MACS, calcium ionophore, endometrial receptivity testing and DNA fragmentation testing without a word about the evidence. The HFEA rates PICSI and time-lapse imaging black (no effect on the chance of a baby for most patients), EmbryoGlue amber and endometrial receptivity testing red. An NHS clinic is the place patients would expect to be told this. It may trim some add-on sales; it also protects the clinic from complaints and gives it something private rivals are reluctant to copy.',
   before_cap='Add-ons listed with prices only, repeated under each package.',
   after_cap='Each add-on carries the HFEA rating and a plain explanation.',
   before='<p><b>Additional Services for Pure:</b><br>ICSI - £1,323<br>PICSI &amp; Zymot - £245 &amp; £150 (in addition to ICSI fee)<br>MACS ICSI - £1,683<br>MACS ICSI (completed at elsewhere) £2,025<br>Vitrification (freezing embryos and one years storage) - £765<br>Calcium Ionophore - £127</p><p class="cv-muted">…and the same list again under PURE Duo, IVF Plus, IVF Plus Duo, Multi-Cycle, three Shared Motherhood packages and DuoStim.</p>',
   after='<table class="cv-table"><thead><tr><th>Add-on</th><th>Price</th><th>HFEA rating</th></tr></thead><tbody><tr><td>EmbryoScope time-lapse</td><td>Included</td><td><span class="hfea black">Black: no effect</span></td></tr><tr><td>EmbryoGlue</td><td>Included</td><td><span class="hfea amber">Amber: conflicting evidence</span></td></tr><tr><td>PICSI and Zymot</td><td>£245 and £150</td><td><span class="hfea black">Black: no effect</span></td></tr><tr><td>Endometrial receptivity test</td><td>£1,308</td><td><span class="hfea red">Red: may reduce success</span></td></tr><tr><td>DNA fragmentation test</td><td>£462</td><td><span class="hfea grey">Grey: not enough evidence</span></td></tr></tbody></table><p class="cv-small" style="margin-top:0.75rem">We’ll only suggest an add-on when there’s a reason it may help you. <a href="#">What the HFEA ratings mean</a></p>')

qw(8, slug='staged-payments', theme='costs',
   summary='Put “pay for cycle 1 now, later cycles only if you need them” at the top of the Duo and Multi-Cycle pages, with the amounts.',
   url='cambridge-ivf.nhs.uk/services/fertility-treatments/multi-cycle-ivf/',
   also='Also part of big improvement 1, Clear costs.',
   why='Staged payment is a real advantage: Multi-Cycle is £11,540 in total but £8,390 to start, and nobody pays for cycles they don’t use. Today it’s mentioned in one sentence at the top of the prices page and not at all at the top of the package pages. Leading with it makes the higher-value packages feel less daunting, at no cost beyond an editor’s afternoon.',
   before_cap='The page opens with what’s included. The payment structure isn’t mentioned.',
   after_cap='The first thing you see is what you pay, and when.',
   before=page('Multi-cycle IVF', '<p>Multi-cycle IVF includes 3 cycles of IVF and is an all-inclusive fixed price package - please see details of what is included below.</p><p>Multi-cycle IVF is led by highly experienced NHS consultants. It includes three cycles of IVF treatment, medication up to pregnancy testing (except Lubion), HFEA fee, monitoring scans and blood tests…</p>'),
   after=page('Multi-cycle IVF', '<div class="cv-panel soft"><p class="cv-eyebrow">Three cycles for £11,540, paid as you go</p><ul class="cv-steps-pay"><li><span>Before cycle 1</span><b>£8,390</b></li><li><span>Cycle 2, only if you need it</span><b>£1,575</b></li><li><span>Cycle 3, only if you need it</span><b>£1,575</b></li></ul></div><p style="margin-top:1rem">Multi-cycle IVF includes three cycles of IVF, all-inclusive and fixed price…</p>'))

qw(32, slug='tidy-prices', theme='costs',
   summary='Correct the typos on the prices page, show the add-ons once in their own table and check the gamete transport fees.',
   url='cambridge-ivf.nhs.uk/prices/',
   also='',
   why='The prices page is the one people read most carefully, and it has “chalmydia”, “IICSI”, “Human and Fertilisation (HFEA)” and “pregnancy scan.pregnancy scan.” The add-on list is repeated under nearly every package. Transporting gametes overseas costs £330, or £300 with a special export directive, which may be right but looks like a mistake. Small things, but on a page asking for several thousand pounds they make people wonder what else is wrong.',
   before_cap='Typos and a fee that looks the wrong way round.',
   after_cap='Corrected copy, and the transport fees flagged for checking.',
   before='<p>Includes: Medication up to pregnancy testing (except Lubion), virals &amp; <span class="cv-mark">chalmydia</span>…</p><p>…the compulsory <span class="cv-mark">Human and Fertilisation (HFEA)</span> license fee…</p><p>Additional Services that may be required: <span class="cv-mark">IICSI</span> - £1,323</p><p>…review appointment or early <span class="cv-mark">pregnancy scan.pregnancy scan.</span></p><p>Transport of gametes to overseas clinic - £330<br>Transport of gametes to overseas clinic (including special export directive) - <span class="cv-mark">£300</span></p>',
   after='<p>Includes: medication up to the pregnancy test (except Lubion), viral and chlamydia screening…</p><p>…the Human Fertilisation and Embryology Authority (HFEA) licence fee…</p><p>Add-ons: see <a href="#">add-ons and the evidence</a>, listed once for all packages.</p><p>…review appointment or early pregnancy scan.</p><p>Transport of gametes to an overseas clinic: £330<br>With a special export direction: [fee to be confirmed]</p>')

# ---------------------------------------------------------------------------
# Getting started
# ---------------------------------------------------------------------------
qw(11, slug='session-dates', theme='start',
   summary='Show the next information session dates on the homepage and key service pages, with booking on the page.',
   url='cambridge-ivf.nhs.uk',
   also='Also part of big improvement 3, Start today.',
   why='The free information session is the clinic’s best way in: fifteen minutes each with an embryologist, a nurse and the finance manager. The homepage has a “Book a free Information Session” button but no date, and booking happens on a separate site. Herts & Essex shows its next open evening date on its homepage; Bourn Hall runs an open evening in Cambridge. A date gives people a reason to act this week rather than “sometime”.',
   before_cap='A button, no dates, and booking on another site.',
   after_cap='The next three dates, booked on the page.',
   before=HEAD_SITE + '<div class="cv-mock-hero"><h2>Your Dreams, Your Choices, Your Future.</h2><p style="margin:1rem 0">We are here to help you create the family of your dreams, either now or in the future…</p><span class="btn">Book a free Information Session</span><p class="cv-small" style="margin-top:0.5rem">Opens trybooking.com in a new tab</p></div>',
   after=HEAD_SITE + '<div class="cv-mock-hero"><h2>Your Dreams, Your Choices, Your Future.</h2><p style="margin:1rem 0">We are here to help you create the family of your dreams, either now or in the future…</p></div><div class="cv-mock-body" style="max-width:none"><h3>Free information sessions</h3><ul class="cv-sessions"><li class="cv-session"><div class="d">Tue<b>[10]</b>[Nov]</div><div><b>By phone, evening</b><br><span class="cv-muted">Embryologist, nurse and finance manager</span></div><span class="btn">Book</span></li><li class="cv-session"><div class="d">Tue<b>[17]</b>[Nov]</div><div><b>By phone, evening</b><br><span class="cv-muted">Embryologist, nurse and finance manager</span></div><span class="btn">Book</span></li><li class="cv-session"><div class="d">Tue<b>[24]</b>[Nov]</div><div><b>By phone, evening</b><br><span class="cv-muted">Embryologist, nurse and finance manager</span></div><span class="btn">Book</span></li></ul></div>')

qw(12, slug='sticky-bar', theme='start',
   summary='A slim bar at the bottom of the screen on phones with Call, Information session and Enquire, on service, price and package pages.',
   url='cambridge-ivf.nhs.uk/prices/ on a phone',
   also='Also part of big improvement 3, Start today.',
   why='On a phone the prices page is about 8,000 pixels long and has no call to action above the fold. People make up their minds while reading the long pages, and at that moment the next step is several screens away. A sticky bar is a small template change for the CUH web team.',
   before_cap='No way to act without scrolling back to the top or the bottom.',
   after_cap='The next step stays one tap away.',
   before='<div class="phone"><div class="phone-screen"><div class="cv-mock-head"><span class="logo">Cambridge IVF</span><span>Menu</span></div><div style="padding:1rem"><h3>Prices</h3><p class="cv-small">Working out how much you may need to pay isn’t always easy…</p><div class="wf-placeholder" style="height:180px">Accordions</div><p class="cv-small" style="margin-top:0.75rem">34 more sections below</p></div></div></div>',
   after='<div class="phone"><div class="phone-screen" style="position:relative"><div class="cv-mock-head"><span class="logo">Cambridge IVF</span><span>Menu</span></div><div style="padding:1rem;flex:1"><h3>Prices</h3><p class="cv-small">Working out how much you may need to pay isn’t always easy…</p><div class="wf-placeholder" style="height:180px">Accordions</div></div><div style="display:flex;gap:0.4rem;padding:0.5rem;border-top:1px solid var(--wf-border-strong)"><span class="btn btn-secondary btn-sm" style="flex:1;text-align:center">Call</span><span class="btn btn-secondary btn-sm" style="flex:1;text-align:center">Info session</span><span class="btn btn-sm" style="flex:1;text-align:center">Enquire</span></div></div></div>')

qw(13, slug='measure', theme='start',
   summary='Turn on GA4 events for phone and email taps, information session bookings and price-list downloads, and send a one-page report each month.',
   url='Google Analytics 4 (already installed)',
   also='Underpins every other change: it’s how you know which ones paid back.',
   why='GA4 and Google Tag Manager are already on the site, but there are no forms to measure and we saw no sign of events on phone numbers, email links, the TryBooking link or the PDF price lists. Without them, nobody can say how many people the website sends to the clinic, or whether a change helped. Setting up the events is a few hours in Tag Manager; the report is a template someone fills in monthly.',
   before_cap='Page views only.',
   after_cap='A monthly report of the actions that lead to patients.',
   before='<div class="cv-report"><div class="cv-stat"><b>[n]</b>Page views</div><div class="cv-stat"><b>[n]</b>Users</div><div class="cv-stat"><b>?</b>Enquiries</div><div class="cv-stat"><b>?</b>Sessions booked</div></div><p class="cv-muted" style="margin-top:1rem">Which pages lead to a call? Nobody knows.</p>',
   after='<h3>Website report: [month]</h3><div class="cv-report"><div class="cv-stat"><b>[n]</b>Phone taps</div><div class="cv-stat"><b>[n]</b>Emails started</div><div class="cv-stat"><b>[n]</b>Information session clicks</div><div class="cv-stat"><b>[n]</b>Price list downloads</div></div><table class="cv-table" style="margin-top:1rem"><thead><tr><th>Page</th><th>Visits</th><th>Actions</th><th>Rate</th></tr></thead><tbody><tr><td>Prices</td><td>[n]</td><td>[n]</td><td>[%]</td></tr><tr><td>PURE IVF</td><td>[n]</td><td>[n]</td><td>[%]</td></tr><tr><td>Egg freezing</td><td>[n]</td><td>[n]</td><td>[%]</td></tr></tbody></table>')

qw(28, slug='nhs-funding', theme='start',
   summary='Replace the CCG-era copy with the current ICB position, a short eligibility summary and a clear self-funded route for people who don’t qualify.',
   url='cambridge-ivf.nhs.uk/referrals/self-funded-referrals/',
   also='Also part of big improvement 2, Find your path.',
   why='The page says Cambridge and Peterborough CCG “have recently announced” that NHS IVF is returning and that details will be “added here as soon as they are available”. CCGs were replaced by integrated care boards in July 2022. People who discover they aren’t NHS-eligible are the clinic’s next self-funded patients, if the page catches them with an alternative rather than a dead end.',
   before_cap='Out-of-date funding news and no alternative.',
   after_cap='Who funds what today, and what to do if you’re not eligible.',
   before=page('NHS / Self-funded referrals', '<p>Cambridge IVF accepts self-funded patients from anywhere and NHS funded patients from the East of England, Hertfordshire and West Essex. <span class="cv-mark">Cambridge and Peterborough CCG have recently announced that they are to re-introduce NHS funded IVF – further details regarding eligibility criteria to be added here as soon as they are available.</span></p>'),
   after=page('NHS-funded and self-funded treatment', '<p>NHS funding for IVF is decided by the integrated care board (ICB) for the area where your GP is.</p><table class="cv-table"><thead><tr><th>Your GP is in</th><th>NHS IVF</th></tr></thead><tbody><tr><td>Cambridgeshire and Peterborough</td><td>[Current criteria and link]</td></tr><tr><td>Hertfordshire and West Essex</td><td>[Current criteria and link]</td></tr><tr><td>Suffolk and North East Essex</td><td>[Current criteria and link]</td></tr></tbody></table><div class="cv-panel soft" style="margin-top:1rem"><b>Not eligible?</b> Self-funded IVF starts at £2,900. <a href="#">See packages and prices</a></div>'))

qw(41, slug='switching', theme='start',
   summary='Explain how to move treatment to Cambridge IVF: records to bring, transferring eggs or embryos, the fee and a dedicated enquiry route.',
   url='cambridge-ivf.nhs.uk/your-journey/started-treatment-elsewhere/',
   also='Also part of big improvement 2, Find your path.',
   why='People who are unhappy with another clinic are already self-funding and ready to start, which makes them some of the most valuable visitors the site gets. Today’s page is five sentences and a “click here”. A clear checklist and an enquiry route would win some of them with copy alone.',
   before_cap='A few sentences and a “click here”.',
   after_cap='A short checklist and a clear next step.',
   before=page('Started treatment elsewhere?', '<p>At Cambridge IVF we are able to provide treatment for those who have already begun their journey somewhere else and are looking for a new provider.</p><p>Whatever the reason may be, we’re happy to talk to you… If you’re ready to start you journey with us, then <u>click here</u> to find out how you can get referred.</p>'),
   after=page('Moving your treatment to us', '<p>Moving clinics is more common than people think, and it’s straightforward.</p><ol class="cv-list"><li>Send us your records: previous cycles, test results and any letters.</li><li>Book a review consultation (£220) to agree a plan.</li><li>If you have frozen eggs or embryos, we arrange the transfer with your current clinic.</li></ol><div class="row" style="margin-top:1rem"><span class="btn">Tell us about your treatment so far</span></div>'))

# ---------------------------------------------------------------------------
# Trust
# ---------------------------------------------------------------------------
qw(24, slug='hfea-rating', theme='trust',
   summary='Ask every patient at their review appointment to rate the clinic on the HFEA site, with a card, a QR code and a follow-up email.',
   url='hfea.gov.uk clinic profile',
   also='Also part of big improvement 4, Proof you can trust.',
   why='The HFEA profile shows a 5 out of 5 inspection rating and a 2 out of 5 patient rating from only 22 people, and it appears on every clinic search and comparison on the HFEA site. With so few ratings, a few dozen more from ordinary, satisfied patients would move the score. This may be the cheapest revenue lever on the whole list: a printed card and a line in an email.',
   before_cap='22 ratings. Nobody is asked.',
   after_cap='Every patient is asked, in person and by email.',
   before='<div class="cv-panel" style="max-width:420px"><p class="cv-eyebrow">HFEA: Cambridge IVF</p><p>Inspection rating <b>5 / 5</b></p><p>Patient rating <b>2 / 5</b> based on 22 ratings</p></div>',
   after='<div class="grid grid-2"><div class="cv-card-qr"><span class="wf-placeholder ratio-1-1">QR code</span><div><b>How was your care?</b><p class="cv-small">Scan to rate us on the HFEA website. It takes two minutes and helps others choose.</p></div></div><div class="cv-panel"><p class="cv-eyebrow">Follow-up email, one week later</p><p>Thank you for choosing Cambridge IVF. Whatever happened, would you tell others what it was like? <a href="#">Rate us on the HFEA website</a></p></div></div>')

qw(26, slug='why-nhs', theme='trust',
   summary='A short “Why an NHS clinic?” section on the homepage and why-choose page, with four concrete reasons.',
   url='cambridge-ivf.nhs.uk/about-us/why-choose-cambridge-ivf/',
   also='Also part of big improvement 4, Proof you can trust.',
   why='Care through to the Rosie, access to CUH genetics, counselling within two weeks and income reinvested in CUH’s women’s and children’s services are all true and all on the site, spread across five pages. It’s the one thing private rivals can’t claim. Pulling it into four lines on the homepage costs nothing.',
   before_cap='The NHS story is scattered across five pages.',
   after_cap='Four reasons, in one place.',
   before=page('Why Cambridge IVF?', '<p>Cambridge IVF is not just another fertility clinic. We are an assisted conception unit, backed by some of the world’s most advanced medical research and offering a unique journey for each family in our care. Whatever your situation, we are here for you…</p>'),
   after=page('Why Cambridge IVF?', '<div class="cv-proof4"><div class="card"><b>Care that carries on</b><p class="card-text">From first scan to the Rosie maternity hospital.</p></div><div class="card"><b>Specialists on hand</b><p class="card-text">CUH genetics, the regional centre.</p></div><div class="card"><b>Support when you need it</b><p class="card-text">Counselling within two weeks.</p></div><div class="card"><b>Money stays in the NHS</b><p class="card-text">Reinvested in CUH women’s and children’s services.</p></div></div>'))

qw(22, slug='heritage-date', theme='trust',
   summary='Use one line about the clinic’s history everywhere: licensed by the HFEA since 1992, at Kefford House since 2011.',
   url='cambridge-ivf.nhs.uk/success-rates/, PURE page, health professionals page',
   also='',
   why='One page says the clinic’s IVF experience dates back to 1992, another says 1994, and a third says it was set up in 2011 and builds on 20 years. The HFEA says licensed since 1992. Ten minutes of editing, and one fewer reason to doubt the rest.',
   before_cap='Three versions of the same fact.',
   after_cap='One version, everywhere.',
   before='<ul class="cv-list"><li>Success rates: “Our IVF experience dates back to <span class="cv-mark">1992</span>”</li><li>PURE IVF: “Our IVF experience dates back to <span class="cv-mark">1994</span>”</li><li>Health professionals: “Set up in <span class="cv-mark">2011</span>, Cambridge IVF builds on <span class="cv-mark">20 years</span>…”</li></ul>',
   after='<ul class="cv-list"><li>Success rates: “Licensed by the HFEA since 1992; at Kefford House since 2011.”</li><li>PURE IVF: “Licensed by the HFEA since 1992; at Kefford House since 2011.”</li><li>Health professionals: “Licensed by the HFEA since 1992; at Kefford House since 2011.”</li></ul>')

# ---------------------------------------------------------------------------
# Content clean-up
# ---------------------------------------------------------------------------
qw(17, slug='broken-links', theme='content',
   summary='Remove “Early pregnancy and Coronavirus” from the menu and give “Your journey” a real page or a working link.',
   url='cambridge-ivf.nhs.uk/your-journey/',
   also='',
   why='Two links in the main menu go to “Page not found”: the “Your journey” section and “Early pregnancy and Coronavirus”. Broken links in the main menu are a small thing that undermines a clinic asking people for several thousand pounds. It’s ten minutes in the menu settings.',
   before_cap='Two main-menu links lead here.',
   after_cap='The coronavirus link is gone; Your journey goes somewhere useful.',
   before=HEAD_SITE + '<div class="cv-404"><b>404</b><h2>Page not found</h2><p>Please check the web address to make sure it was correct.</p></div>',
   after=HEAD_SITE + '<div class="cv-mock-body"><p class="cv-eyebrow">Your journey</p><h2>What happens, step by step</h2><ol class="cv-list"><li>Get in touch</li><li>Fertility assessment</li><li>Consultation and plan</li><li>Getting ready</li><li>Your treatment cycle</li><li>Embryo transfer</li><li>Pregnancy test</li><li>Early pregnancy and the Rosie</li></ol></div>')

qw(29, slug='postcode-lottery', theme='content',
   summary='Remove the “Postcode lottery” section or replace it with a short, current explanation of NHS funding.',
   url='cambridge-ivf.nhs.uk/your-journey/sources-of-support/',
   also='',
   why='The section cites “36 of 209 CCG’s”, asks readers to contact “Jane Ellison, the Minister for Public Health” and links to a closed e-petition. CCGs no longer exist and the minister left the post years ago. Dated politics on a clinical site makes everything around it look dated too.',
   before_cap='Out-of-date campaign copy.',
   after_cap='A short, current note with a link to the patient charity.',
   before=page('Postcode lottery', '<p>The postcode lottery for fertility treatment continues to be a major problem within the UK, with only <span class="cv-mark">36 of 209 CCG’s</span> (Clinical Commissioning Groups) offering the 3 cycles recommended by NICE.</p><p>Sign the <span class="cv-mark">e-petition</span> for equal funding across the UK. Contact your MP or <span class="cv-mark">Jane Ellison, the Minister for Public Health</span>…</p>'),
   after=page('NHS funding varies by area', '<p>NHS funding for IVF is decided locally, so what’s offered depends on where your GP is. <a href="#">Check what your area funds</a>.</p><p>Fertility Network UK campaigns for fair access and offers support whatever your situation. <a href="#">Visit Fertility Network UK</a></p>'))

qw(30, slug='legacy-links', theme='content',
   summary='Replace links to the old cambridge-ivf.org.uk domain and the Outlook “safelinks” on the feedback page with direct links.',
   url='cambridge-ivf.nhs.uk/contact-us/feedback/',
   also='',
   why='The egg freezing and health professionals pages still link to the old domain. The feedback page’s links to the HFEA, the GMC and the NMC are wrapped in Outlook safelinks that include a member of staff’s email address, presumably pasted from an email. That’s a small privacy slip as well as untidy. Fixing it, and adding a broken-link check to a monthly routine, is an hour’s work.',
   before_cap='Links pasted from an email, staff address included.',
   after_cap='Plain links to the right places.',
   before='<p>Complaints about a fertility clinic can be made to the HFEA:</p><p class="cv-small" style="word-break:break-all">https://gbr01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.hfea.gov.uk%2Fcontact-us%2F&amp;data=05%7C01%7C<span class="cv-mark">[staff.name]%40nhs.net</span>%7C…</p><p>Prices | Cambridge IVF (<span class="cv-mark">cambridge-ivf.org.uk</span>)</p>',
   after='<p>Complaints about a fertility clinic can be made to the HFEA:</p><p><a href="#">HFEA: making a complaint about a fertility clinic</a></p><p><a href="#">Prices</a></p>')

qw(31, slug='non-urgent', theme='content',
   summary='Use plain headings on the support information page instead of the NHS “Non-urgent advice” card, and link to the lab page rather than repeating it.',
   url='cambridge-ivf.nhs.uk/about-us/support-information/',
   also='',
   why='The support information page is about 41,000 characters long and labels every section “Non-urgent advice”, including the glossary and a list of useful websites. On NHS sites that label means something specific about when to seek care. The page also repeats the whole “What happens in the lab?” page. Plain headings and a link would make it shorter and clearer.',
   before_cap='Everything is “Non-urgent advice”.',
   after_cap='Plain sections, and a link instead of a copy.',
   before='<div class="cv-panel" style="border-top:6px solid var(--wf-text)"><p class="cv-eyebrow">Non-urgent advice: Glossary of terms</p><p>A · B · C · D …</p></div><div class="cv-panel" style="border-top:6px solid var(--wf-text);margin-top:0.75rem"><p class="cv-eyebrow">Non-urgent advice: Useful websites</p><p>BICA · British Fertility Society · ESHRE · NICE · HFEA</p></div><div class="cv-panel" style="border-top:6px solid var(--wf-text);margin-top:0.75rem"><p class="cv-eyebrow">What happens in the lab?</p><p>[The whole lab page, repeated]</p></div>',
   after='<h3>Glossary of terms</h3><p>A · B · C · D …</p><h3>Useful websites</h3><p>BICA · British Fertility Society · ESHRE · NICE · HFEA</p><h3>What happens in the lab</h3><p><a href="#">Read about what happens to your eggs and embryos in the lab</a></p>')

qw(33, slug='under-development', theme='content',
   summary='Finish or remove the “this page is currently under development” notes, and group leaflets by stage of treatment.',
   url='cambridge-ivf.nhs.uk/services/patient-information-leaflets/',
   also='',
   why='The services page and the patient information leaflets page both say they’re under development. The leaflets page lists files with version numbers in their names (“v1.0”, “v3.2”). Removing the notice and grouping leaflets under headings such as “Before treatment” and “Donors” is an editor’s afternoon.',
   before_cap='“Under development” and an alphabetical list of files.',
   after_cap='Grouped by when you’ll need them.',
   before=page('Patient Information Leaflets', '<p>On this page you will find all Cambridge IVF Patient Information Leaflets. <span class="cv-mark">Please note, this page is currently under development.</span></p><ul class="cv-list"><li>Approved Suppliers of Donor Eggs for Treatment at Cambridge IVF v3.0</li><li>Artificial Oocyte Activation Information for Patient v1.2</li><li>CIVF MicroTESE Sperm retrieval - Information for patients v1.0</li><li>CMV Patient Information v3.0</li><li>…</li></ul>'),
   after=page('Patient information leaflets', '<h3>Before treatment</h3><ul class="cv-list"><li>CMV and your treatment</li><li>Diagnostic semen analysis</li></ul><h3>During treatment</h3><ul class="cv-list"><li>Artificial egg activation</li><li>Embryo freezing</li></ul><h3>Donors</h3><ul class="cv-list"><li>Approved suppliers of donor eggs</li><li>Using donor eggs</li></ul>'))

qw(34, slug='egg-bank-topic', theme='content',
   summary='Move the semen-quality advice from the donor egg page to an andrology page, and drop the supplement brand.',
   url='cambridge-ivf.nhs.uk/services/donor-services/donor-egg-bank-service-uk/',
   also='',
   why='The donor egg bank page includes several paragraphs on improving semen quality, ending with a recommendation of a named commercial supplement. It’s in the wrong place, and an NHS page appearing to endorse a product is a small reputational risk. Moving the advice and removing the brand takes minutes.',
   before_cap='Semen advice, and a supplement brand, on the egg bank page.',
   after_cap='The egg bank page sticks to donor eggs; the advice moves to andrology, without the brand.',
   before=page('Donor egg bank', '<h3>Availability of donor eggs</h3><p>…Men need to do what they can to improve their semen quality… Taking a fertility supplement that contains zinc and selenium… may be beneficial, <span class="cv-mark">Such as [brand name]</span>.</p><h3>Is there a waiting list for this service?</h3><p>…allow at least three to four months…</p>'),
   after=page('Donor egg bank', '<h3>Availability of donor eggs</h3><p>[Donor egg availability.]</p><h3>Is there a waiting list for this service?</h3><p>Allow at least three to four months from your first appointment to starting treatment.</p><p class="cv-small">Looking for advice on sperm health? <a href="#">Read our andrology guidance</a></p>'))

qw(35, slug='pregnancy-care', theme='content',
   summary='Lead the pregnancy care page with what joined-up care means for a patient, not the Rosie’s opening in 2013.',
   url='cambridge-ivf.nhs.uk/your-journey/pregnancy-care/',
   also='',
   why='Care that continues from IVF into one of the country’s biggest maternity hospitals is a genuine advantage. The page that explains it closes on a royal visit in May 2013 and a multi-million pound extension. Rewriting it around the patient (early scan, handover, specialist services) turns a dated page into a reason to choose the clinic.',
   before_cap='History of the Rosie building.',
   after_cap='What happens to you after a positive test.',
   before=page('Pregnancy care', '<p>The Rosie Hospital is part of Cambridge University Hospitals NHS Foundation Trust… It has recently undergone a multi-million pound extension… <span class="cv-mark">On 24 May 2013 we were delighted and proud to welcome Her Majesty The Queen</span>…</p>'),
   after=page('After a positive test', '<ol class="cv-list"><li><b>Early pregnancy scan</b> at Cambridge IVF, included in your package.</li><li><b>Handover to the Rosie</b>, part of the same hospital trust, with your notes.</li><li><b>Specialist care if you need it</b>: high-risk obstetrics, fetal medicine and one of the UK’s largest neonatal units.</li></ol>'))

# ---------------------------------------------------------------------------
# Look and findability
# ---------------------------------------------------------------------------
qw(18, slug='theme-fix', theme='look',
   summary='Correct the theme setting on inner pages so they use the Cambridge IVF colours already in the stylesheet, not NHS blue.',
   url='cambridge-ivf.nhs.uk/services/fertility-treatments/pure-duo-ivf/',
   also='',
   why='The homepage uses Cambridge IVF’s dark pink, but every inner page has a blue hero, because the page carries the class “theme-- -ivf” instead of a valid theme name. The IVF theme rules are in the stylesheet and simply never apply. It’s a small fix for the CUH web team, and the site starts looking like one brand rather than two.',
   before_cap='A broken theme name, so inner pages fall back to NHS blue.',
   after_cap='The IVF theme applies: pink accent bar and headings.',
   before='<div class="cv-mock-head"><span class="logo">Cambridge IVF</span></div><div style="padding:2rem 1.25rem;background:var(--wf-text);color:var(--wf-page)"><h2 style="color:inherit">PURE IVF &amp; PURE IVF Duo</h2></div><p class="cv-small" style="padding:0.75rem 1.25rem">&lt;body class=“template-information-page <span class="cv-mark">theme-- -ivf</span>”&gt;</p>',
   after='<div class="cv-mock-head"><span class="logo">Cambridge IVF</span></div><div style="padding:2rem 1.25rem;background:var(--wf-surface);border-left:10px solid var(--wf-text)"><h2>PURE IVF &amp; PURE IVF Duo</h2></div><p class="cv-small" style="padding:0.75rem 1.25rem">&lt;body class=“template-information-page theme--ivf”&gt;</p>')

qw(19, slug='next-step-panel', theme='look',
   summary='Use the empty right-hand side of content pages for a “Next step” panel: price, next information session and an enquiry button.',
   url='cambridge-ivf.nhs.uk/services/fertility-treatments/pure-duo-ivf/',
   also='',
   why='At desktop width, content pages sit in a 640-pixel column with nothing beside them. That space is where a reader’s eye goes when they’ve decided they’re interested. A sticky panel with the price and the next step puts the call to action beside the content that persuades, without adding any content.',
   before_cap='One narrow column, nothing beside it.',
   after_cap='A next-step panel that follows you down the page.',
   before='<div style="display:grid;grid-template-columns:3fr 2fr;gap:1.5rem"><div><h3>PURE Package - 1 cycle</h3><p>This package is for 1 cycle of fresh IVF including medication up to pregnancy testing (except Lubion), HFEA fee, monitoring scans and bloods tests…</p><div class="wf-placeholder ratio-16-9">Image</div></div><div></div></div>',
   after='<div style="display:grid;grid-template-columns:3fr 2fr;gap:1.5rem"><div><h3>PURE Package - 1 cycle</h3><p>This package is for 1 cycle of fresh IVF including medication up to pregnancy testing (except Lubion), HFEA fee, monitoring scans and blood tests…</p><div class="wf-placeholder ratio-16-9">Image</div></div><div class="cv-panel"><p class="cv-eyebrow">PURE IVF</p><p class="cv-price">£5,240</p><p class="cv-small">Next information session: Tuesday [date]</p><div class="row"><span class="btn btn-sm">Enquire</span><span class="btn btn-sm btn-secondary">Estimate my cost</span></div></div></div>')

qw(42, slug='search-basics', theme='look',
   summary='Write unique titles and descriptions for the top 20 pages, and add short FAQs to the pages people search for.',
   url='Google search results',
   also='',
   why='Several pages share the same description (“Cambridge fertility clinic, 1 hr from London…”), and the search results page on the site has no title at all. Bourn Hall, ten miles away, competes for the same searches: “IVF Cambridge”, “egg freezing Cambridge”, “IVF cost Cambridge”. Clear titles and descriptions that mention price and “NHS” are free, and earn more of those clicks.',
   before_cap='The same generic description on several pages.',
   after_cap='Each listing says what the page is and why to click.',
   before='<div class="serp"><div class="url">cambridge-ivf.nhs.uk › services</div><div class="title">Services | Cambridge IVF</div><p class="desc">Cambridge fertility clinic, 1 hr from London. IVF, egg &amp; sperm freezing, donor services &amp; more. NHS and self-funded. Advanced research &amp; technology.</p></div><div class="serp" style="margin-top:1rem"><div class="url">cambridge-ivf.nhs.uk › referrals</div><div class="title">Referrals | Cambridge IVF</div><p class="desc">Cambridge fertility clinic, 1 hr from London. NHS and self-funded. IVF, egg &amp; sperm freezing, donor services &amp; more…</p></div>',
   after='<div class="serp"><div class="url">cambridge-ivf.nhs.uk › prices</div><div class="title">IVF prices in Cambridge from £2,900 | NHS clinic | Cambridge IVF</div><p class="desc">Fixed-price IVF packages from an NHS clinic, paid in stages. See what’s included and estimate your cost.</p><div class="serp-faq"><div><span>How much does IVF cost at Cambridge IVF?</span><span>˅</span></div><div><span>Can I pay in stages?</span><span>˅</span></div></div></div>')


# ---------------------------------------------------------------------------
# Writers
# ---------------------------------------------------------------------------
HEAD = '''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}: Cambridge IVF quick wins</title>
  <link rel="stylesheet" href="~/css/base.css">
  <link rel="stylesheet" href="~/css/components.css">
  <link rel="stylesheet" href="~/css/theme.css">
</head>
'''
FOOT = '''  <!-- @@include footer.html -->
  <script src="~/js/quick-wins.js"></script>
  <script src="~/js/wireframe.js"></script>
  <script src="~/js/civf.js"></script>
  <script src="~/js/photos.js"></script>
</body>
</html>
'''


def write_page(i, q):
    n = i + 1
    theme_name = dict(THEMES)[q['theme']]
    also = f'<p class="qw-where">{escape(q["also"])}</p>' if q.get('also') else ''
    html = HEAD.format(title=escape(q['title'])) + f'''<body data-qw-theme="{q['theme']}">
  <!-- @@include header.html -->

  <main id="main" class="flush">
    <!-- What we're proposing and why (shown when Notes are on) -->
    <aside class="proposal" aria-label="About this quick win">
      <div class="container">
        <p class="proposal-eyebrow">Quick win {n} of {len(QW)} · {escape(theme_name)}</p>
        <div class="proposal-grid">
          <div><h2>What we're proposing</h2><p>{escape(q['summary'])}</p></div>
          <div><h2>Why</h2><p>{escape(q['why'])}</p></div>
        </div>
      </div>
    </aside>

    <!-- Quick win QW{n} (idea {q['idea']}): {escape(q['title'])} -->
    <div class="container qw-head">
      <p class="qw-num">Quick win {n} · {escape(theme_name)}</p>
      <h1>{escape(q['title'])}</h1>
      <p class="lead">{escape(q['summary'])}</p>
      {also}
    </div>

    <div data-ba>
      <div class="ba-bar">
        <div class="container">
          <div class="ba-switch" role="group" aria-label="Compare">
            <button type="button" data-ba-show="before" aria-pressed="true">Today</button>
            <button type="button" data-ba-show="after" aria-pressed="false">Proposed</button>
          </div>
          <span class="ba-hint">Switch between the site as it is today and the change. Arrow keys work too.</span>
        </div>
      </div>
      <div class="container ba-stage">
        <div class="ba-before">
          <p class="ba-caption"><b>Today</b><span>{escape(q['before_cap'])}</span></p>
          <div class="ba-frame"><div class="ba-frame-bar"><i></i><i></i><i></i><span>{escape(q['url'])}</span></div>
            <div class="ba-frame-body">
{q['before']}
            </div>
          </div>
        </div>
        <div class="ba-after" hidden>
          <p class="ba-caption"><b>Proposed</b><span>{escape(q['after_cap'])}</span></p>
          <div class="ba-frame"><div class="ba-frame-bar"><i></i><i></i><i></i><span>{escape(q['url'])}</span></div>
            <div class="ba-frame-body">
{q['after']}
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>

''' + FOOT
    with open(os.path.join(OUT, q['slug'] + '.html'), 'w') as fh:
        fh.write(html)


def write_index():
    sections = ''
    for key, name in THEMES:
        items = [(i, q) for i, q in enumerate(QW) if q['theme'] == key]
        cards = ''.join(f'''
          <li><a class="qw-card" href="{q['slug']}.html"><span class="qw-n">QW{i + 1}</span><h3>{escape(q['title'])}</h3><p>{escape(q['summary'])}</p><span class="qw-also"><strong>Try:</strong> switch to Proposed.</span></a></li>''' for i, q in items)
        sections += f'''
      <section class="qw-theme" id="{key}" aria-labelledby="t-{key}">
        <h2 class="section-title" id="t-{key}">{escape(name)}</h2>
        <ul class="qw-grid">{cards}
        </ul>
      </section>
'''
    html = HEAD.format(title='Quick wins').replace(': Cambridge IVF quick wins', ': Cambridge IVF prototypes') + f'''<body class="qw-index">
  <!-- @@include header.html -->

  <main id="main" class="flush">
    <div class="page-head">
      <div class="container">
        <h1>Quick wins</h1>
        <p class="lead">{len(QW)} smaller changes to cambridge-ivf.nhs.uk, each shown on its own against the site as it is today. Any of them can be made independently of the five big improvements and of each other, and most need nothing more than an editor in the content management system.</p>
        <p style="margin-top:1rem">Open one, then use <strong>Today</strong> and <strong>Proposed</strong> to compare. Switch <strong>Notes on</strong> to see why we suggest it.</p>
      </div>
    </div>
    <div class="container" style="padding-top:2.5rem">
{sections}
    </div>
  </main>

''' + FOOT
    with open(os.path.join(OUT, 'index.html'), 'w') as fh:
        fh.write(html)


def write_data():
    data = [{'slug': q['slug'], 'title': q['title'], 'theme': q['theme'], 'idea': q['idea']} for q in QW]
    with open(os.path.join(ROOT, 'src', 'js', 'quick-wins.js'), 'w') as fh:
        fh.write('/* Generated by tools/quick_wins.py: the ordered list of quick wins, used for previous/next links and the jump list. */\n')
        fh.write('window.CIVF_QUICK_WINS = ' + json.dumps(data, ensure_ascii=False, indent=1) + ';\n')
    with open(os.path.join(ROOT, 'data', 'quick-wins.json'), 'w') as fh:
        json.dump([{'qw': i + 1, **{k: q[k] for k in ('slug', 'title', 'theme', 'idea', 'summary')}} for i, q in enumerate(QW)], fh, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    order = [k for k, _ in THEMES]
    QW.sort(key=lambda q: order.index(q['theme']))
    for i, q in enumerate(QW):
        write_page(i, q)
    write_index()
    write_data()
    print(f'Wrote {len(QW)} quick wins and the index to src/quick-wins/')
