# Cambridge IVF website: findings, ideas and how to do them

## Overview

Cambridge IVF is a good clinic with a website that makes people work too hard to become patients. This document sets out what we found on cambridge-ivf.nhs.uk, how five competing clinics handle the same things, and 43 ideas for improving the site, judged mainly on one question: does the change make it more likely that a visitor becomes a paying patient, pays for more, or costs the clinic less to serve?

It is written to be read alongside two other things. The first is a [clickable model](https://claude.ai/artifact/Kmv3jsjWSrXxN2xDhboYfL) of the five biggest ideas and 22 quick wins, styled to look like the Cambridge IVF site. The second is the [findings and opportunities page](https://claude.ai/artifact/4wSxQavT4ERFQSL34fVicE), which has every idea in a filterable list and a rough payback calculator. The design values used throughout are on the [design system page](https://claude.ai/artifact/7EtJavHXqrG74wQfCKuxx4).

None of this needs an agency. The site runs on Wagtail, a widely used content management system, on a platform shared with the rest of Cambridge University Hospitals (CUH). Most of the quick wins are an editor's job. The bigger ideas need the CUH web team or its supplier, or a tool the Trust already approves. The last third of this document explains who would do what, in what order, and how to tell whether it paid back.

Everything here is from the public website, the HFEA's public data and the competitors' public sites. We haven't seen the clinic's analytics, enquiry numbers, margins or capacity, and some of the recommendations depend on them. Where that's the case, we say so.

## What's working well

A good deal, which is worth saying first because most of the ideas build on it rather than replacing it.

- **Prices are published in full.** Many private clinics hide their prices behind a consultation. Cambridge IVF lists every package, test and fee on its [prices page](https://www.cambridge-ivf.nhs.uk/prices/), and Duo and Multi-Cycle packages are paid in stages, only for the cycles a patient goes ahead with.
- **The regulator rates it highly.** The [HFEA profile](https://www.hfea.gov.uk/choose-a-fertility-clinic/search/results/51/) shows a 5 out of 5 inspection rating, a licence to 2030 and a 2024 birth rate per embryo transferred of 31%, which the HFEA describes as consistent with the national average of 35%.
- **It's inclusive from the first line.** The [homepage](https://www.cambridge-ivf.nhs.uk/) names heterosexual couples, same sex couples, single women, single men and transgender people in its opening paragraph.
- **The free information sessions are a strong offer.** Fifteen minutes each with an embryologist, a fertility nurse and the finance manager, on Tuesday evenings ([information sessions](https://www.cambridge-ivf.nhs.uk/contact-us/free-information-sessions/)).
- **Some content is kept carefully up to date.** The [andrology wait times page](https://www.cambridge-ivf.nhs.uk/wait-times-for-andrology-appointments-and-semen-analysis-results/) was updated this week.
- **The NHS story is real and distinctive.** Care through to the Rosie, CUH genetics, counselling within two weeks and income reinvested in CUH's women's and children's services. No private rival can say the same.
- **The success rates page is honest in tone.** It quotes the HFEA's view that most clinics are "broadly all as good as each other" and points readers to the HFEA's comparison tool.

## What's holding it back

### No way to enquire online

There is no enquiry, booking or referral form on any of the 50 or so pages we checked. Self-referral is "by email or post" ([referrals](https://www.cambridge-ivf.nhs.uk/referrals/self-funded-referrals/)). Appointments are by phone, and information sessions are booked on a separate site with no date shown on the homepage. Every competitor we looked at takes enquiries on the page. Most people research fertility treatment in the evening, when the phone lines are closed, and an email address is a weak substitute for a form that tells someone what happens next.

It also means the clinic can't count how many enquiries the website produces, which makes every other change on this list hard to judge.

### Costs that surprise people

Sixteen of the 22 people who have rated the clinic on the HFEA site say they paid "way above the estimate". Six say it was about right. None say it was cheaper. The prices page, meanwhile, says the clinic prides itself on having no "hidden extras".

Both can be true. The package prices are fixed, but ICSI (£1,323 a cycle), freezing (£765), Lubion, medication top-ups and optional add-ons sit outside them, and they are listed separately under each of a dozen packages. The page runs to about 8,000 pixels on a phone, with 34 collapsible sections. It also has typos ("chalmydia", "IICSI", "Human and Fertilisation (HFEA)") and a gamete transport fee that is cheaper with a special export directive (£300) than without (£330), which may be right but looks like a mistake.

### Two answers to the same question

The prices page gives the PURE criteria as 37 and under, AMH 6 to 35 and BMI below 35. The [PURE page](https://www.cambridge-ivf.nhs.uk/services/fertility-treatments/pure-duo-ivf/) says under 38, AMH above 10, BMI below 30 and regular periods. Someone with an AMH of 8 and a BMI of 32 qualifies on one page and not on the other, and finds out which at a £220 consultation. The clinic's history is given as 1992 on one page, 1994 on another and "set up in 2011, builds on 20 years" on a third.

### Add-ons without the evidence

The clinic sells, or includes, several add-ons that the HFEA rates on its [traffic-light scale](https://www.hfea.gov.uk/treatments/treatment-add-ons/). Time-lapse imaging (EmbryoScope) and PICSI are rated black, meaning good evidence that they make no difference to the chance of a baby for most patients. EmbryoGlue is amber. Endometrial receptivity testing, sold at £1,308 to £1,623, is rated red. Sperm DNA fragmentation testing (£462) and assisted hatching are grey. None of this appears on the site, and the [EmbryoScope page](https://www.cambridge-ivf.nhs.uk/services/fertility-treatments/embryoscope/) says it "can improve your IVF treatment".

An NHS clinic is where patients would expect to be told this plainly. Guy's and St Thomas' says on its prices page that it recommends only evidence-based treatments, "ensuring you won't have any unnecessary add-ons".

### Out-of-date and broken pages

- Two main-menu links, "Your journey" and "Early pregnancy and Coronavirus", go to "Page not found".
- The [NHS funding section](https://www.cambridge-ivf.nhs.uk/referrals/self-funded-referrals/) says Cambridge and Peterborough CCG "have recently announced" that NHS IVF is returning, with details "to be added here as soon as they are available". CCGs were replaced by integrated care boards in July 2022.
- The [Sources of support page](https://www.cambridge-ivf.nhs.uk/your-journey/sources-of-support/) cites "36 of 209 CCG's", asks readers to contact a Minister for Public Health who left the post years ago, and links to a closed petition.
- The [success rates page](https://www.cambridge-ivf.nhs.uk/success-rates/) uses 2019 and 2020 data, "correct as of 8th January 2024", shown as pictures of charts. The HFEA now publishes 2024 figures.
- The [pregnancy care page](https://www.cambridge-ivf.nhs.uk/your-journey/pregnancy-care/) leads on the Rosie's royal opening in 2013. The newest patient story is of a similar vintage.
- The services and [patient information leaflets](https://www.cambridge-ivf.nhs.uk/services/patient-information-leaflets/) pages say they are "currently under development".
- The egg freezing and health professionals pages link to the old cambridge-ivf.org.uk domain, and the [feedback page](https://www.cambridge-ivf.nhs.uk/contact-us/feedback/) has links pasted from Outlook that include a member of staff's email address.
- The [support information page](https://www.cambridge-ivf.nhs.uk/about-us/support-information/) labels everything, glossary included, as "Non-urgent advice", which means something specific on NHS sites, and repeats the whole lab page.

### A structure built around the clinic, not the patient

The menu is organised by service: assessments, treatments, preservation, donors. The homepage names five kinds of patient, but none of them has a way in of their own. Female couples, single women and people freezing their eggs are almost all self-funded, which makes them the most valuable visitors the site gets. The [egg freezing page](https://www.cambridge-ivf.nhs.uk/services/fertility-preservation/egg-freezing/) is about 750 characters long, with no price on it.

### A broken theme

Inner pages carry the CSS class "theme-- -ivf" instead of a valid theme name, so the Cambridge IVF theme in the stylesheet never applies. The homepage is IVF pink; every other page has an NHS blue banner. It's a small developer fix.

## How the money works

Self-funded income is reinvested in CUH's women's and children's services, so it matters beyond the clinic. These are the purchases a website visitor can turn into, all at published prices.

| Stage | What people buy | Price |
|---|---|---|
| First steps | Fertility assessment; initial consultation; private semen analysis | £375 to £595; £220; £189 |
| Treatment | First IVF; PURE; PURE Duo; Plus; Multi-Cycle; donor egg cycle | £2,900; £5,240; £7,265; £6,290; £11,540; £6,990 to £7,990 |
| Planning ahead | Egg freezing, one to three cycles | £3,675 to £7,875 |
| Recurring | Egg, embryo or sperm storage from year two | £346 a year |

The arithmetic is simple and worth keeping in view. One extra PURE patient a month is £62,880 of revenue a year. One extra egg freezer a month is £44,100 in the first year, plus £4,152 a year in storage for every year after that, for each year's cohort. These are revenue figures, not profit, and we don't know the clinic's margin on each package.

The other caveat is capacity. If clinics and the lab are already full, more enquiries don't become more cycles. They become a shorter list of empty slots, more choice about whom to treat and when, and less need to spend on advertising. That is still a return, just a different one, and the clinic will know which situation it's in.

### What the changes cost, and when they pay back

We haven't priced any of the work, because most of it would be done by people the clinic or CUH already employs, and we don't know what their time costs. A useful way to judge each piece is to ask how many extra patients it needs to pay for itself. If the enquiry form, booking and tracking in concept 3 cost £15,000 all in, three extra PURE patients would cover it. If the egg freezing hub takes an editor two weeks and a little developer time, it needs very few extra cycles to cover it: four bring in £14,700 before any storage income. Most of the quick wins cost an hour or two of an editor's time, so they need no justification beyond being right.

## How the competition does it

We looked at five clinics: the nearest private rival, the biggest national group, the private clinic in Cambridge IVF's Hertfordshire and West Essex catchment, and two NHS units that have modernised their self-funded offer.

| Competitor | Why it matters | What stands out | Source |
|---|---|---|---|
| Bourn Hall Clinic | The nearest private rival, about ten miles west of Cambridge, plus clinics across the East of England. Same patients, same searches. | Menu by type of patient; "Book a discovery call" as the main button; open evenings including one in Cambridge; finance and a refund programme; success rates by age using 2025 outcomes; Doctify reviews; patient portal. | [bournhall.co.uk](https://www.bournhall.co.uk/) |
| CARE Fertility | The largest UK group, and the standard many self-funders compare against. | "Where to start" by audience, including trans and non-binary people and over-40s; NHS eligibility and BMI calculators; personalised success prediction; online events; Carepay finance; Trustpilot. | [carefertility.com](https://carefertility.com/) |
| Herts & Essex Fertility Centre | Cheshunt, in the middle of Cambridge IVF's Hertfordshire and West Essex NHS catchment. | "Are you…" menu listing eight patient situations; next free open evening date on the homepage; consultation form; refund policy page; Meet our team. | [hertsandessexfertility.com](https://hertsandessexfertility.com/) |
| The Hewitt Fertility Centre | An NHS unit in Liverpool with a self-funded offer. The closest model for what Cambridge IVF could be online. | "How can we help you?" menu by situation; profiles of every consultant; award-winning patient portal; virtual appointments; self-funded "Hewitt Options" with a fee schedule and financial packages. | [Hewitt costs](https://www.thehewittfertilitycentre.org.uk/funded-and-self-fund-care/treatment-and-care-costs/) |
| Guy's and St Thomas' Specialist Care | An NHS trust selling self-funded fertility care in London. | Eligibility criteria on the prices page; "no unnecessary add-ons"; personalised costed plan; enquiry form on the prices page; payments through GOV.UK Pay; evening and weekend appointments. | [GSTT prices](https://guysandstthomasspecialistcare.co.uk/services/fertility-prices-and-packages/) |

Every one of them lets people enquire or book without picking up the phone, and four of the five organise their menus around the patient rather than the service. The two NHS units show that an NHS clinic can do both.

In the table below, "n/c" means not checked rather than missing. All sites were checked in the browser for this review.

| Feature | Cambridge IVF | Bourn Hall | CARE | Herts & Essex | Hewitt | Guy's and St Thomas' |
|---|---|---|---|---|---|---|
| Full prices on site | Yes | Yes | Yes | Yes | PDF | Yes |
| Online enquiry form | No | Yes | Yes | Yes | n/c | Yes |
| Book a call or consultation online | No | Yes | n/c | Form | n/c | Yes |
| Events or open evenings | Phone sessions | Open evenings | Online events | Open evenings | n/c | n/c |
| Menu by type of patient | No | Yes | Yes | Yes | By situation | n/c |
| Eligibility or self-assessment tool | No | Yes | Yes | n/c | n/c | Criteria listed |
| Finance or refund programme | Staged payments | Yes | Yes | Funding options page | Yes | n/c |
| Add-on evidence stated | No | n/c | n/c | n/c | n/c | Yes |
| Current success rates by age | No | Yes | n/c | n/c | n/c | n/c |
| Team profiles | No | Yes | n/c | Yes | Yes | Yes |
| Patient portal or digital consent | None seen | Yes | Yes | Yes | Yes | Yes |

What this adds up to is three gaps. Cambridge IVF is the only one of the six with no online enquiry route. It is one of the few that doesn't speak to each kind of patient by name. And it is behind on current, readable proof: success rates, team and reviews. The one place it could lead is honesty about add-ons, where only Guy's and St Thomas' takes a clear position.

We didn't analyse search. Bourn Hall competes for the same local searches ("IVF Cambridge", "egg freezing Cambridge", "IVF cost Cambridge"), and the clinic's Google Search Console data would show which ones bring people to the site and which it's losing.

## The five big improvements

Each of these combines several ideas into one piece of work. They are shown as working prototypes in the model.

### 1. Clear costs

An honest total before the first appointment. A short estimator asks which package, whether ICSI is likely and whether spare embryos would be frozen, and gives a likely total, a range and the staged payments. The packages sit side by side in one table, with criteria, price per cycle and how payment is staged. Every add-on carries the HFEA's rating and a line on why it might be suggested. A short "Ways to pay" section covers staged payments, refunds and, if CUH agrees, finance.

**Ideas combined:** 1, 2, 3, 6, 7, 8 and 32.

**How it pays back:** fewer people dropping out after an expensive first consultation; more people choosing Duo and Multi-Cycle, which are worth more and give more than one try; a better "did you pay what you expected" score on the HFEA site. Candidly, showing the add-on ratings may trim some optional sales. We think the trust it buys is worth more.

**How to build it:** the CUH web team. The important part is holding prices, inclusions and criteria once, as Wagtail "snippets", so the table, the estimator, the package pages and the PDF price list all change together each April. The estimator is a small piece of JavaScript reading those snippets. Medium to large.

### 2. Find your path

A starting point for each kind of patient: couples, female couples, single women, single men and male couples, trans and non-binary people, people planning ahead, NHS referrals and people moving from another clinic. Each shows the likely route, the first paid step and the next thing to do. Alongside it, a four-question check of which package is likely to fit, a plain NHS funding check by area, and a "Your journey" page from first enquiry to the Rosie.

**Ideas combined:** 4, 15, 16, 28 and 41.

**How it pays back:** puts the most valuable self-funded visitors on the right price and next step in one or two clicks, and catches people who find they aren't NHS-eligible with a self-funded alternative.

**How to build it:** mostly an editor, using pages and blocks the site already has. The package check needs a small block from the CUH web team. Medium.

### 3. Start today

One place to take the first step: a short enquiry form, a free call booked at a chosen time, a place at an information session booked on the page, or a full self-referral with uploads for previous results. Each ends with a clear "what happens next". A guide sign-up catches people who aren't ready yet.

**Ideas combined:** 9, 10, 11, 12, 13 and 14.

**How it pays back:** the biggest single lever on the list. More enquiries, captured out of hours, followed up faster and counted for the first time, so the clinic can see which pages and changes work.

**How to build it:** a third-party tool. Enquiries contain health information, so the forms should use a tool the Trust already approves, with a data protection impact assessment, rather than Wagtail's own form builder. Booking can use whatever CUH uses for outpatient appointments, or TryBooking, which the clinic already uses. Medium, mostly governance rather than building.

### 4. Proof you can trust

Current HFEA success rates by age, in both of the HFEA's measures, as real charts rather than images; profiles of the people who'll look after you; stories from every kind of family; four plain reasons why an NHS clinic is different; and a routine for asking patients to rate the clinic on the HFEA site.

**Ideas combined:** 21, 23, 24, 25 and 26.

**How it pays back:** wins more of the people who shortlist on the HFEA site and compare Cambridge IVF with Bourn Hall. The rating routine may be the cheapest revenue lever in the whole document: with only 22 ratings, a few dozen more from ordinary, satisfied patients would move the score.

**How to build it:** an editor, plus the patient team for the rating routine and for collecting stories with consent. Small to medium.

### 5. Self-pay services

An egg freezing hub with the full cost over time, including storage; online booking and payment for private semen analysis with the current wait shown at the point of booking; a short online pre-screen for would-be sperm donors in place of the PDF questionnaire; and a page to pay storage fees.

**Ideas combined:** 36, 37, 38 and 39.

**How it pays back:** egg freezing is entirely self-funded, worth £3,675 to £7,875 up front and £346 a year after that, and the current page barely competes for it. Online booking and payment take calls off a busy line and bring cash in faster. Each recruited donor supports several treatment cycles.

**How to build it:** the egg freezing hub is editorial. Booking and payment need a tool; GOV.UK Pay is what Guy's and St Thomas' uses. Medium.

## The quick wins

Twenty-two smaller changes, each shown on its own in the model against the site as it is today. Any of them can be made independently of the big improvements and of each other. Payback: £££ brings in paying patients directly; ££ improves conversion or trust, or saves staff time; £ is hygiene that protects the rest.

{{QW_TABLE}}

## How the site is built, and who would do what

The site runs on Wagtail, a content management system built on Django: the admin login at /admin/ is Wagtail's, and images are served as Wagtail renditions from media.cuh.nhs.uk. It shares one codebase and one stylesheet with the rest of CUH's websites (the stylesheet carries themes for CUH, the Rosie, Cambridge Children's and others). The front end uses NHS.UK design system components. Google Analytics 4 and Google Tag Manager are installed. Information sessions are booked through TryBooking and feedback is collected through SurveyMonkey.

That shapes the work into four routes.

### Editor, in Wagtail (25 ideas)

Copy fixes, menu changes, new pages and new sections built from blocks the site already has: accordions, teasers, inset text, the pink call-to-action panel, document lists and video. Almost every quick win is here. The practical need is an owner with an hour or two a week and the authority to publish, and a clinical lead who will sign off criteria and add-on wording quickly.

### CUH web team or supplier (8 ideas)

Template fixes (the broken IVF theme, the empty right-hand column, the search page title), a sticky action bar on mobile, and new blocks: the package comparison table, the estimator, the package check and the next-step panel. The most valuable single change is a "price" snippet in Wagtail, so that one record feeds every page that shows that price.

These are best raised together as one change request. Several would be useful to other CUH services, such as the comparison table and the next-step panel, which should make them easier to prioritise on a shared platform.

### Third-party tool (6 ideas)

Forms, booking and payments. Because enquiries and referrals contain health information, the forms must be secure and approved by the Trust's information governance team, with a data protection impact assessment. It's worth asking which tools CUH already uses elsewhere before buying anything. GOV.UK Pay is available to NHS bodies and is what Guy's and St Thomas' uses for fertility payments.

### Process (4 ideas)

Things the clinic does rather than builds: asking every patient to rate the clinic on the HFEA site, collecting new patient stories with consent, deciding whether to offer finance, and a monthly report from the analytics that is already installed.

### A sensible order

1. **This month.** The editor quick wins, starting with the PURE criteria, the two broken menu links, the NHS funding page and the add-on ratings. Turn on event tracking in Google Tag Manager so there's a "before" to compare with. Start handing out the HFEA rating card.
2. **Next month.** Information session dates on the homepage and key pages; the egg freezing hub; the success rates refresh.
3. **Within three months.** The online enquiry form and call booking (concept 3), because they make everything after them measurable.
4. **Within six months.** Clear costs and Find your path (concepts 1 and 2) with the CUH web team; online payments and semen analysis booking.

## Measuring whether it paid back

Google Tag Manager is already on the site, so the measurement is configuration, not development. We'd set up these events first:

- taps on phone numbers and email links;
- clicks through to TryBooking, and later information session bookings on the page;
- downloads of the PDF price lists;
- form submissions, once the forms exist, tagged with the page they came from;
- use of the estimator and package check (which package was chosen).

A one-page monthly report should show visits to service, price and package pages, the actions above, and the rate at which visits turn into actions, by page. The patient services team can add the number of enquiries that became paid treatment. With those two numbers, the payback calculator on the findings page becomes a real forecast rather than an illustration.

The HFEA patient rating is the other number to watch. It's public, it's what comparison shoppers see, and it should respond within months to both the rating routine and clearer costs.

## Questions for the clinic

These are the questions whose answers would most change what we'd recommend. The starred ones matter most.

| # | Question | Why we ask |
|---|---|---|
| 1 ★ | Are clinics and the lab full, or is there capacity for more self-funded cycles? | Decides whether more enquiries mean more revenue or simply more choice. |
| 2 ★ | Roughly how many enquiries a month come in, and how many become paid treatment? | Turns the payback calculator into a forecast. |
| 3 ★ | Which PURE criteria are current? | Two versions are live today. |
| 4 | Which clinics do patients most often mention comparing you with? | We assumed Bourn Hall is the main rival; the clinic will know. |
| 5 | Will the clinical lead stand behind publishing the HFEA add-on ratings, and keep offering add-ons rated red? | Shapes concept 1 and the clinic's positioning. |
| 6 | What is behind the "way above the estimate" ratings: medication, ICSI, freezing or something else? | Tells us what the estimator must show. |
| 7 | Which form, booking and payment tools does CUH already approve? | Using one is quicker and cheaper than buying one. |
| 8 | Who can publish in Wagtail, and how much of their time could this have? | Most of the quick wins depend on it. |
| 9 | Would CUH allow a finance partner or interest-free instalments? | Every private rival offers finance. |
| 10 | Which staff are happy to have a profile and photo? | Needed for concept 4. |

## Sources and method

We walked the Cambridge IVF site in a browser at desktop and phone widths, read every page linked from the menus and service pages (about 50), measured the design values from its stylesheet and computed styles, and checked the platform from the admin login and image URLs. We read the clinic's HFEA profile and the HFEA's add-on ratings, and looked at the equivalent pages on five competitors' sites. All of this was done for this review.

We didn't see the clinic's analytics, enquiry or conversion figures, margins, capacity or anything behind a login, and we didn't analyse search volumes or rankings. Success-rate figures by age in the model are samples to show the layout. Competitor features marked "n/c" weren't checked.

- [Cambridge IVF homepage](https://www.cambridge-ivf.nhs.uk/)
- [Prices](https://www.cambridge-ivf.nhs.uk/prices/)
- [PURE IVF and PURE Duo](https://www.cambridge-ivf.nhs.uk/services/fertility-treatments/pure-duo-ivf/)
- [EmbryoScope](https://www.cambridge-ivf.nhs.uk/services/fertility-treatments/embryoscope/)
- [Egg freezing](https://www.cambridge-ivf.nhs.uk/services/fertility-preservation/egg-freezing/)
- [Success rates](https://www.cambridge-ivf.nhs.uk/success-rates/)
- [NHS and self-funded referrals](https://www.cambridge-ivf.nhs.uk/referrals/self-funded-referrals/)
- [Free information sessions](https://www.cambridge-ivf.nhs.uk/contact-us/free-information-sessions/)
- [Sources of support](https://www.cambridge-ivf.nhs.uk/your-journey/sources-of-support/)
- [Support information](https://www.cambridge-ivf.nhs.uk/about-us/support-information/)
- [Pregnancy care](https://www.cambridge-ivf.nhs.uk/your-journey/pregnancy-care/)
- [Patient information leaflets](https://www.cambridge-ivf.nhs.uk/services/patient-information-leaflets/)
- [Feedback](https://www.cambridge-ivf.nhs.uk/contact-us/feedback/)
- [Andrology wait times](https://www.cambridge-ivf.nhs.uk/wait-times-for-andrology-appointments-and-semen-analysis-results/)
- [HFEA clinic profile: Cambridge IVF](https://www.hfea.gov.uk/choose-a-fertility-clinic/search/results/51/)
- [HFEA: treatment add-ons with limited evidence](https://www.hfea.gov.uk/treatments/treatment-add-ons/)
- [Bourn Hall Clinic](https://www.bournhall.co.uk/) and [its fees and funding page](https://www.bournhall.co.uk/fees-funding/)
- [CARE Fertility](https://carefertility.com/)
- [Herts & Essex Fertility Centre](https://hertsandessexfertility.com/)
- [The Hewitt Fertility Centre: treatment and care costs](https://www.thehewittfertilitycentre.org.uk/funded-and-self-fund-care/treatment-and-care-costs/)
- [Guy's and St Thomas' Specialist Care: fertility prices and packages](https://guysandstthomasspecialistcare.co.uk/services/fertility-prices-and-packages/)
- [Findings and opportunities page](https://claude.ai/artifact/4wSxQavT4ERFQSL34fVicE)
- [Design system page](https://claude.ai/artifact/7EtJavHXqrG74wQfCKuxx4)
- [Prototype model](https://claude.ai/artifact/Kmv3jsjWSrXxN2xDhboYfL)
