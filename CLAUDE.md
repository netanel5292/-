# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is not a software project. There is no code, build, lint or test step. The repository holds business and marketing material for the owner's martial-arts studio. Talk to the owner in Hebrew, and write content for the studio in Hebrew.

- `CLAUDE_CODE_BUSINESS_COMMANDS.md`: a Hebrew guide to Claude Code commands, agents, video editing and reminders for promoting the business.
- `.claude/agents/`: three subagents. `social` (posts, reels, captions), `ideas` (cheap growth ideas), `property` (new-space search). The dashboard shows them under "הצוות שלי"; a scheduled task runs the property search daily at 10:20 Sun–Fri (Israel) and writes to the `listings` collection and `agents/property`.

## The business

- **Name:** Jew Jitsu Ashkelon (the official English spelling; ג'ו-ג'יצו אשקלון in Hebrew).
- **Owner:** Netanel. Serves in the reserves (מילואים), so the studio needs someone in charge while he is away.
- **Paid ads:** tracked in the finance tab's "📣 פרסום ממומן" box (`finance/ads.items`: {d, ch: instagram|tiktok|meta|other, a in ₪, note}), by week (Sunday start). Week of 15 Nov about ₪600, week of 22 Nov ₪240 so far (Instagram); TikTok and Meta coming. All amounts are shekels, never dollars. The current lease ends about 2.5 weeks after 11 Nov 2026.
- **Tools in use:** Arbox (studio management and lead app). A daily Instagram story about that day's class is already automated.
- **Space search:** looking for about 110–150 m², target about ₪9,000 a month, ideally without a broker. Deadline: a decision before early December 2026 (end of the first year).
  - Brokers frustrate the owner (each claims ownership of listings), so prefer owners directly, the municipality and the regional council.
  - Promising: 2–3 warehouses for rent in the Hof Ashkelon regional council, seen on Facebook Marketplace (10 Nov 2026). Cheap, need renovation; the owner likes this option. Check zoning / change-of-use permit before signing. 11 Nov: the first owner refused (agricultural compound, said a studio could cause trouble).
  - Ashkelon municipality sports department: the owner visited on 11 Nov to ask about a partnership or a space; waiting for an answer.
  - Eli Cohen shelters/warehouses: visited, not suitable. Municipal allocations unit (Anat Machluf, 08-6792437) allocates buildings to non-profits for free or a token fee, so a non-profit route is worth checking with lawyer Hajaj.
  - Seen or offered: properties via brokers Tal and Bashiri (10 Nov), villas via Ron (requested); a 100 m² yard in Migdal via Arik Ezra (11 Nov, option: cover the yard?).
  - **The relevant options (16 Nov):** the property at the entrance to Migdal (contact: Tomer, not Ami; ₪5,500–6,000; viewing on 16 Nov at 14:00) first, Arik Ezra's yard in Migdal second, plus two Facebook Marketplace leads (a 170 m² building; Matan Shmuel's house with a garden). The search now also covers the Hof Ashkelon regional council (business zones easy; farm compounds need a change-of-use permit). Hof Ashkelon sports: Sofia Moisa, sport@hof-ashkelon.org.il, council switchboard 08-6776402. Listings the property agent found on yad2 (Neve Alonim shop, Migdal office, a 120 m² warehouse) are not on the owner's radar.
- **Task dashboard:** https://claude.ai/artifact/AVqhSAjH9etHzc46Usz6NZ (tasks, leads, quick actions; data in its `tasks` collection and `studio/settings`). A scheduled task at 07:45 Sun–Thu (Israel) rewrites `studio/morning`: 5 focus tasks picked from the existing list, a day schedule from Google Calendar, one idea, one task to drop. It never adds tasks. Tabs (21 Nov): "📋 משימות ופרויקטים" (weekly projects from the `projects` collection on top, then tasks) and "👥 לידים ורשומים" (leads on top, the registered list below; a lead marked "נרשם" moves down to it). The tab bar wraps onto 2–3 rows. The owner likes the "פחות מ-3 דקות" quick-task category: keep feeding it. The 80/20 focus holds only big moves (owner, 19 Nov): each one can bring 5+ trainees or save ₪1,000+ a month and needs morning focus (space, lead engine, retention, campaigns, school partnerships); these tasks have ids starting `m_`. Reminders for a single lead or trainee go into the small-task block, never the 80/20. Every task has a priority `pri`: A 🔴 important (morning 80/20), B 🟡 medium (small-task block, the default), C ⚪ "when bored" (afternoon); set it when adding a task. The owner works mornings 08:45–12:30: the "היום" tab has "🧱 לבנות הבוקר" (`studio/blocks`): two big blocks of about an hour (10:15–11:30, 11:30–12:30) and small-task slots before them; tasks are dragged (or tapped) into blocks. The morning task fills them unless the owner already planned that day.
- **Whiteboard** (separate from the dashboard, 21 Nov): https://claude.ai/artifact/CRpudsUabS6XPg2H21AQpx, sections for big moves, hot leads and ideas. Never mix its data with the dashboard.
- **Type:** a martial-arts studio (מכון אומנויות לחימה).
- **Classes:** Brazilian jiu-jitsu, classic boxing, Muay Thai, wrestling, and kids' classes (mostly mixed disciplines).
- **Trainees:** 65 at present (21 November 2026). The dashboard's top +/− counter (`studio/settings.trainees`) and the current month's trainee count in the finance tab (`finance/months`) are kept in sync: changing either updates the other and the forecasts. The "מי רשום" tab now stores each trainee's preferred class times (`pref`); ask for them when a trainee joins.
- **Price list** (full version in `pricing/mechiron.html`, printable PDF `pricing/mechiron.pdf`):
  - Unlimited: ₪400 by standing order / credit card, ₪420 cash / Bit / PayBox.
  - 3 times a week ₪350; twice a week ₪280; once a week ₪180; open mat only ₪50 (a month).
  - Single class ₪50. Trial class (from 19 Nov 2026): ₪25 by prior arrangement, paid in advance through the Arbox link; deducted from the membership if the trainee signs up that same week. A trial without prior arrangement: ₪50. Discounts for reservists, soldiers and security forces: ask at the desk.
  - Standing order on a credit card, charged from the sign-up date a month ahead. Cash / Bit / PayBox: paid in advance for the next two months.
  - All members may come to open mat (Fridays and as announced in the WhatsApp group). Morning classes only by arrangement in the "אימוני בוקר" group.
  - No classes on Pesach, Shavuot and Sukkot (including Chol HaMoed), Memorial Day and Independence Day, 2 days of Chanukah, and Purim day.
  - Private training (BJJ, wrestling, Muay Thai, classic boxing, self-defense): ₪230 a single session; ₪205 a session in a prepaid 5-pack; ₪185 a session in a prepaid 10-pack.
  - Earlier note from the owner: most trainees pay ₪280.
- **Space costs:** rent ₪12,000 + VAT a month (rises by ₪1,000 + VAT from 1 Dec 2026; the dashboard's "🔮 שנה קדימה" forecast includes it), public arnona ₪1,000, regular arnona ₪1,500. Other costs are not yet known.
- **Location:** Ashkelon. The owner is looking for another, cheaper space in Ashkelon and is seriously considering a move.
- **Age:** the first year ends at the end of November 2026.
- **Finances:** the studio loses about ₪6,000 a month at present.
- **Finances (from the owner's Excel, Nov 2026):** the dashboard tab "💰 כספים" (`finance/plan`, `finance/months`) holds the data; the owner marks expenses as paid and edits amounts there.
  - Monthly fixed costs about ₪23,760 (₪21,600 + 10% buffer): rent ₪14,200 incl. VAT (₪15,380 from 1 Dec), arnona 2,500 (1,000 public + 1,500 regular), electricity/water 500, extra coach 1,000, ads 2,000 (actual ~500), software 200, accountant 500, Arbox 600, cleaning 100. Insurance, owner's salary and a secretary have no amount yet.
  - Income: average membership ₪270, private training ~₪400, sales ~₪700 a month. A normal month without rent grace loses about ₪7,500 (from Dec, staying in the mall). Migdal scenario in the dashboard: ₪6,000 + VAT rent, ₪1,200 arnona, ₪5,000 brokerage once; this turns the month positive at the current trainee count.
  - Start capital ₪160,000 (₪119,800 of it family loans). About ₪39,000 left after November; Oct and Nov had a rent grace of ₪14,180 each.
  - By the Excel numbers, break-even is about 78 trainees (the dashboard keeps 88 as a safety margin). At ₪6,000 + VAT rent it drops to about 52.
- **Break-even:** 88 registered trainees. **Big goal:** at least 110.
- **Bank:** business account at Mizrahi Tefahot. On 18 Nov the owner signed up for "מזרחי-טפחות בזמן אמת" (email + SMS). The morning task (07:45 Sun–Thu) searches Gmail for the bank email, writes `finance/bank` {date, balance, card[], note} (the finance tab starts its forecast from that balance), and emails the owner a short summary with observations and what it added. Never ask for bank passwords. 19 Nov: balance ₪32,465 (books, 18 Nov), credit line ₪10,000 unused. The ₪18,000 arnona debt was paid by business credit card in 3 charges of ₪6,000 (Dec, Jan, Feb), stored in `finance/bank.card` and deducted in the forecast; with them, staying in the mall runs out of cash around March 2027. The business credit card is charged on the 2nd of each month; card income from the GROW clearing arrives on the 9th, and the mall rent is paid on the 1st or 2nd, so the balance is lowest between the 1st and the 9th (`finance/plan.cardDay`, `settleDay`).
- **What the owner is trying now:** automations, more advertising, and partnerships. The open question is whether these bring a real return, or whether the studio needs to move or change course.

## How to help

- Measure every marketing idea by the main goal: more paying trainees, toward break-even at 88 and the big goal of 110. Where possible, estimate cost and expected trainees gained.
- Treat a lower rent from a move as a direct way to lower the break-even point, and weigh it against growth options.
- The owner has little time. Prefer ideas and automations that are quick to set up and run with free or cheap tools, and give step-by-step instructions.
- Churn (owner, 19 Nov): about 5 trainees leave a month (4–8) and 4–8 join, so the net is near zero. Family loans have no monthly repayment yet. The forecast uses `finance/plan.joins` (6) and `churn` (5). Retention is the cheapest lever: weekly project "לעצור עזיבות".
- Still unknown: other fixed costs (coaches, insurance, utilities), and lease terms. Ask for them when they matter, and add them here.
- Marketing content (posts, ads, reels scripts, landing pages) should speak to people in Ashkelon and nearby.
- The owner likes it when Claude proposes in-between steps on its own (e.g. "check the zoning with the municipality first"): keep adding them as quick tasks or weekly projects.
- Social media workflow: the owner drops photos/videos into the Google Drive folder "Jew Jitsu – מדיה לפרסום" (id 1AaGLIPz3T7jcP9WzLEN6BYxoiUZtbVXi; subfolder "קליסטניקס" 1j4DJIbuG3owcu8N4fvG-Jvyi4iNuKW9A). Claude reads them, designs the post and caption, and saves the result in "מוכן לפרסום" (1AE7Iu3c5h1U1ZPFw9SRTt13BQ8HPIoNT). There is no Instagram/TikTok connector, so the owner (or Meta Business Suite scheduling) does the actual posting.

## Where things stand (handoff, 19 Nov 2026)

- **Decisions this week:** the space (Tomer, Migdal entrance, `m_place`) before the lease ends on 30 Nov; the lead-form ad with Lior Ben Hamo handling leads (`m_leadform`, weekly project p11, budget ₪1,000); retention (`m_retain`, project p12); a "year one" campaign for 30 Nov (`m_year1`); a demo class at the Chabad school.
- **Hot leads:** HaRav Gad's group of 4–5 (12% off each by standing order, plus friend-brings-friend: 50% off the second month for each referrer whose friend signs up; task `m_gadref`); Shai (classic boxing, Mon 23 Nov 18:30, calendar reminder 09:00); Olga (daughters Eva 5 and Shaylin 6) and Yavnia Cohen (daughter 5): book them into the same kids' trial; Tehila Shabo (15, Muay Thai).
- **Dashboard tabs added this week:** 🧱 morning blocks (drag tasks), priority tags 🔴/🟡/⚪ with a filter in the tasks tab, 👩 women and girls lead group (sub-tags: wants a woman coach / Muay Thai only / young girls), finance: real bank balance, card installments, joins vs churn, trend chart, what-if line, loan box.
- **Dashboard technical note:** the artifact runtime returns frozen (read-only) snapshot data; the page deep-copies every snapshot (`dc()`). Keep doing that in any new code, or edits silently fail.
- **Files:** latest business-status flyer `weekly/status-19-11.png`; price list `pricing/mechiron.*` (trial ₪25).
- **Open questions for the owner:** is the old lead "נערה בת 15: לחזור לאם" Tehila? Exact spelling of "אור יוספשווילי"? Coach pay and lease terms.
