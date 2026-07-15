---
title: AI use policy
description: How to use AI tools when contributing to BeeHive — you are accountable for what you submit.
---

# AI use policy

BeeHive welcomes contributions made with the help of AI tools — but **you are
responsible for everything you submit**. This page sets out how to use them well.

## The core principle

We are humans who enjoy working with other humans. Use whatever tools help you,
but you are ultimately accountable for the boards, code, and documentation you
contribute. If you would not be comfortable explaining a change and standing
behind it, it is not ready to submit.

## Please don't

- Let an AI agent open pull requests on your behalf.
- Submit a board design, recipe, code, or docs change you have not personally
  understood and tested.
- Let a chatbot carry on a conversation (an issue thread, a PR review) for you.

Pull requests that appear to ignore these guidelines may be closed without
review — checking un-vetted machine output costs maintainers more time than it
saves.

## Using AI to build and code

- **Get familiar with what you are changing first.** Understanding the board,
  the [design rules](introduction/design-rules.md), or the code you are touching
  lets you write better prompts *and* judge whether the output is right.
- **Don't trust an assistant's claims about how BeeHive works.** LLMs are often
  confidently wrong, even about things the docs answer directly. Check against
  the design rules, the board's schematics, or a real device.
- **Test on hardware.** A recipe or snippet that looks plausible is not a
  contribution until it actually runs on the boards it claims to.
- **Keep pull requests small and focused,** even if a tool generated everything
  in one go. One board, one recipe, or one fix per PR is far easier to review.
- **Edit AI-written comments and prose.** Prefer clarity and brevity over
  exhaustive, generic text; delete comments that just restate the code.

## Using AI to communicate

- **Say why, not what.** A PR description that merely restates the diff adds
  nothing — explain your reasoning and what you tested.
- **Fill in the templates yourself.** Issue and PR templates exist to save
  everyone time; complete them rather than having a tool do it.
- **Verify anything you post.** Don't paste unchecked AI output into an issue or
  a pull request.
- **Link, don't quote.** Pointing to the primary source — a datasheet, the docs,
  a repo file — beats quoting an LLM. If you must quote one, put it in a
  `>` blockquote so it is clearly machine output, not your own words.
- **Clarity over polish.** A clear, slightly imperfect message beats a
  perfectly-worded one that hides the point.

## Attribution

This policy is adapted from the
[napari AI use policy](https://napari.org/dev/developers/contributing/ai.html),
which was itself adapted from Zulip's AI usage guidelines.
