# Website illustrations

Picks for advertising globtim on a personal website (2026-09-24). Copies, not
links: the originals may be regenerated. `_generated/` is gitignored.

## crops/ — label-free, ready to use

| File | What it shows | Source |
|---|---|---|
| `mars_census_rotating_square.png` | 544 certified Earth→Mars trajectories, Mars-fixed rotating frame, coloured by transfer time | `_generated/traj_illustrations/mars_census_all_ungrouped.png` (right panel) |
| `mars_census_inertial_square.png` | same census, heliocentric inertial frame | same file (left panel) |
| `earth_moon_L4_transfers.png` | the 11 Earth–Moon transfers to L4 (CR3BP), forbidden region shaded | `_generated/traj_illustrations/cr3bp_census7d_ungrouped.png` (left panel) |
| `fhn3d_levelset_cloud.png` | level set of the FitzHugh–Nagumo misfit in 3 parameters; the cross marks the true parameters | `_generated/fhn_driven_video/fhn3d_levelsets_0.0_0.2_0.35_0.5.png` (right panel) — tick labels still clipped at the edges |

## images/ — full originals (most carry internal titles/legends; crop before use)

- `mars_census_all_ungrouped.png`, `cr3bp_census7d_ungrouped.png`, `cr3bp_4d_export_ungrouped.png` — trajectory censuses, dark background
- `deuflhard.png` — minima of the Deuflhard function; no title, usable as is
- `gallery_polyapprox_levelset.png` — six-hump camel, polynomial critical points and refined minima
- `analytic_hero_step{1,2,3}_*.png` — the method in three panels: sample → polynomial → minima
- `porkchop_earthvenus_figure.png` — Earth→Venus porkchop plot, recovered transfers starred
- `fhn3d_levelsets_0.0_0.2_0.35_0.5.png` — four FHN level sets
- `ode_pe_sir_landscape.png` — SIR epidemic parameter-fitting landscape

## videos/

- `census_all_public.mp4`, `census_T12_public.mp4` — animated Mars census (descriptions in `_generated/youtube/*_public.md`)
- `cr3bp_moon_7d_gateway_*_public.mp4` — Earth–Moon gateway transfers
- `mars_census_all_family_facet.mp4` — Mars census by family
- `fhn3d_levelset_sweep.mp4` — FHN level-set sweep (33 MB; re-encode before putting on the web)

## vector/ — SVG (web) + PDF (print)

Re-rendered from source with CairoMakie's vector backend (2026-09-24), not traced from the PNGs.

| File | Pure vector? | Source |
|---|---|---|
| `camel_levelset.{svg,pdf}` | yes | section 1 of `pkg/globtimplots/examples/gallery.jl` |
| `deuflhard.{svg,pdf}` | yes | rebuilt with `cairo_plot_polyapprox_levelset` (inferno, Chebyshev levels, d = 12, box ±1.2; all 6 minima captured). The original PNG's script no longer exists: `generate_deuflhard()` now draws a different two-panel figure. Minima are red, not blue, in the current plotting code. |
| `hero_step{1,2,3}_*.{svg,pdf}` | yes | `generate_hero_step{1,2,3}` in `pkg/globtim/docs/scripts/generate_illustrations.jl` |
| `porkchop_earthvenus.{svg,pdf}` | yes | `experiments/sandbox/figure_porkchop.jl` on `_generated/astro/metrics_porkchop_earthvenus.jsonl` |
| `sir_landscape.{svg,pdf}` | no: 4 embedded rasters (heatmap, surface) | paper figure `CertifiedParameterEstimation/georgy_update/images/sir_landscape.pdf` |

Not exported as vector, on purpose: the trajectory censuses (every gradient-coloured
segment becomes its own stroke: 1 GB for the 689-arc figure, 36 MB for the 11-arc one,
per the comment in `cr3bp_transfer_video.jl`) and the FHN point cloud (~100k points).
Use the high-resolution PNGs in `crops/` for those.

## Tracked copy (2026-10-18, bead 04kq.13)

`crops/`, `vector/` and this file were copied from `_generated/website_illustrations/`
into `docs/posts/assets/` so the website picks survive a regeneration. `images/` and
`videos/` were not copied (15 MB and 86 MB; the films live under `_generated/youtube/`
and on the channel). The `_generated/traj_illustrations/*.png` stills that `crops/` were
cut from have no tracked generator on `dev-main` as of this date (the census films' branch,
bead 25k2.2, is not landed); the tracked, labelled equivalents are in `docs/showcase/assets/`.

## POST-3 figures (2026-10-19, bead 04kq.3)

Both rendered from the ledgered run `20261019T194131_post3_hit_curve_globtim_4d`
(`globtim_results/local/post3_hit_curve/20261019T193232/hits.jsonl`) by the runbook
`experiments/sandbox/post3_hit_curve/README.md`, step 6:

| file | generator | what |
|---|---|---|
| `crops/l4_routes_from_one_fit.png` | `pkg/Opt_Traj/examples/specialized/cr3bp_transfer_video.jl --candidates hits.jsonl --stage basin --clean --public --still` | the 52 flyable hits of one map as routes, synodic and inertial panels (3 through-Earth arcs suppressed by `--clean`) |
| `crops/l4_hit_curves.png` | `experiments/sandbox/post3_hit_curve/curve_figure.py --hits hits.jsonl --seed-run …_trace` | the census curves in (flight time, λv_z) with the 55 hits; reads only committed runs |
