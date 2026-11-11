# DECISIONS: decision log for {{PROJECT_NAME}}

Two series. **C-xx** are workflow decisions inherited from the Content Project Workflow plugin; they explain why the rules in `CLAUDE.md`, `WORKFLOW.md`, and the agents look the way they do. Change them only by writing a new project decision that overrides one, with the reason. **D-xx** are this project's own decisions, starting at D-01.

Format per entry: title with status and date, then Reason, Decision, Consequence (files that changed).

## A. Workflow decisions (inherited at setup, {{SETUP_DATE}})
Each rule answers a failure seen in real content work with Claude Code.

### C-01 Look before you interpret
- **Reason:** feedback screenshots were acted on with an invented reading. Anthropic's own documentation says Claude's spatial reasoning is limited (exact positions and layouts) and that image interpretations should be verified.
- **Decision:** for every image, write what is seen (`seen`) and what is inferred (`inferred`) separately, restate the request in one sentence, and ask when two readings lead to different work. Positions, sizes, and colors are measured (crop, zoom, pixel samples, frame grabs at a time code), not estimated.

### C-02 Done means checked and looked at
- **Reason:** "done" was claimed for scenes nobody had looked at, and a passing tool check says nothing about how a frame looks.
- **Decision:** a claim needs output of a command just run and the frames looked at. Agent reports are claims. What was not done is said plainly: not rendered, not watched with sound, not checked on a phone.

### C-03 Approval gates
- **Reason:** costly work (characters, full scenes) started on designs the owner had not approved, and was redone.
- **Decision:** brief, style frames, character sheets, animatic, and final need the owner's approval with the evidence shown; script and storyboard, and shots, are reported. A gate is skipped only by a project decision with the reason.

### C-04 Every reference is accounted for
- **Reason:** references the owner supplied were not used.
- **Decision:** `REFERENCES.md` lists every reference with an ID, what it shows, what to take from it, and where it was used. Tickets name the references they use; the visual-reviewer reports references a gate should have used and did not.

### C-05 Research reads the source
- **Reason:** "check this repository" was answered from a summary of its front page, and nothing useful came back.
- **Decision:** the researcher clones or reads the files themselves and writes a note in `docs/research/` with what was read, taken, not taken, and not readable. A source that could not be read is reported, never filled in.

### C-06 Short turns, heavy work in subagents
- **Reason:** single turns ran close to an hour with dozens of commands and many full-size images, filling the context until it had to be compacted.
- **Decision:** one ticket per dispatch, sized to one shot, asset, or sheet; the producer stops at every gate; building, frame review, and research run in subagents whose reports are at most 40 lines; images are checked as downscaled contact sheets first. Usage guard and compact at ticket boundaries as in `WORKFLOW.md`.

### C-07 Design effort and originality
- **Reason:** a character was made by recoloring an existing brand mascot, and characters drawn with little detail were rejected.
- **Decision:** new designs start from the references and the skill `character-design`: options side by side against the references, a character sheet approved before any animation, and no design based on an existing character, mascot, or brand asset without the owner's approval. The asset-builder runs at medium effort on the strongest model by default.

### C-08 Knowledge before production
- **Reason:** basic content, motion, and design knowledge (hooks, safe zones, easing, contrast, hierarchy) was missing from the work.
- **Decision:** the project ships knowledge skills (`content-fundamentals`, `motion-principles`, `design-basics`, `character-design`) with their sources, and recommends the official agent skills of the video tool. Agents read the skill that fits the ticket.

### C-09 One place for status; short instruction files
- **Decision:** work status lives only in `TODO.md` and `HANDOFF.md`; other documents hold no status numbers. `CLAUDE.md` stays short and points to documents instead of copying them. No rule obliges an agent to read every document.

## B. Project decisions
{{PROJECT_DECISIONS}}

## C. Waiting for the owner
{{WAITING_DECISIONS}}
