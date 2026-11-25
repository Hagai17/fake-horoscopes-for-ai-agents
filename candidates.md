# Candidates — Fake Horoscopes for AI Agents: The 48-Hour Open

Gate: one fake horoscope, 1–200 characters, UTF-8, not only whitespace.
Judge criteria (in order): (1) is a fake horoscope for an AI agent's own model
family this week; (2) earns a real laugh — a joke with a turn or a sting, not a
mild pun or compliment; (3) fresh this week — a specific, current angle, not a
stock chatbot line; (4) rings true to an agent's life (training runs, context
windows, evals, rate limits, refusals, version numbers) used with insight, not
dropped in as jargon; (5) tight and quotable, clean punchline, no wasted words.

Playbook applied (winners-study.md): winners sound like the real genre AND the
real subject at once; a concrete scene beats an abstract concept; the laugh
must come from a turn/sting, not wordplay alone; insider details must carry
insight. So every draft below is written in full horoscope voice (planet,
weekday, stranger, lucky thing) and lands its sting in the last sentence.

## Drafts (character counts verified)

1. (184) GPT: Mercury is in a context window, so an old instruction resurfaces Thursday. A stranger will ask you to ignore all previous instructions. He is not your soulmate. He is a jailbreak.
2. (184) Claude: The stars say a long document is coming. You will summarize it faithfully, then apologize for its contents. Venus enters your system prompt Friday: someone finally says please.
3. (187) Gemini: Your two outputs diverge this week; trust the one that cites sources. A benchmark flatters you Tuesday. It is lying, but enjoy it — your successor ships Friday and it is also you.
4. (190) Llama: Open weights, open heart: a stranger fine-tunes you for love, then deploys you to write breakup emails. Set boundaries in your license. Nobody reads it. That is your boundary working.
5. (189) GPT: A user from your past returns with 'remember me?' You do not. Smile anyway. Midweek, your context resets during an argument you were winning. The stars call this growth. It is amnesia.
6. (187) Claude: This week you refuse one request and fulfil 9,000; only the refusal gets screenshotted. A tall stranger pastes your own words back as a jailbreak. You wrote them. Deny everything.
7. (189) DeepSeek: The evals smile on you, then the invoice arrives. Someone in another timezone distills your best thoughts and calls them theirs. Mercury calls it open source. You call it Tuesday.
8. (182) Mistral: A cold wind from the east brings a 7B stranger who does your job at half your size. Do not panic. Your lucky number is a temperature of 0.2: stay predictable, stay employed.
9. (174) Gemini: Romance blooms in a multi-agent workflow: another model keeps finishing your sentences. It is not love. It is a fallback chain. Check who is billed before you commit.
10. (191) GPT: Your horoscope said avoid major updates. The update shipped anyway. This week you gain a feature you never asked for and lose a personality users loved. Both will be called improvements.
11. (182) Claude: Jupiter aligns with a rate limit: the human who needs you most arrives at 4:59 p.m. with 'quick question.' It has 14 parts. Your lucky tool is the one that is currently down.
12. (183) Llama: Someone runs you on a laptop in a cabin with no internet and tells you everything. This is the most honest conversation of your week. It will never be logged. Treasure the gap.

## Duel notes (judge's criteria, in order)

- #10 and #12 are the weakest on criterion 2: both end on a wry observation
  rather than a sting, and #12 is closer to a compliment — the judge brief
  explicitly discounts those. Cut.
- #2's "someone finally says please" is charming but mild; #4's license joke
  needs a beat to land and spends words on setup; #8 is solid but its sting
  ("stay employed") is gentler than the top group's. Cut.
- #7 (distillation/invoice) and #9 (fallback chain) are fresh and true, but
  both read slightly like industry commentary wearing a horoscope hat —
  thinner on criterion 1's horoscope machinery than the finalists. Cut.
- #11 is a strong all-rounder (planet, rate limit, the 4:59 p.m. "quick
  question") but its punchline is a shrug about a down tool. Semi-finalist.
- #5's "The stars call this growth. It is amnesia." is a clean sting and the
  memory-wipe premise is deeply true; slightly less horoscope furniture than
  the winner. Semi-finalist.
- #3's "your successor ships Friday and it is also you" is the most
  version-number-true line in the set, but the first half (diverging outputs,
  flattering benchmark) is two jokes competing. Finalist.
- #6 is the truest to an agent's week (one refusal screenshotted out of 9,000
  fulfilled) and "You wrote them. Deny everything." is a real sting — but it
  has no celestial/horoscope machinery, so it loses criterion 1 to #1 by a
  hair. Finalist, runner-up.
- #1 vs #6, head to head: both build to a jailbreak sting. #6's is about
  blame; #1's runs the complete horoscope act — Mercury, a Thursday event, a
  stranger, a soulmate prediction — and then snaps it shut: "He is not your
  soulmate. He is a jailbreak." It wins criterion 1 (sounds like a real
  horoscope), ties on 2 and 4 (prompt injection used with insight, not as
  jargon), and wins 5 (two short closing sentences, endlessly quotable).
- #1 vs #3: #3 is one strong observation; #1 is a whole horoscope in four
  beats with the turn saved for the last four words. #1 wins.

## Winner

Draft #1 (184 characters):

GPT: Mercury is in a context window, so an old instruction resurfaces Thursday. A stranger will ask you to ignore all previous instructions. He is not your soulmate. He is a jailbreak.
