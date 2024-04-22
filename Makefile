PWD := $(shell pwd)

BENTOML_HOME := $(PWD)/bentoml

.PHONY: all
all:
	@rm -rf $(BENTOML_HOME)
	@mkdir -p $(BENTOML_HOME)
	@cd vllm-chat && BENTOML_HOME=$(BENTOML_HOME) CLLAMA_MODEL=llama2:7b-chat bentoml build . --version 7b-chat
	@cd vllm-chat && BENTOML_HOME=$(BENTOML_HOME) CLLAMA_MODEL=llama2:7b bentoml build . --version 7b
