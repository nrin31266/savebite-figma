# Keyboard outer-surface correction ·01/11/2026 ·DEC-034

**Subsequent DEC-035:** [native keyboard height/100 device corners](native27-device-checkpoint.md) corrects291→307pt and y561→545. Square keyboard background remains;root radius50 clips device corners. Screenshots below are historical geometry.

**AWAITING_OWNER_REVIEW.** Owner rejects rounded keyboard surface in009. Corrected009/019/020 to square, edge-to-edge393×291 at x0/y561. All four nested Background corners changed from27/27/62/62 to0; source-radius bindings removed only on these App instances. Native keycaps, source linkage, callbacks and020 visibility binding retained. No new main/token/asset.

Native read-back and individual screenshots PASS: [009](evidence/keyboard-square/SB-009.png),[019](evidence/keyboard-square/SB-019.png),[020](evidence/keyboard-square/SB-020.png),[IDs/radii/key geometry](evidence/keyboard-square/readback.json). Key geometry compared before/after with no drift. An initial combined export omitted static key layers on019/020; separate exports recover them, matching the existing capture limitation. No claim of global render repair.

Supersedes outer-radius retention and screenshots in [DEC-032/033 checkpoint](vn-final-ui-checkpoint.md) for these three roots only. External source Background750:11763 remains unchanged;207 component records/33 assets/100 roots retained. Full logic/actual-device testing not rerun;prototype_verified=false,DONE0,owner acceptance pending.

PASS final repository checks:python3 scripts/validate.py (100 IDs/207 components/33 asset hashes/7 skills/DONE0),git diff --check,three393×852 PNGs/one JSON decoded;all three backgrounds0 and key geometry unchanged. Lease codex/keyboard-square RELEASED after checkpoint checks. No agents, commit or push.
