# ONDEWO brand kit - common tasks. Run `make help`.
PY        ?= python3
PLATFORMS ?=
PDF_2026  := ondewo_logo_identity_guideline_2026.pdf

.PHONY: help all social guideline guideline-2026 clean-social

help:
	@echo "make social [PLATFORMS=\"linkedin tiktok\"]  build brand-kit/social/<platform>/ (md + svg + png)"
	@echo "make guideline                              social kits + brand-kit/generated/ondewo_logo_identity_guideline.pdf"
	@echo "make guideline-2026                         social kits + $(PDF_2026) in the repo root"
	@echo "make all                                    same as guideline-2026"
	@echo "make clean-social                           remove generated social images"

all: guideline-2026

social:
	$(PY) scripts/build_social.py $(PLATFORMS)

guideline: social
	$(PY) scripts/build_guideline.py

guideline-2026: social
	$(PY) scripts/build_guideline.py -o $(PDF_2026)

clean-social:
	rm -rf brand-kit/social/*/images
