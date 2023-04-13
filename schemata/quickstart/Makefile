
#
all: build-all

.PHONY: proto-gen
proto-gen:
	protoc  --proto_path=org --proto_path=schema --descriptor_set_out=model.desc --include_imports --include_source_info ./**/*.proto

.PHONY: build-all
build-all: proto-gen

