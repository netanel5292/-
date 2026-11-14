# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is not a software project. There is no code, build, lint or test step. The repository holds business and marketing material for the owner's martial-arts studio. Talk to the owner in Hebrew, and write content for the studio in Hebrew.

- `CLAUDE_CODE_BUSINESS_COMMANDS.md`: a Hebrew guide to Claude Code commands, agents, video editing and reminders for promoting the business.
- `.claude/agents/`: three subagents. `social` (posts, reels, captions), `ideas` (cheap growth ideas), `property` (new-space search). The dashboard shows them under "הצוות שלי"; a scheduled task runs the property search daily at 10:20 Sun–Fri (Israel) and writes to the `listings` collection and `agents/property`.

## The business

- **Name:** Jew Jitsu Ashkelon (the official English spelling; ג'ו-ג'יצו אשקלון in Hebrew).
- **Owner:** Netanel. Serves in the reserves (מילואים), so the studio needs someone in charge while he is away.
- **Paid ads:** about ₪500 a month of sponsored ads (as of Nov 2026). The current lease ends about 2.5 weeks after 11 Nov 2026.
- **Tools in use:** Arbox (studio management and lead app). A daily Instagram story about that day's class is already automated.
- **Space search:** looking for about 110–150 m², target about ₪9,000 a month, ideally without a broker. Deadline: a decision before early December 2026 (end of the first year).
  - Brokers frustrate the owner (each claims ownership of listings), so prefer owners directly, the municipality and the regional council.
  - Promising: 2–3 warehouses for rent in the Hof Ashkelon regional council, seen on Facebook Marketplace (10 Nov 2026). Cheap, need renovation; the owner likes this option. Check zoning / change-of-use permit before signing. 11 Nov: the first owner refused (agricultural compound, said a studio could cause trouble).
  - Ashkelon municipality sports department: the owner visited on 11 Nov to ask about a partnership or a space; waiting for an answer.
  - Eli Cohen shelters/warehouses: visited, not suitable. Municipal allocations unit (Anat Machluf, 08-6792437) allocates buildings to non-profits for free or a token fee, so a non-profit route is worth checking with lawyer Hajaj.
  - Seen or offered: properties via brokers Tal and Bashiri (10 Nov), villas via Ron (requested); a house in Barnea with a 100 m² yard via Arik Ezra (11 Nov, option: cover the yard?).
- **Task dashboard:** https://claude.ai/artifact/AVqhSAjH9etHzc46Usz6NZ (tasks, leads, quick actions; data in its `tasks` collection and `studio/settings`). A scheduled task at 07:45 Sun–Thu (Israel) rewrites `studio/morning`: 5 focus tasks picked from the existing list, a day schedule from Google Calendar, one idea, one task to drop. It never adds tasks. The "🎯 השבוע" tab holds weekly projects (`projects` collection) with a status and a note each. The owner likes the "פחות מ-3 דקות" quick-task category: keep feeding it.
- **Type:** a martial-arts studio (מכון אומנויות לחימה).
- **Classes:** Brazilian jiu-jitsu, classic boxing, Muay Thai, wrestling, and kids' classes (mostly mixed disciplines).
- **Trainees:** 56 at present (9 November 2026; Oz Stark joined that day).
- **Price list** (full version in `pricing/mechiron.html`, printable PDF `pricing/mechiron.pdf`):
  - Unlimited: ₪400 by standing order / credit card, ₪420 cash / Bit / PayBox.
  - 3 times a week ₪350; twice a week ₪280; once a week ₪180; open mat only ₪50 (a month).
  - Single class ₪50; trial class ₪30. Discounts for reservists, soldiers and security forces: ask at the desk.
  - Standing order on a credit card, charged from the sign-up date a month ahead. Cash / Bit / PayBox: paid in advance for the next two months.
  - All members may come to open mat (Fridays and as announced in the WhatsApp group). Morning classes only by arrangement in the "אימוני בוקר" group.
  - No classes on Pesach, Shavuot and Sukkot (including Chol HaMoed), Memorial Day and Independence Day, 2 days of Chanukah, and Purim day.
  - Private training (BJJ, wrestling, Muay Thai, classic boxing, self-defense): ₪230 a single session; ₪205 a session in a prepaid 5-pack; ₪185 a session in a prepaid 10-pack.
  - Earlier note from the owner: most trainees pay ₪280.
- **Space costs:** rent ₪12,000 + VAT a month, public arnona ₪1,000, regular arnona ₪1,500. Other costs are not yet known.
- **Location:** Ashkelon. The owner is looking for another, cheaper space in Ashkelon and is seriously considering a move.
- **Age:** the first year ends at the end of November 2026.
- **Finances:** the studio loses about ₪6,000 a month at present.
- **Finances (from the owner's Excel, Nov 2026):** the dashboard tab "💰 כספים" (`finance/plan`, `finance/months`) holds the data; the owner marks expenses as paid and edits amounts there.
  - Monthly fixed costs about ₪22,110 (₪20,100 + 10% buffer): rent ₪14,200 incl. VAT, arnona 1,000, electricity/water 500, extra coach 1,000, ads 2,000 (actual ~500), software 200, accountant 500, Arbox 600, cleaning 100. Insurance, owner's salary and a secretary have no amount yet.
  - Income: average membership ₪270, private training ~₪400, sales ~₪700 a month. A normal month without rent grace loses about ₪5,900.
  - Start capital ₪160,000 (₪119,800 of it family loans). About ₪39,000 left after November; Oct and Nov had a rent grace of ₪14,180 each.
  - By the Excel numbers, break-even is about 78 trainees (the dashboard keeps 88 as a safety margin). At ₪6,000 + VAT rent it drops to about 52.
- **Break-even:** 88 registered trainees. **Big goal:** at least 110.
- **What the owner is trying now:** automations, more advertising, and partnerships. The open question is whether these bring a real return, or whether the studio needs to move or change course.

## How to help

- Measure every marketing idea by the main goal: more paying trainees, toward break-even at 88 and the big goal of 110. Where possible, estimate cost and expected trainees gained.
- Treat a lower rent from a move as a direct way to lower the break-even point, and weigh it against growth options.
- The owner has little time. Prefer ideas and automations that are quick to set up and run with free or cheap tools, and give step-by-step instructions.
- Still unknown: other fixed costs (coaches, insurance, utilities), lease terms, and how many trainees leave each month. Ask for them when they matter, and add them here.
- Marketing content (posts, ads, reels scripts, landing pages) should speak to people in Ashkelon and nearby.
- The owner likes it when Claude proposes in-between steps on its own (e.g. "check the zoning with the municipality first"): keep adding them as quick tasks or weekly projects.
- Social media workflow: the owner drops photos/videos into the Google Drive folder "Jew Jitsu – מדיה לפרסום" (id 1AaGLIPz3T7jcP9WzLEN6BYxoiUZtbVXi; subfolder "קליסטניקס" 1j4DJIbuG3owcu8N4fvG-Jvyi4iNuKW9A). Claude reads them, designs the post and caption, and saves the result in "מוכן לפרסום" (1AE7Iu3c5h1U1ZPFw9SRTt13BQ8HPIoNT). There is no Instagram/TikTok connector, so the owner (or Meta Business Suite scheduling) does the actual posting.
