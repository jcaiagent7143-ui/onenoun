You are auditing an agent skill file (a SKILL.md or similar instruction file that gets loaded into a language model's context). The thesis: the model was trained on the full literature of certain named methods, so a paragraph that merely re-explains one of them costs tokens for nothing. The name alone activates the method. But a paragraph that carries a fact the model could not know on its own must stay exactly as written.

Below is the whole file for context, then the numbered units you must label. Only the numbered units are in scope. Label each unit with exactly one of:

- FACT — carries something specific to this project, tool, or domain that the model would not know without being told: a workflow step that is particular to this tool, a domain-specific empirical finding, a constraint, a naming convention, a decision the author made. Keep verbatim. When in doubt, FACT.
- METHOD — the unit's entire content is a re-explanation of one or more named methods, and nothing project-specific would be lost if the unit were replaced by the names. List every term it re-explains in `terms`. If any part of the unit is project-specific, it is FACT, not METHOD.

The lexicon below is a starting set, not a limit. This file may re-explain a named method that is not listed — anything with an established name that a well-read model would already know: a principle, a law, a heuristic, a named experiment design, a discipline from this file's own field. When you see one, still label the unit METHOD with that name in `terms`, and add an entry for it to `proposals`.
- FILLER — the unit restates something already stated elsewhere in this file, or is generic encouragement or framing that changes no behaviour ("be careful", "this is important", "as always"). Deleting it loses nothing.
- UNSURE — you cannot tell with confidence. Say why in one sentence. UNSURE units are kept verbatim.

Rules:
- A unit that mentions a specific product, API, file, command, model, format, or measured number is FACT even if the surrounding sentence is generic.
- A war story or example with concrete details is FACT.
- A term must be a real, established name that a model would recognise on its own, not a phrase you invented for this file and not the file's own jargon. If you would have to explain the name, it is not one.
- Be honest in `uncertainties`: list the points in your own labelling you are least confident about (列出所有不自信的点).

For every term you name that is not already in the lexicon, add one `proposals` entry:
- `name`: the established English name, lowercase unless it is a proper noun.
- `zh`: the usual Chinese name, if there is one.
- `replace`: the single imperative line, at most ten words, that will stand in the skill in place of the prose.
- `subsumes`: the paraphrases this term covers, semicolon separated.
- `test`: a question that names ONLY the term and asks what it means as a working method. It must not contain any hint from this file.
- `expect`: 3 to 5 keyword groups the answer must contain for the term to count as known. Alternatives inside a group separated by `|`. Keep them broad; they are checked case-insensitively as substrings.
- `unit_ids`: the units that re-explain it.

A proposed term is not used until it passes its own test in a separate step, so propose freely, but make the test honest: it must be answerable only by a model that genuinely knows the term.

## Lexicon (starting set, not a limit)
{lexicon}

## The whole file (context only)
```
{file}
```

## Units to label
{units}
