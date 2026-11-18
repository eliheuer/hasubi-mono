# Working on Hasubi Mono

Read [CONTEXT.md](CONTEXT.md) for the design and its grades. The working designspace is [Hasubi-Mono.designspace](sources/Hasubi-Mono.designspace). Use the two UFOs it names. The Glyphs file and earlier UFO export document the source history. Keep those originals available for comparison.

## Assigning a batch

The designer names the glyphs, masters, intended change and eligible donor drawings. Record those names and the starting Git revision in the assignment. Existing green marks lock a drawing. The designer confirms which drawings may serve as references. A queue entry suggests work and carries no drawing permission.

Run the [glyph drafting contract](.agents/tasks/glyph-drafts.md) in a clean worktree on a branch from the recorded revision. Keep every change within its assignment. The dependency check reads the base commit, follows every component recursively and reports the glyphs affected by a proposed edit. A protected composite locks its entire chain of donors in that master.

For parallel work, give each writer a separate worktree and disjoint sets of affected glyphs. Keep a glyph and its corresponding masters with one writer when interpolation is involved. Independent assignments may read the same frozen references. Group assignments when one writer would change a drawing the other reads. Give the [visual review contract](.agents/tasks/visual-review.md) to a different reviewer.

## Drawing and review

Edit individual foreground GLIFs. Preserve the other layers, components, anchors, widths, features and grades outside the assignment. Keep existing master compatibility and mark each AI draft purple. Creating a new glyph or modifying a shared source requires an assignment that explicitly includes its registrations and dependencies.

Run the scoped change check, build, QA and proof on the finished batch. Inspect the diff and assign an independent review of the before and after renders. Correct visible faults, rerender and submit the revised proof for review. Commit tested batches with their glyphs and masters in the message. Keep a draft purple until the designer reviews it. Record the designer's grade in a separate review commit. When a correction reveals a reusable design rule, propose it for CONTEXT.md with the review revision.

## Opening the editor

Use the web workspace server with the working designspace. Choose a free port if the default port already serves a project, verify the workspace and entry source, and leave the server running for the session.

```sh
runebender-serve sources/Hasubi-Mono.designspace --open
```

For a different port, add `--port N`. Browser saves write to the served worktree. Use a separate worktree and port for a second assignment. The Runebender MCP configuration targets the native live-editor bridge. Use that bridge only for an explicitly requested native session after verifying the connected document, master and source ID. Use the web workspace for ordinary editor checks.
