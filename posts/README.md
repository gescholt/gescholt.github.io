# Posts — what the software can do, one story at a time

This directory holds the website posts (epic `globopt_merged-04kq`). A post is not a
showcase page and not a paper section: a showcase page (`docs/showcase/`) documents a
system and its critical set for someone who already wants to use the method; a post
shows one surprising, true thing about a system people recognise, to someone who has
never heard of the method.

Posts are plain Markdown until the website stack is decided (bead 04kq.13); front
matter is added then, nothing else changes.

## The shape of a post

Four parts, in this order, and nothing before the picture except the question.

1. **The question**, as an outsider would ask it. One or two sentences.
2. **The picture or film.** The hero figure draws the critical points *as the models
   they are* — densities over the data, orbits, functions, epidemic curves, molecules —
   never as dots in parameter space. Parameter-space slices come later, cut through a
   symmetry axis so the reader can check the count by eye.
3. **The answer as a count**: how many solutions there are, what finding them cost, and
   where the method breaks. A negative result is part of the story, not left out.
4. **One command** that reproduces the figure, then one link to the showcase page.

## Rules

- Every number carries provenance before the post is published: the ledger `run_id`
  (`experiments/ledger.jsonl`) or the tracked script that recomputes it in seconds —
  the same rule as `docs/showcase/README.md`. A number with neither does not go in.
- The vocabulary on screen and in the text is the public one of
  `docs/videos/youtube_metadata.md` ("approximate map", "fine-tuned", "checked",
  "valley floor", "mountain pass"); a project term is glossed at first use or not used.
- Captions are one declarative line plus a legend.
- Films come from the public-caption renders (`*_public.mp4`, 1440p, ~21 s). Four kinds
  serve the whole series: the **search stages** (raw guesses → fine-tuned → checked), the
  **census gallery** (one critical point after another, each as its model), the **dial**
  (one external quantity sweeps and critical points are born, merge and die), and the
  **landscape sweep** (a level set filling in). The hero still is the last frame of the
  search-stage film, so figure and film agree by construction.
- Each new example adds one film to the "Globtim at work" highlights
  (`docs/videos/highlights/`); that playlist is the series index.
- `assets/` holds the tracked stills: `crops/` (label-free PNG, ready for the web) and
  `vector/` (SVG for the web, PDF for print), with their sources in `assets/README.md`.
  Films are not tracked here; they live under `_generated/youtube/` and on the channel.
- **Handing the material to the website**: `infra/scripts/build_posts_bundle.sh` writes
  `_generated/website_bundle/`, one folder with the posts, this template, `assets/`, the
  public films each post cites (with their title/description drafts), the highlight
  descriptions, the figures of posts not yet drafted, and a `MANIFEST.md` that lists sizes,
  each post's status line and every repo-internal link that still needs a public target.
  Run it from the main checkout, where the film renders are.

## Posts

| File | Status | Source |
|---|---|---|
| [2026-10-eleven-ways-to-the-moon.md](2026-10-eleven-ways-to-the-moon.md) | draft, numbers checked | bead 04kq.1 — 7-D full-costate CR3BP census, showcase `cr3bp_transfers.md`, highlights 1–3 |
| [2026-10-hundreds-of-routes-to-mars.md](2026-10-hundreds-of-routes-to-mars.md) | draft | bead 04kq.2 — Earth→Mars rendezvous catalogue (544), the five-draw map-vs-random comparison (ledgered), films 3, 8, 9, 10 |
| [2026-10-when-the-solution-set-is-a-curve.md](2026-10-when-the-solution-set-is-a-curve.md) | draft, all numbers ledgered | bead 04kq.3 — 4-D L4 chart: one map's 55 hits on the census's traced curves, two through-Earth; films 13/14 (raw, fine-tuned) |

Planned (one bead each under `04kq`): is this mixture one phase or two (.4), the multimodality was in the
loss function (.5), where the method stops (.6), spurious roots are roots of the fit error
(.7); new examples: Gaussian-mixture likelihood (.8), radial-velocity exoplanets (.9), a
tiny neural network (.10), SEIR (.11), Morse clusters (.12).
