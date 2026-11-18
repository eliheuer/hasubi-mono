# Draft assigned glyphs

Start from the coordinator's base commit in a separate worktree. The assignment supplies glyph names, masters, the requested change and the designer's eligible references. Put the base SHA in `BASE`, space-separated glyph names in `GLYPHS`, and space-separated master names in `MASTERS`.

1. Read AGENTS.md and CONTEXT.md. Check the dependency closure before drawing. Report a lock to the coordinator and skip the protected drawing. Share the affected names with the coordinator so parallel assignments can be checked for overlap.

   ```sh
   .venv/bin/python sources/check_donors.py --plan --base "$BASE" --glyphs "$GLYPHS" --masters "$MASTERS"
   ```

2. Render the named glyphs and affected words at the starting revision. Use a separate directory under `output/` for each comparison. Take the construction from the designer's approved references. If no reference answers a construction question, report the specific decision.
3. Make the assigned change and mark the drawing purple. Follow component references when checking the effect on other glyphs and include affected composites in the proof.
4. Run the checks and open the new proofs. Use the recorded base SHA throughout.

   ```sh
   make check-changes BASE="$BASE" GLYPHS="$GLYPHS" MASTERS="$MASTERS"
   make build
   make test NO_BUILD=1
   make proof NO_BUILD=1
   make render BASE="$BASE" GLYPHS="$GLYPHS"
   ```

5. Give the render, the proof, names of affected glyphs, masters and family rules to the independent reviewer. Revise any visible fault and rerun the checks and review for the changed drawings.
6. Checkpoint the tested batch on the assignment branch. Report its commit, source and donor names, affected composites, proof paths, check results and any unresolved design decisions. The coordinator integrates reviewed checkpoints and reruns the checks on the combined working tree. The designer grades the work.

For accented letters, include the base, mark, precomposed form and decomposed text sequence in each review. A request about one accent applies only to the named glyphs and masters. Preserve shared base and mark anchors unless they are separately assigned and clear the protection check.
