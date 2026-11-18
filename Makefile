PYTHON = .venv/bin/python
FGTOOLS = .venv/bin/fgtools
BASE = main
BUILD = $(if $(NO_BUILD),,build)

##@ Help

help: ## Print this list
	@awk -F ':.*## ' '/^##@ / {printf "\n%s\n", substr($$0, 5)} /^[a-z-]+:.*## / {printf "  make %-18s %s\n", $$1, $$2}' Makefile
	@echo
	@echo 'A target that says "Build, then" skips the build with NO_BUILD=1, for example: make test NO_BUILD=1'

##@ Setup

setup: ## Install the pinned Python and Rust tools of the project into .venv/
	python3 -m venv .venv
	$(PYTHON) -m pip install -r requirements.txt
	$(FGTOOLS) install-tools

venv: setup

##@ Build and test

build: ## Build the fonts into fonts/ with fontmake
	$(FGTOOLS) build --compiler fontmake

test: $(BUILD) ## Build, check the repository and run the full Hasubi QA gate
	$(PYTHON) sources/check_repository.py
	$(PYTHON) sources/check_qa.py $(QA_OPTIONS)

test-google-fonts: $(BUILD) ## Build, then run only the Google Fonts checks
	$(FGTOOLS) qa --checks google-fonts

test-fontgarden: $(BUILD) ## Build, then run only the Font.Garden checks and the checks of this font
	$(FGTOOLS) qa --checks fontgarden

##@ Design work

status: ## Count the glyphs of each mark color into STATUS.md
	$(FGTOOLS) status

queue: ## List the glyphs that are not green, the ones that most composites use first
	$(FGTOOLS) queue

check-design: ## Check glyphs against the rules of CONTEXT.md: make check-design GLYPHS="n a"
	$(PYTHON) sources/check_design.py $(GLYPHS)

check-changes: ## Guard protected glyphs, donors and assigned glyph/master scope
	$(PYTHON) sources/check_donors.py --base "$(BASE)" $(if $(GLYPHS),--glyphs "$(GLYPHS)",) $(if $(MASTERS),--masters "$(MASTERS)",)

render: ## Draw glyphs large for review into output/render/: make render GLYPHS="a n"
	@test -n "$(GLYPHS)" || { echo 'Name the glyphs: make render GLYPHS="a n"' >&2; exit 2; }
	$(FGTOOLS) render "$(GLYPHS)" --base "$(BASE)"

diff: ## Build main, or BASE=..., and the working tree, and compare them with diffenator3 into output/diff/
	$(PYTHON) sources/compare_builds.py "$(BASE)"

PORT ?= 8765
runebender: ## Open Hasubi in the web editor (PORT=... selects another port)
	runebender-serve sources/Hasubi-Mono.designspace --port $(PORT) --open

##@ Proofs, specimen and media

formats: ## List the names that FORMAT, CANVAS and PAGE take
	$(FGTOOLS) media --list

proof: $(BUILD) ## Build, then write the print proof to output/proof/proof.pdf, or its pages PAGE=...
	$(PYTHON) sources/print_proof.py $(PAGE)

specimen: $(BUILD) ## Build, then write the print specimen to output/specimen/, or its pages PAGE=...
	$(FGTOOLS) media --specimen $(PAGE)

media: $(BUILD) ## Build, then render the images, carousels and videos into output/media/, or FORMAT=... CANVAS=...
	$(FGTOOLS) media $(FORMAT) $(if $(CANVAS),--canvas $(CANVAS),) $(if $(LATTICE),--lattice,)

copy-format: ## Copy a default format into documentation/media/ to change it: make copy-format FORMAT=words
	@test -n "$(FORMAT)" || { echo 'Name the format: make copy-format FORMAT=words' >&2; exit 2; }
	$(FGTOOLS) media --copy $(FORMAT)

site: proof test ## Build the print proof and full QA site for GitHub Pages
	$(MAKE) collect-site

collect-site: ## Collect the existing proof and QA reports into output/site/
	$(FGTOOLS) site
	cp -R output/qa/all output/site/qa
	cp documentation/site.html output/site/index.html

proof-web: $(BUILD) ## Build, then serve the font beside the fonts of reference-fonts/ in a browser
	$(FGTOOLS) proof-web --current

##@ Housekeeping

clean: ## Remove fonts/ and output/
	rm -rf fonts output

.PHONY: help setup venv build test test-google-fonts test-fontgarden status queue check-design check-changes render diff runebender formats proof specimen media copy-format site proof-web collect-site clean
